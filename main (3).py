from enum import Enum

class Days(Enum):
    Mon = 0
    Tue = 1
    Wed = 2
    Thu = 3
    Fri = 4
    Sat = 5
    Sun = 6

def main():
    # Enum assignment
    today = Days.Wed
    print(f"Today is: {today.name}")  # Output: Today is: Wed

    # Enum to integer
    day_value = today.value
    print(f"The numeric value of {today.name} is: {day_value}")  # Output: The numeric value of Wed is: 2

    # Check if an enum value is defined
    is_defined = 3 in Days._value2member_map_
    print(f"Is 3 a valid day in enum? {is_defined}")  # Output: Is 3 a valid day in enum? True

    # Enum to String
    day_string = Days(3).name
    print(f"The day corresponding to 3 is: {day_string}")  # Output: The day corresponding to 3 is: Thu

if __name__ == "__main__":
    main()
