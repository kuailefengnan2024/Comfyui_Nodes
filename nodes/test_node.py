class SimpleTestNode:
    """
    一个用于诊断的极简测试节点。
    它只接收一个字符串并将其返回，以确认节点加载是否成功。
    """
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"default": "如果看到我，说明加载成功了！"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output_text",)
    FUNCTION = "run"
    CATEGORY = "Test" # 使用一个独特的分类，方便查找

    def run(self, text):
        # 在后台打印一条消息，方便在控制台确认
        print("SimpleTestNode 正在运行...")
        
        # 返回处理后的文本
        return (f"测试节点输出: {text}",)

# ComfyUI节点映射
NODE_CLASS_MAPPINGS = {
    "SimpleTestNode": SimpleTestNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SimpleTestNode": "Simple Test Node"
}
