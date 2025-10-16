# Comfyui_Nodes by kuailefengnan2024

一套为 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 开发的自定义节点。

## 安装

1.  进入 `ComfyUI/custom_nodes/` 目录:
    ```bash
    cd ComfyUI/custom_nodes/
    ```

2.  克隆本仓库:
    ```bash
    git clone https://github.com/kuailefengnan2024/Comfyui_Nodes
    ```

3.  安装依赖 (如果需要):
    ```bash
    cd Comfyui_Nodes
    pip install -r requirements.txt
    ```
    
4.  重启 ComfyUI.

## 节点示例

### 文本 (`nodes/my_first_nodes.py`)

*   **我的第一个节点**: 简单的文本处理示例。
    *   **输入**: `text` (字符串), `value` (整数)
    *   **输出**: `处理后的文本` (字符串)

### 图像 (`nodes/image_nodes.py`)

*   **我的图像节点**: 简单的图像处理示例。
    *   **输入**: `image` (图像)
    *   **输出**: `image` (图像)

*(更多节点正在开发中...)*

---

## 开发须知

添加新节点时，必须完成以下两步：

### 1. 在 `__init__.py` 中注册

此步骤是为了让 ComfyUI **发现**新节点。

1.  **导入**: 在 `__init__.py` 中添加 `from .nodes.新节点文件名 import ...`
2.  **合并**: 将导入的 `NODE_CLASS_MAPPINGS` 和 `NODE_DISPLAY_NAME_MAPPINGS` 添加到主字典中。

*如果跳过此步骤，新节点将无法在 ComfyUI 中显示。*

### 2. 在节点代码中设置 `CATEGORY`

此步骤是为了将所有节点**分组**到同一个菜单项下。

-   在节点类中，统一设置 `CATEGORY = "donyan"` 即可。