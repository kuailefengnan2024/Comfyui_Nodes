import torch
import json

class SelectBestImageByScore:
    """
    一个根据输入的分数选择最佳图像的节点。
    """
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "images": ("IMAGE",),
                "scores_json": ("STRING", {
                    "multiline": True,
                    "default": '[{"aesthetic": 6.5, "clarity": 8.0}]'
                }),
            }
        }

    RETURN_TYPES = ("IMAGE", "STRING")
    RETURN_NAMES = ("best_image", "best_scores")
    FUNCTION = "select_best"
    CATEGORY = "donyan"

    def select_best(self, images, scores_json):
        scores_list = []
        # 尝试将输入作为标准的JSON列表解析
        try:
            scores_list = json.loads(scores_json)
        except json.JSONDecodeError:
            # 如果失败，则尝试按行解析 (JSON Lines格式)
            lines = scores_json.strip().split('\n')
            for line in lines:
                line = line.strip()
                if line:
                    try:
                        scores_list.append(json.loads(line))
                    except json.JSONDecodeError:
                        raise ValueError(f"无法解析此行，请确保每行都是一个有效的JSON对象: {line}")

        if not scores_list:
            raise ValueError("解析后的分数列表为空。")

        num_images = images.shape[0]
        num_scores = len(scores_list)

        # 2. 检查图片数量和分数数量是否匹配
        if num_images != num_scores:
            raise ValueError(f"图片数量 ({num_images}) 与分数条目数量 ({num_scores}) 不匹配。")
        
        if num_images == 0:
            return (torch.empty(0), "[]")

        best_score = -1.0
        best_index = -1

        # 3. 计算每张图片的总分并找到最高分
        for i, scores in enumerate(scores_list):
            if not isinstance(scores, dict):
                raise TypeError(f"分数列表中的第 {i+1} 个元素不是一个有效的对象 (dict)。")
            
            current_total_score = sum(scores.values())
            
            if current_total_score > best_score:
                best_score = current_total_score
                best_index = i

        if best_index == -1:
            raise ValueError("无法确定最佳图片，请检查分数。")

        # 4. 提取最佳图片和其分数
        best_image_tensor = images[best_index].unsqueeze(0)
        best_scores_dict = scores_list[best_index]

        return (best_image_tensor, json.dumps(best_scores_dict, indent=2))

# ComfyUI节点映射
NODE_CLASS_MAPPINGS = {
    "SelectBestImageByScore": SelectBestImageByScore
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SelectBestImageByScore": "Select Best Image by Score"
}
