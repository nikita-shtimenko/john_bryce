class User:
    name: str
    age: int
    data: dict

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.data = dict()

    def get_name(self) -> str:
        return self.name

    def get_age(self) -> int:
        return self.age

    def get_data_str(self) -> str:
        result = f">>> {self.name}: \n"

        for key, val in self.data.items():
            result += f"Date: {key} | Water glasses: {val}\n"

        return result

    def is_date_exists(self, date: str) -> bool:
        if date not in self.data.keys():
            return False

        return True

    def add_date(self, date: str, water_count: int) -> bool:
        if self.is_date_exists(date):
            return False

        self.data.update({date : water_count})
        return True

    def remove_date(self, date: str) -> bool:
        if not self.is_date_exists(date):
            return False

        self.data.pop(date)
        return True