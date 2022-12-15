from enum import IntEnum, auto

class Action(IntEnum):
    VEHICLES_LIST = 0
    VEHICLES_ADD = auto()

ACTIONS = (
    "Vehicles list",
    "Add new vehicle to list"
)

VEHICLE_TYPE_MODELS = {
    "Private": (
        "S-30", 
        "S-40", 
        "S-60", 
        "S-80", 
        "S-90"
    ),
    "Semi-truck": (
        "VNL-760", 
        "VNL-860", 
        "VNR-300", 
        "VNR-600", 
        "VHD-500", 
        "VHD-900"
    )
}

VEHICLE_ENGINE_TYPES = (
    "Diesel",
    "Patrol",
    "Electric",
    "Hydrogen"
)

VEHICLE_COLORS = (
    "Orange",
    "Green",
    "Violet",
    "Red-Orange",
    "Yellow-Orange",
    "Yellow-Green",
    "Blue-Green",
    "Blue-Violet",
    "Red-Violet"
)

vehicles = {
    "VOLVO S-30 (Private)": {
        "vehicle_type": "Private",
        "production_year": 2002,
        "model": "S-30",
        "engine_type": "Diesel",
        "color": "Orange"
    }
}

def main():
    while True:
        print("\n")
        print(">>> Welcome to VOLVO vehicles list.")
        print("> Avaliable actions (enter '@' to exit): \n")

        for i, action in enumerate(ACTIONS):
            print(f"{i + 1}. {action}")

        action = input("> Enter action number: ")

        if action == '@':
            print("\nOK: Exit programm...")
            break

        if not action.isdigit():
            print("\nError: invalid input: you have to insert a number.")
            continue

        action = int(action) - 1

        if action not in range(0, len(ACTIONS)):
            print("\nError: invalid input: action does not exists.")
            continue

        vehicleCallAction(action)

    return 1

def vehicleCallAction(action: int):
    match action:
        case Action.VEHICLES_LIST:
            printVehiclesCatalog()

        case Action.VEHICLES_ADD:
            updateVehiclesCatalog(vehicles)
            printVehiclesCatalog()

def printVehiclesCatalog():
    print("\n>>> VOLVO vehicles catalog: ")

    for i, vehicle_name in enumerate(vehicles.keys()):
        print(f"{i + 1}. {vehicle_name}")

def updateVehiclesCatalog(catalog: dict) -> bool:
    vehicle_type = getVehicleTypeFromUser()
    vehicle_model = getVehicleModelFromUser(vehicle_type)

    vehicle_id = f"VOLVO {vehicle_model} ({vehicle_type})"

    if vehicle_id in vehicles.keys():
        print("Error: vehicle like this already exists in catalog.")
        return False

    vehicle_production_year = getVehicleProductionYearFromUser()
    vehicle_engine_type = getVehicleEngingeTypeFromUser()
    vehicle_color = getVehicleColorFromUser()

    vehicles.update(
        {
            vehicle_id: {
                "type": vehicle_type,
                "model": vehicle_model,
                "production_year": vehicle_production_year,
                "engine": vehicle_engine_type,
                "color": vehicle_color
            }
        }
    )

    return True

def getVehicleTypeFromUser() -> str:
    result = None
    vehicle_types = tuple(key for key in VEHICLE_TYPE_MODELS.keys())
    print(vehicle_types)

    while True:
        """ Vehicle type input """

        print("\n>>> Add new vehicle to catalog.")
        print("> Vehicle types: ")

        for i, vehicle_type in enumerate(vehicle_types):
            print(f"{i + 1}. {vehicle_type}")

        try:
            result = int(input("\n> Enter vehicle type: "))
        except ValueError:
            print("\nError: invalid input: you have to insert a number.")
            continue

        result -= 1

        if result not in range(0, len(vehicle_types)):
            print("\nError: invalid input: vehicle type does not exists.")
            continue

        break

    return vehicle_types[result]

def getVehicleModelFromUser(user_vehicle_type: str) -> str:
    result = None
    vehicle_models = VEHICLE_TYPE_MODELS[user_vehicle_type]

    while True:
        """ Vehicle model input """
        print(f"> {user_vehicle_type} vehicle models:")

        for i, vehicle_model in enumerate(vehicle_models):
            print(f"{i + 1}. {vehicle_model}")

        try:
            result = int(input("\n> Enter vehicel model number: "))
        except ValueError:
            print("\nError: invalid input: you have to insert a number.")
            continue

        result -= 1

        if result not in range(0, len(vehicle_models)):
            print("\nError: invalid input: vehicle model does not exists.")
            continue

        break

    return vehicle_models[result]

def getVehicleEngingeTypeFromUser() -> str:
    result = None

    while True:
        print(">>> Vehicle engine types: ")

        for i, engine in enumerate(VEHICLE_ENGINE_TYPES):
            print(f"{i + 1}. {engine}")

        try:
            result = int(input("\n> Enter vehicle engine type number: "))
        except ValueError:
            print("\nError: invalid input: you have to insert a number.")
            continue

        result -= 1

        if result not in range(0, len(VEHICLE_ENGINE_TYPES)):
            print("\nError: invalid input: vehicle engine type does not exists.")
            continue

        break

    return VEHICLE_ENGINE_TYPES[result]

def getVehicleProductionYearFromUser() -> int:
    result = None

    while True:
        """ Production year input """
        try:
            result = int(input("\n> Enter year of production: "))
        except ValueError:
            print("\nError: invalid input: you have to insert a number.")
            continue

        break

    return result

def getVehicleColorFromUser() -> str:
    result = None

    while True:
        print(">>> Vehicle colors: ")

        for i, color in enumerate(VEHICLE_COLORS):
            print(f"{i + 1}. {color}")

        try:
            result = int(input("\n> Enter vehicle color number: "))
        except ValueError:
            print("\nError: invalid input: you have to insert a number.")
            continue

        result -= 1

        if result not in range(0, len(VEHICLE_COLORS)):
            print("\nError: invalid input: vehicle engine type does not exists.")
            continue

        break

    return VEHICLE_COLORS[result]

if __name__ == '__main__':
    main()