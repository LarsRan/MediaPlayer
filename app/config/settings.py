from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class AppConfig:
    root: dict[str, Any]

    @property
    def audio(self) -> dict[str, Any]:
        return self.root["audio"]

    @property
    def render(self) -> dict[str, Any]:
        return self.root["render"]

    @property
    def ui(self) -> dict[str, Any]:
        return self.root["ui"]


class ConfigStore:
    def __init__(self, config_dir: Path, user_dir: Path):
        self._config_dir = config_dir
        self._user_dir = user_dir
        self._user_dir.mkdir(parents=True, exist_ok=True)

    def load_defaults(self) -> AppConfig:
        with (self._config_dir / "defaults.json").open("r", encoding="utf-8") as f:
            root = json.load(f)
        return AppConfig(root)

    def load_shortcuts(self) -> dict[str, str]:
        with (self._config_dir / "shortcuts.json").open("r", encoding="utf-8") as f:
            return json.load(f)

    def load_theme(self) -> dict[str, Any]:
        with (self._config_dir / "theme.json").open("r", encoding="utf-8") as f:
            return json.load(f)

    def load_user_state(self) -> dict[str, Any]:
        state_path = self._user_dir / "state.json"
        if not state_path.exists():
            return {}
        with state_path.open("r", encoding="utf-8") as f:
            return json.load(f)

    def save_user_state(self, state: dict[str, Any]) -> None:
        state_path = self._user_dir / "state.json"
        with state_path.open("w", encoding="utf-8") as f:
            json.dump(state, f, ensure_ascii=False, indent=2)
