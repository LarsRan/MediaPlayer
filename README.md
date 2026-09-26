# MediaPlayer

MediaPlayer v2 uses Python 3.12 + PySide6(QML) + GPU shader rendering.

## 运行

1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
2. 启动：
   ```bash
   python -m app.main
   ```

## 借鉴与合规

- 设计思想借鉴：wavesurfer.js（BSD-3-Clause）、Tone.js、pyqtgraph。
- 仅借鉴思路：峰值缓存、多级缩略、Region(A-B Loop)、可视化插件注册。
- 未复制以上项目的代码、命名、注释和资源。
