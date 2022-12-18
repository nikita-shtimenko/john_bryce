from house import House
from apartament import Apartament
from room import Room, ROOM_TYPE

def main():
    house = House("Israel", "Tel-Aviv", "Noname street", 1, 10)
    flat = Apartament(10, 20)

    parents_bedroom = Room("Parents bedroom", 40, ROOM_TYPE.BEDROOM)
    parents_bedroom.add_objects(["bed", "closet"])
    parents_bedroom_balcony = Room("Parents bedroom balcony", 15, ROOM_TYPE.BALCONY)
    parents_bedroom_balcony.add_objects(["chair"])
    parents_bathroom = Room("Parents bathroom", 20, ROOM_TYPE.BATHROOM)
    parents_bathroom.add_objects(["bath", "toilet", "sink"])

    kids_bedroom1 = Room("Kids bedroom 1", 20, ROOM_TYPE.BEDROOM)
    kids_bedroom1.add_objects(["bed", "toy1", "toy2"])
    kids_bedroom2 = Room("Kids bedroom 2", 20, ROOM_TYPE.BEDROOM)
    kids_bedroom2.add_objects(["bed", "toy10", "toy20"])
    kids_bathroom = Room("Kids bathroom", 25, ROOM_TYPE.BATHROOM)
    kids_bathroom.add_objects(["shower", "toilet"])

    living_room = Room("Living Room", 50, ROOM_TYPE.LIVING_ROOM)
    living_room.add_objects(["sofa", "tv", "table", "playstation 5"])
    living_room_balcony = Room("Living Room Balcony", 15, ROOM_TYPE.BALCONY)
    living_room_balcony.add_objects(["chair"])

    kitchen = Room("Kitchen", 30, ROOM_TYPE.KITCHEN)
    kitchen.add_objects(["toster", "microvawe", "fridge", "sink"])

    flat.add_rooms([
        parents_bedroom,
        parents_bedroom_balcony,
        parents_bathroom,
        kids_bedroom1,
        kids_bedroom2,
        kids_bathroom,
        living_room,
        living_room_balcony,
        kitchen
    ])

    house_add_app_result = house.add_apartament(flat)
    print(house_add_app_result)

    """
        To change default arnona rate use:
            house.set_arnona(rate)
    """

    print(f"House: {house.get_number()} | {house.get_floors_count()} floors")
    print(f"Flat {flat.get_number()} on {flat.get_floor_number()} floor")
    print(f"    - Rooms: {flat.get_rooms_count()}")
    print(f"    - Living area size: {flat.get_living_area_size()}")
    print(f"    - Balconies area size: {flat.get_balconies_area_size()}")
    print(f"    - Arnona per month: {flat.get_arnona_per_month()}")
    print("\n---------- Rooms ----------")
    
    for room in flat.get_rooms():
        print(f"- {room.get_name()}")
        print(f"    Objects: {room.get_objects()}\n")

if __name__ == '__main__':
    main()