from __future__ import annotations

from app.render.registry import VisualizerPlugin


def plugin() -> VisualizerPlugin:
    return VisualizerPlugin(
        plugin_id="industrial_meter",
        title="Industrial Meter",
        qml_component="IndustrialMeterVisualizer",
    )
