from src.domian.models.user import User


class UserBuilder:
    def __init__(self) -> None:
        self._first_name: str | None = None
        self._last_name: str | None = None
        self._passport: str | None = None
        self._address: str | None = None

    def set_name(self, first_name: str, last_name: str) -> "UserBuilder":
        self._first_name = first_name.strip()
        self._last_name = last_name.strip()
        return self

    def set_passport(self, passport: str) -> "UserBuilder":
        self._passport = passport.strip()
        return self

    def set_address(self, address: str) -> "UserBuilder":
        self._address = address.strip()
        return self

    def set_adress(self, address: str) -> "UserBuilder":
        return self.set_address(address)

    def build(self) -> User:
        if not self._first_name or not self._last_name:
            raise ValueError("First name and last name are required for User.")
        return User(
            first_name=self._first_name,
            last_name=self._last_name,
            passport=self._passport,
            address=self._address,
        )