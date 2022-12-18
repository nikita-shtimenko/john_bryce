from datetime import date

RIDE_UNLIMITED_LENGTH = float("inf") # infinity
DATE_FORMAT_TYPE = "%d.%m.%Y"

class RavKav:
    def __init__(self, holder_id: int, holder_name: str) -> None:
        self.__holder_id: int = holder_id
        self.__holder_name: str = holder_name
        self.__balance: float = 0.0
        self.__rides_log: dict[str, list[str]] = dict()

        self.__ride_types: dict[str, dict[str, float]] = {
            "short": {
                "min_distance": 0.1,
                "max_distance": 15.0,
                "price": 5.5
            },
            "medium": {
                "min_distance": 15.1,
                "max_distance": 40.0,
                "price": 12.0
            },
            "long": {
                "min_distance": 40.1,
                "max_distance": RIDE_UNLIMITED_LENGTH,
                "price": 23.0
            }
        }

    def get_holder_id(self) -> int:
        return self.__holder_id

    def get_holder_name(self) -> str:
        return self.__holder_name

    def get_current_balance(self) -> float:
        return self.__balance

    def topup(self, amout: float) -> bool:
        if amout <= 0.0:
            return False
        
        self.__balance += amout
        return True

    def ride(self, ride_distance: float, ride_date: date) -> tuple[bool, str]:
        if ride_distance <= 0.0:
            return False, "Invalid distance: <= 0.0"

        for ride_type in self.__ride_types.keys():
            min_distance = self.__ride_types[ride_type]["min_distance"]
            max_distance = self.__ride_types[ride_type]["max_distance"]

            if not min_distance <= ride_distance <= max_distance:
                continue

            ride_price = self.__ride_types[ride_type]["price"]

            if self.__balance < ride_price:
                return False, "Not enough money for ride"

            self.__balance -= ride_price

            ride_date_str = ride_date.strftime(DATE_FORMAT_TYPE)

            if ride_date not in self.__rides_log.keys():
                self.__rides_log[ride_date_str] = list()

            self.__rides_log[ride_date_str].append(ride_type)
            break

        return True, "Valid ride, added to rides log"

    def get_rides_count_by_date(self, ride_date: date) -> tuple[bool, int, str]:
        ride_date_str = ride_date.strftime(DATE_FORMAT_TYPE)

        if ride_date_str not in self.__rides_log.keys():
            return False, 0, "There are no rides for passed date"

        return True, len(self.__rides_log[ride_date_str]), "Valid date, rides count returned"
            

    def get_rides_count_by_type(self, ride_type: str) -> tuple[bool, int, str]:
        ride_type = ride_type.lower()

        if ride_type not in self.__ride_types.keys():
            return False, 0, "Passed ride type does not exists"

        count = 0

        for ride_date in self.__rides_log.keys():
            count += self.__rides_log[ride_date].count(ride_type)

        return True, count, "Valid ride type, count of rides returned"