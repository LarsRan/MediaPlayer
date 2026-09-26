from __future__ import annotations

import sys
from pathlib import Path

from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from app.config.settings import ConfigStore
from app.render.plugins.industrial_meter import plugin as industrial_meter_plugin
from app.render.registry import VisualizerRegistry
from app.ui.backend import UIBackend


def main() -> int:
    app = QGuiApplication(sys.argv)
    root = Path(__file__).resolve().parent
    config_store = ConfigStore(root / "config", Path.home() / ".mediaplayer")
    app_config = config_store.load_defaults()
    shortcuts = config_store.load_shortcuts()
    theme = config_store.load_theme()["colors"]

    registry = VisualizerRegistry()
    registry.register(industrial_meter_plugin())

    backend = UIBackend(config_store, app_config, registry)

    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("backend", backend)
    engine.rootContext().setContextProperty("shortcuts", shortcuts)
    engine.rootContext().setContextProperty("themeColors", theme)
    main_qml = root / "ui" / "Main.qml"
    engine.load(QUrl.fromLocalFile(str(main_qml)))
    if not engine.rootObjects():
        return 1
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
