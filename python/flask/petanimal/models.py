from typing import Tuple, Any

class Pet:
    def __init__(self, det: Tuple[int, str, str, float, str]) -> None:
        self.set_details(det)

    def set_details(self, det: Tuple[int, str, str, float, str]) -> None:
        self.id, self.category, self.breed, self.price, self.owner = det

    def get_details(self) -> Tuple[int, str, str, float, str]:
        return (self.id, self.category, self.breed, self.price, self.owner)

    def get_id(self) -> int:
        return self.id

    def get_category(self) -> str:
        return self.category.capitalize()

    def get_breed(self) -> str:
        return self.breed

    def get_price(self) -> float:
        return self.price

    def get_owner(self) -> str:
        return self.owner