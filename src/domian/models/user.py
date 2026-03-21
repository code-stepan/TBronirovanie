from dataclasses import dataclass


@dataclass(slots=True)
class User:
    first_name: str
    last_name: str
    passport: str | None = None
    address: str | None = None

    def __post_init__(self) -> None:
        self.first_name = self.first_name.strip()
        self.last_name = self.last_name.strip()
        self.passport = self.passport.strip() if self.passport else None
        self.address = self.address.strip() if self.address else None

        if not self.first_name or not self.last_name:
            raise ValueError("First name and last name cannot be empty.")

    @property
    def is_verified(self) -> bool:
        return bool(self.passport)