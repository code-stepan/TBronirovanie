from abc import ABC, abstractmethod
from typing import Any


class BaseRepository(ABC):
    @abstractmethod
    def save(self, key: str, data: dict[str, Any]) -> None:
        raise NotImplementedError

    @abstractmethod
    def load(self, key: str) -> dict[str, Any] | None:
        raise NotImplementedError

    @abstractmethod
    def load_all(self) -> list[dict[str, Any]]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, key: str) -> None:
        raise NotImplementedError