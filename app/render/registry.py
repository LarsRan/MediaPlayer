from __future__ import annotations

from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True, slots=True)
class VisualizerPlugin:
    plugin_id: str
    title: str
    qml_component: str


class VisualizerRegistry:
    def __init__(self) -> None:
        self._plugins: dict[str, VisualizerPlugin] = {}

    def register(self, plugin: VisualizerPlugin) -> None:
        self._plugins[plugin.plugin_id] = plugin

    def list_plugins(self) -> list[VisualizerPlugin]:
        return list(self._plugins.values())

    def get(self, plugin_id: str) -> VisualizerPlugin:
        return self._plugins[plugin_id]
