import torch
import numpy as np

class MyImageNode:
    """
    一个简单的图像节点示例，它会直接传递输入的图像。
    """
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "process_image"

    CATEGORY = "我的节点/图像"

    def process_image(self, image):
        # 在这个示例中，我们只是将输入的图像直接返回。
        # 'image' 是一个 torch 张量。
        return (image,)

# 用于 ComfyUI 注册的字典
NODE_CLASS_MAPPINGS = {
    "MyImageNode": MyImageNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MyImageNode": "我的图像节点"
}
