from enum import Enum, auto

class APARTMENT_ESTATE_TYPE(Enum):
    FLAT = 0,
    PENTHOUSE = auto(),
    VILLA = auto()

__APARTMENT_ESTATE_TYPE_NAME = (
    "Flat",
    "Penthouse",
    "Villa"
)

class APARTMENT_PARKING_TYPE(Enum):
    NO_PARKING = 0,
    STREET = auto(),
    UNDERGROUND = auto(),
    GARAGE = auto()

__APARTMENT_PARKING_TYPE_NAME = (
    "No parking",
    "Parking on street",
    "Underground parking",
    "Garage parking"
)

class APARTMENT_DEAL_TYPE(Enum):
    RENT = 0,
    SALE = auto()

__APARTMENT_DEAL_TYPE_NAME = (
    "Rent",
    "Sale"
)

class Apartment:
    def __init__(self, address: str, estate_type: APARTMENT_ESTATE_TYPE, floor: int,
        size_in_sq_meters: float, rooms_number: int, balcony: bool,
        monthly_municipal_tax: int, parking_type: APARTMENT_PARKING_TYPE,
        deal_type: int) -> None:

        self.__address: str = address
        self.__estate_type: APARTMENT_ESTATE_TYPE = estate_type
        self.__floor: int = floor
        self.__size_in_sq_meters: float = size_in_sq_meters
        self.__rooms_number: int = rooms_number
        self.__balcony: bool = balcony
        self.__monthly_municipal_tax: int = monthly_municipal_tax
        self.__parking_type: APARTMENT_PARKING_TYPE = parking_type
