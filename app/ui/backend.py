from __future__ import annotations

from pathlib import Path
from PySide6.QtCore import QObject, Property, Signal, Slot

from app.config.settings import AppConfig, ConfigStore
from app.render.registry import VisualizerRegistry


class UIBackend(QObject):
    statusChanged = Signal()
    commandPaletteVisibleChanged = Signal()
    visualizerChanged = Signal()

    def __init__(
        self,
        config_store: ConfigStore,
        app_config: AppConfig,
        registry: VisualizerRegistry,
    ) -> None:
        super().__init__()
        self._config_store = config_store
        self._config = app_config
        self._registry = registry
        self._status = "就绪"
        self._command_palette_visible = False
        self._visualizer_id = self._config.render["visualizer"]

    @Property(str, notify=statusChanged)
    def status(self) -> str:
        return self._status

    @Property(bool, notify=commandPaletteVisibleChanged)
    def commandPaletteVisible(self) -> bool:
        return self._command_palette_visible

    @Property(str, notify=visualizerChanged)
    def visualizerId(self) -> str:
        return self._visualizer_id

    @Slot(str)
    def executeCommand(self, command: str) -> None:
        if command == "toggle_command_palette":
            self._command_palette_visible = not self._command_palette_visible
            self.commandPaletteVisibleChanged.emit()
            return
        if command == "cancel":
            self._command_palette_visible = False
            self.commandPaletteVisibleChanged.emit()
            return
        self._status = f"命令已执行: {command}"
        self.statusChanged.emit()

    @Slot(str)
    def setStatus(self, text: str) -> None:
        self._status = text
        self.statusChanged.emit()

    @Slot(str)
    def switchVisualizer(self, plugin_id: str) -> None:
        if plugin_id not in {p.plugin_id for p in self._registry.list_plugins()}:
            self._status = f"未知可视化: {plugin_id}"
            self.statusChanged.emit()
            return
        self._visualizer_id = plugin_id
        self.visualizerChanged.emit()
        self._status = f"可视化已切换: {plugin_id}"
        self.statusChanged.emit()
