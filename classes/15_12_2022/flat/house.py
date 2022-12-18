from apartament import Apartament

class House:
    def __init__(self, country: str, city: str, street: str,
        house_number: int, floors_count: int) -> None:
        
        self.__country: str = country
        self.__city: str = city
        self.__street: str = street
        self.__house_number: int = house_number
        self.__floors_count: int = floors_count

        self.__apartaments: list[Apartament] = list()

    def get_number(self) -> int:
        return self.__house_number

    def get_floors_count(self) -> int:
        return self.__floors_count

    def get_apartaments(self) -> list[Apartament]:
        return self.__apartaments

    def get_apartaments_count(self) -> int:
        return len(self.__apartaments)

    def add_apartament(self, apartament: Apartament) -> bool:
        if apartament.get_floor_number() > self.__floors_count:
            return False

        self.__apartaments.append(apartament)
        return True

    def remove_apartament(self, apartament: Apartament) -> bool:
        if apartament not in self.__apartaments:
            return False

        self.__apartaments.remove(apartament)
        return True