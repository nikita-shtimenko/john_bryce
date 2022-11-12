import string

VALID_AIRCRAFT_CHAR_SYMBOLS = string.ascii_uppercase + ' '

def main():
    aircraft_chars = getAircraftChars()
    aircraft_seat = getAircraftSeat(aircraft_chars)

    print(f"""
        Row: {aircraft_seat["row"]}
        Char: {aircraft_seat["char"]}
        Place: {aircraft_seat["place"]}
    """)

    return 1

def getAircraftSeat(aircraft_chars: list[dict]) -> dict():
    aircraft_seat = None
    result = None

    while True:
        aircraft_seat = input("Enter seat in aircraft (example: 1A, 35B): ")
        aircraft_seat = aircraft_seat.upper()

        aircraft_seat_len = len(aircraft_seat)

        if aircraft_seat_len not in range(2, 3 + 1):
            print("Error: seat length has to be in range from 2 to 3.")
            continue

        seat_row = aircraft_seat[:aircraft_seat_len - 1]

        if not seat_row.isdigit():
            print("Error: invalid format.")
            continue

        if not 1 <= int(seat_row) <= 99:
            print("Error: seat row can not be lower than 1 or higher than 99.")
            continue

        seat_char = aircraft_seat[aircraft_seat_len - 1:].upper()

        if seat_char not in VALID_AIRCRAFT_CHAR_SYMBOLS:
            print("Error: invalid seat char.")
            continue

        seat_char_place = None

        for char in aircraft_chars:
            if seat_char != char.get("char"):
                continue

            seat_char_place = char.get("place")
            break


        if seat_char_place is None:
            print("Error: char does not exists. Try again.")
            continue

        result = {
            "char": seat_char,
            "row": seat_row,
            "place": seat_char_place
        }

        break

    return result


def getAircraftChars() -> list[dict]:
    aircraft_chars_layout = None
    result = list()

    while True:
        aircraft_chars_layout = input("Enter aircraft chars layout: ")
        aircraft_chars_layout = aircraft_chars_layout.upper()
        
        if len(aircraft_chars_layout) < 3:
            print("Error: aircraft can not contain less than 2 char groups.")
            continue

        if aircraft_chars_layout.isspace():
            print("Error: aircraft chars layout can not be only white-spaces.")
            continue

        if aircraft_chars_layout.count(' ') == 0:
            print("Error: invalid input.")
            continue

        if aircraft_chars_layout.startswith(' '):
            print("Error: aircraft chars layout can not start with white-space.")
            continue

        if aircraft_chars_layout.endswith(' '):
            print("Error: aircraft chars layout can not end with white-space.")
            continue

        result.append({
            "char": aircraft_chars_layout[0],
            "place": "Window"
        })

        is_valid_aircraft_layout = True
        index = 1
        temp_char = None

        while index <= len(aircraft_chars_layout) - 2:
            temp_char = aircraft_chars_layout[index]

            if temp_char not in VALID_AIRCRAFT_CHAR_SYMBOLS:
                is_valid_aircraft_layout = False
                print("Error: invalid aircraft chars layout (allowed symbols: A-Z, white-space).")
                break

            if temp_char.isspace() and aircraft_chars_layout[index + 1].isspace():
                is_valid_aircraft_layout = False
                print("Error: invalid input (two whitespaces in row).")
                break

            if temp_char != ' ':
                if aircraft_chars_layout.count(temp_char) > 1:
                    is_valid_aircraft_layout = False
                    print("Error: char cant repeat itself.")
                    break

                if aircraft_chars_layout[index - 1] != ' ' \
                    and aircraft_chars_layout[index + 1] != ' ':

                    result.append({
                        "char": temp_char,
                        "place": "Middle"
                    })

                elif aircraft_chars_layout[index - 1] == ' ' \
                    or aircraft_chars_layout[index + 1] == ' ':

                    result.append({
                        "char": temp_char,
                        "place": "Aisle"
                    })

            index += 1

        result.append({
            "char": aircraft_chars_layout[len(aircraft_chars_layout) - 1],
            "place": "Window"
        })

        if not is_valid_aircraft_layout:
            continue

        break

    return result

if __name__ == '__main__':
    main()