from enum import Enum, auto

class ROOM_TYPE(Enum):
    BEDROOM = 1,
    LIVING_ROOM = auto(),
    BATHROOM = auto(),
    KITCHEN = auto(),
    BALCONY = auto(),
    OTHER = auto()

class Room:
    def __init__(self, room_name: str, room_size_sq: float, 
        room_type: ROOM_TYPE) -> None:
        
        self.__name: str = room_name
        self.__size_sq: float = room_size_sq
        self.__type: ROOM_TYPE = room_type
        self.__objects: list[str] = list()

    def get_name(self) -> str:
        return self.__name

    def get_size(self) -> float:
        return self.__size_sq

    def get_type(self) -> ROOM_TYPE:
        return self.__type

    def get_objects(self) -> list[str]:
        return self.__objects

    def __is_object_exists(self, object_name: str) -> bool:
        if object_name not in self.__objects:
            return False

        return True

    def add_objects(self, object_names: list[str]) -> tuple[bool, str, list[str]]:
        if not len(object_names):
            return False, "Error: empty objets list", [""]

        invalid_objects: list[str] = list()
        invalid_objects_count = 0

        for obj_name in object_names:
            if self.__is_object_exists(obj_name):
                invalid_objects.append(obj_name)
                invalid_objects_count += 1
                continue

            self.__objects.append(obj_name)

        if not invalid_objects:
            result_message = "Objects added. No invalid objects."
        else:
            result_message = f"Object added. Invalid objects: {len(invalid_objects)}"

        return True, result_message, invalid_objects

    def remove_object(self, object_name: str) -> bool:
        if not self.__is_object_exists(object_name):
            return False

        self.__objects.remove(object_name)
        return True