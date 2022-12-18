from room import Room, ROOM_TYPE

DEFAULT_ARNONA_RATE = 5

class Apartament:
    def __init__(self, floor: int, number: int, arnona: int = DEFAULT_ARNONA_RATE) -> None:

        self.__floor: int = floor
        self.__number: int = number
        self.__arnona: float = arnona
        self.__rooms: list[Room] = list()

    def get_floor_number(self) -> int:
        return self.__floor

    def get_number(self) -> int:
        return self.__number

    def get_arnona(self) -> float:
        return self.__arnona

    def set_arnona(self, arnona: float) -> bool:
        if arnona <= 0.0:
            return False

        self.__arnona = arnona
        return True

    def get_rooms(self) -> list[Room]:
        return self.__rooms

    def get_rooms_count(self) -> int:
        return len(self.__rooms)

    def add_rooms(self, rooms: list[Room]) -> None:
        for room in rooms:
            self.__rooms.append(room)

    def remove_room(self, room: Room) -> None:
        self.__rooms.remove(room)

    def get_living_area_size(self) -> float:
        result = 0.0

        for room in self.__rooms:
            if room.get_type() == ROOM_TYPE.BALCONY:
                continue

            result += room.get_size()

        return result

    def get_balconies_area_size(self) -> float:
        result = 0.0

        for room in self.__rooms:
            if room.get_type() != ROOM_TYPE.BALCONY:
                continue

            result += room.get_size()

        return result

    def get_arnona_per_month(self) -> float:
        result = 0.0

        for room in self.__rooms:
            if room.get_type() == ROOM_TYPE.BALCONY:
                result += self.__arnona * 0.75 * room.get_size()
            else:
                result += self.__arnona * room.get_size()

        return result