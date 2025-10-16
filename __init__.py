# 从第一个文件中导入节点，并重命名以避免冲突
from .nodes.my_first_nodes import NODE_CLASS_MAPPINGS as text_nodes, NODE_DISPLAY_NAME_MAPPINGS as text_nodes_display

# 从新的图像节点文件中导入
from .nodes.image_nodes import NODE_CLASS_MAPPINGS as image_nodes, NODE_DISPLAY_NAME_MAPPINGS as image_nodes_display

# 从图像选择节点文件中导入
from .nodes.image_selection_nodes import NODE_CLASS_MAPPINGS as selection_nodes, NODE_DISPLAY_NAME_MAPPINGS as selection_nodes_display

# 导入新的测试节点
from .nodes.test_node import NODE_CLASS_MAPPINGS as test_nodes, NODE_DISPLAY_NAME_MAPPINGS as test_nodes_display

# 将所有导入的节点合并到一个字典中
NODE_CLASS_MAPPINGS = {**text_nodes, **image_nodes, **selection_nodes, **test_nodes}
NODE_DISPLAY_NAME_MAPPINGS = {**text_nodes_display, **image_nodes_display, **selection_nodes_display, **test_nodes_display}

# 将合并后的字典导出给 ComfyUI
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
