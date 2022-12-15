from usd_converter import USDConverter

def main():
    converter = USDConverter()
    converter.add_rate("ILS", 3.44)
    converter.add_rate("UAH", 36.77)

    print(converter.get_rate("ILS"))
    print(converter.get_rate("UAH"))

    print(converter.exchange(3.44, "ILS")) # convert 3.44 ILS to USD
    print(converter.exchange(36.77, "UAH", False)) # convert 36.77 USD to UAH

    converter.update_rate("ILS", 3)
    converter.update_rate("UAH", 30)

    print(converter.exchange(3, "ILS")) # convert 3.44 ILS to USD
    print(converter.exchange(30, "UAH", False)) # convert 36.77 USD to UAH

    converter.remove_rate("UAH")
    print(converter.exchange(30, "UAH", False))

if __name__ == '__main__':
    main()