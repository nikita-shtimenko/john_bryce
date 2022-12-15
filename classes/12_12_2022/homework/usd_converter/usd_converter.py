class USDConverter:
    def __init__(self) -> None:
        self.__currency_rate: dict[str, float] = dict()

    def add_rate(self, currency: str, rate: float) -> bool:
        if len(currency) < 2:
            return False

        if rate <= 0.0:
            return False

        self.__currency_rate[currency] = rate
        return True

    def remove_rate(self, currency: str) -> bool:
        if not self.__is_currency_rate_exists(currency):
            return False

        self.__currency_rate.pop(currency)
        return True

    def update_rate(self, currency: str, rate: float) -> bool:
        if not self.__is_currency_rate_exists(currency):
            return False

        self.__currency_rate[currency] = rate
        return True

    def __is_currency_rate_exists(self, currency: str) -> bool:
        if currency not in self.__currency_rate.keys():
            return False

        return True

    def get_rate(self, rate: str) -> float:
        if not self.__is_currency_rate_exists(rate):
            return 0.0

        return self.__currency_rate[rate]

    def exchange(self, value: float, currency: str, to_usd: bool = True) -> tuple[bool, float]:
        if value <= 0.0:
            return False, 0.0

        if not self.__is_currency_rate_exists(currency):
            return False, 0.0

        if not to_usd:
            return True, value * self.__currency_rate[currency]

        return True, value / self.__currency_rate[currency]