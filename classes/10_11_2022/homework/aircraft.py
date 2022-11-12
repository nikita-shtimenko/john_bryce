import string

CHAR_GROUP_DELIMITER = ' '
VALID_AIRCRAFT_CHAR_SYMBOLS = string.ascii_uppercase

def main():
    chars_layout = getAircraftCharsLayoutFromUser()

    seat = getSeatInAircraftFromUser(chars_layout)
    seat_len = len(seat)

    seat_char = seat[seat_len - 1:]
    seat_row = seat[:seat_len - 1]
    seat_placement = getSeatPlacementInAircraft(chars_layout, seat)

    print(f"""
        Char: {seat_char}
        Row: {seat_row}
        Placement: {seat_placement}
        """)
        
    return 1

def getAircraftCharsLayoutFromUser() -> str:
    chars_layout = None

    while True:
        chars_layout = input("Enter aircraft chars layout: ")
        chars_layout = chars_layout.upper()

        if not isValidCharsLayout(chars_layout):
            continue

        break

    return chars_layout

def isValidCharsLayout(chars_layout: str) -> bool:
    if len(chars_layout) < 3:
        print("Error: chars layout lenght can not be less then 3 symbols.")
        return False

    if chars_layout.isspace():
        print("Error: chars layout can not be only white-spaces.")
        return False

    if chars_layout.count(CHAR_GROUP_DELIMITER) < 1:
        print("Error: there should be at least 2 groups of chars.")
        return False

    if chars_layout.startswith(CHAR_GROUP_DELIMITER):
        print("Error: aircraft chars layout can not start with white-space.")
        return False

    if chars_layout.endswith(CHAR_GROUP_DELIMITER):
        print("Error: aircraft chars layout can not end with white-space.")
        return False

    index = 0
    temp_char = None

    while index <= len(chars_layout) - 1:
        temp_char = chars_layout[index]

        if temp_char == CHAR_GROUP_DELIMITER:
            if chars_layout[index + 1] == CHAR_GROUP_DELIMITER:
                print("Error: invalid input (two whitespaces in row).")
                return False
        else:
            if temp_char not in VALID_AIRCRAFT_CHAR_SYMBOLS:
                print("Error: invalid chars layout (allowed symbols: A-Z, white-space).")
                return False

            if chars_layout.count(temp_char) > 1:
                print("Error: char cant repeat itself.")
                return False

        index += 1

    return True

def getSeatInAircraftFromUser(chars_layout: str) -> str:
    seat = None

    while True:
        seat = input("Enter aircraft seat: ")
        seat = seat.upper()

        if not isValidSeatFormat(seat):
            continue

        if not isSeatExistsInCharsLayout(chars_layout, seat):
            continue

        break

    return seat

def isValidSeatFormat(seat: str) -> bool:
    seat_len = len(seat)

    if seat_len not in range(2, 3 + 1):
        print("Error: seat length has to be in range from 2 to 3.")
        return False

    seat_row = seat[:seat_len - 1]

    if not seat_row.isdigit():
        print("Error: invalid format.")
        return False

    if not 1 <= int(seat_row) <= 99:
        print("Error: seat row can not be lower than 1 or higher than 99.")
        return False

    seat_char = seat[seat_len - 1:]

    if seat_char not in VALID_AIRCRAFT_CHAR_SYMBOLS:
        print("Error: invalid seat char.")
        return False

    return True

def isSeatExistsInCharsLayout(chars_layout: str, seat: str) -> bool:
    seat_char = seat[len(seat) - 1:]
    chars_list = [char for char in chars_layout if char != CHAR_GROUP_DELIMITER]
    
    if seat_char not in chars_list:
        print("Error: entered char does not exists in this aircraft.")
        return False

    return True

def getSeatPlacementInAircraft(chars_layout: str, seat: str) -> str:
    seat_placement = None
    seat_char = seat[len(seat) - 1:]

    index = 0
    temp_char = None

    while index <= len(chars_layout) - 1:
        temp_char = chars_layout[index]

        if seat_char == temp_char:

            if index in [0, len(chars_layout) - 1]:
                seat_placement = "Window"

            else:
                if chars_layout[index - 1] != CHAR_GROUP_DELIMITER \
                    and chars_layout[index + 1] != CHAR_GROUP_DELIMITER:
                    seat_placement = "Middle"
                else:
                    seat_placement = "Aisle"

            break
        
        index += 1
        continue

    return seat_placement

if __name__ == '__main__':
    main()