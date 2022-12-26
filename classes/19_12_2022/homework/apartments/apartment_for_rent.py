from apartment import Apartment, APARTMENT_ESTATE_TYPE, APARTMENT_PARKING_TYPE

class ApartmentForRent(Apartment):
    def __init__(self, address: str, estate_type: APARTMENT_ESTATE_TYPE, floor: int,
        size_in_sq_meters: float, rooms_number: int, balcony: bool,
        monthly_municipal_tax: int, parking_type: APARTMENT_PARKING_TYPE,
        rent_price: int, deal_state: str) -> None:

        super().__init__(address, estate_type, floor, size_in_sq_meters, 
            rooms_number, balcony, monthly_municipal_tax, parking_type)

        self.__rent_price: int = rent_price
        self.__deal_state: str = deal_state