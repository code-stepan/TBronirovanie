import json
from pathlib import Path
from typing import Any

from src.infrastructure.repositories.base_repository import BaseRepository


class JSONRepository(BaseRepository):
    def __init__(self, file_path: str) -> None:
        self._path = Path(file_path).resolve()
        self._path.parent.mkdir(parents=True, exist_ok=True)
        if not self._path.exists():
            self._write({})

    def save(self, key: str, data: dict[str, Any]) -> None:
        payload = self._read()
        payload[key] = data
        self._write(payload)

    def load(self, key: str) -> dict[str, Any] | None:
        payload = self._read()
        value = payload.get(key)
        return value if isinstance(value, dict) else None

    def load_all(self) -> list[dict[str, Any]]:
        payload = self._read()
        return [v for v in payload.values() if isinstance(v, dict)]

    def delete(self, key: str) -> None:
        payload = self._read()
        payload.pop(key, None)
        self._write(payload)

    def _read(self) -> dict[str, Any]:
        try:
            with self._path.open("r", encoding="utf-8") as file:
                data = json.load(file)
            return data if isinstance(data, dict) else {}
        except (json.JSONDecodeError, OSError):
            return {}

    def _write(self, payload: dict[str, Any]) -> None:
        temp_path = self._path.with_suffix(f"{self._path.suffix}.tmp")
        with temp_path.open("w", encoding="utf-8") as file:
            json.dump(payload, file, ensure_ascii=False, indent=2)
        temp_path.replace(self._path)