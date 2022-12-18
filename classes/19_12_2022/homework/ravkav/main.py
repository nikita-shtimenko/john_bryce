from datetime import date
from ravkav import RavKav

def main():
    # create/init ravkav card
    ride_card = RavKav(1, "JohnBryce")

    # check for invalid/does not exists passed values / default return values
    print("\n---------- Inavlid/Default ----------")
    print(ride_card.get_current_balance())
    print(ride_card.get_rides_count_by_date(date(2022, 12, 15)))
    print(ride_card.get_rides_count_by_type("invalid"))
    print(ride_card.get_rides_count_by_type("short"))
    print(ride_card.get_rides_count_by_type("medium"))
    print(ride_card.get_rides_count_by_type("long"))

    print("\n---------- RavKav ----------")
    # lets top up card
    ride_card.topup(200.0)
    print(ride_card.get_current_balance())

    # short ride
    print(ride_card.ride(13.7, date(2022, 12, 15)))
    print(ride_card.get_current_balance())

    # medium ride
    print(ride_card.ride(34.2, date(2020, 11, 10)))
    print(ride_card.get_current_balance())

    # long ride
    print(ride_card.ride(183.4, date(2017, 6, 5)))
    print(ride_card.get_current_balance())

    # print rides count by date/type
    print(ride_card.get_rides_count_by_date(date(2022, 12, 15)))
    print(ride_card.get_rides_count_by_date(date(2020, 11, 10)))
    print(ride_card.get_rides_count_by_date(date(2017, 6, 5)))
    print(ride_card.get_rides_count_by_type("short"))
    print(ride_card.get_rides_count_by_type("medium"))
    print(ride_card.get_rides_count_by_type("long"))

if __name__ == '__main__':
    main()