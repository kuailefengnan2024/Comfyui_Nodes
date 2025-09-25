class MyFirstNode:
    """
    一个节点的简短描述会显示在这里。
    """
    @classmethod
    def INPUT_TYPES(s):
        """
        这个方法定义了节点的输入参数。
        返回的字典结构如下:
        {
            "required": {
                "参数名": ("类型", {"选项": "值"}),
                ...
            },
            "optional": {
                ...
            }
        }
        常见的类型有: STRING, INT, FLOAT, BOOLEAN, IMAGE, MASK。
        """
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True, # 让文本框可以输入多行
                    "default": "Hello World!"
                }),
                "value": ("INT", {
                    "default": 1, 
                    "min": 0,    # 最小值
                    "max": 100,  # 最大值
                    "step": 1    # 步长
                }),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("处理后的文本",) # 可选，定义输出参数的名称

    FUNCTION = "process" # 执行功能的函数名

    # 节点在UI菜单中的分类
    CATEGORY = "我的节点"

    def process(self, text, value):
        """
        这是节点的核心逻辑。
        函数的参数必须和 INPUT_TYPES 中定义的 required 参数名完全一致。
        返回值必须是一个元组 (tuple)，且与 RETURN_TYPES 中定义的类型一一对应。
        """
        processed_text = f"{text} (数值: {value})"
        
        # 返回值必须是元组
        return (processed_text,)


# ComfyUI必须的字典，用于映射节点类名和显示名称
NODE_CLASS_MAPPINGS = {
    "MyFirstNode": MyFirstNode
}

# 节点在UI中显示的友好名称
NODE_DISPLAY_NAME_MAPPINGS = {
    "MyFirstNode": "我的第一个节点"
}
