from pathlib import Path

from app.config.settings import ConfigStore


def test_load_defaults(tmp_path: Path) -> None:
    store = ConfigStore(Path(__file__).resolve().parents[1] / "app" / "config", tmp_path)
    cfg = store.load_defaults()
    assert cfg.audio["chunk_frames"] > 0
    assert cfg.render["visualizer"] == "industrial_meter"
