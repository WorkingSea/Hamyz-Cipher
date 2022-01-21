#!/usr/bin/env python3
def Code(message):
    coded_message = ""
    for string in message.lower().split():
        for char in string:
            if char in number_dict:
                coded_message += number_dict[char]
            else:
                coded_message += char
        coded_message += " "
    return coded_message


def Decode(message):
    decoded_message = ""
    reversed_number_dict = {v: k for k, v in number_dict.items()}
    for string in message.split():
        i = 0
        for char in string:
            try:
                int(string[i])
                decoded_message += reversed_number_dict[string[i] + string[i + 1]]
                i += 2
            except ValueError:
                decoded_message += string[i]
                i += 1
            except IndexError:
                pass
        decoded_message += " "
    return decoded_message


number_dict = {
    "a": "10",
    "b": "20",
    "c": "30",
    "d": "40",
    "e": "50",
    "f": "60",
    "g": "70",
    "h": "80",
    "i": "90",
    "j": "01",
    "k": "11",
    "l": "21",
    "m": "31",
    "n": "41",
    "o": "51",
    "p": "61",
    "q": "71",
    "r": "81",
    "s": "91",
    "t": "02",
    "u": "12",
    "v": "22",
    "w": "32",
    "x": "42",
    "y": "52",
    "z": "62",
}


def Main():
    message = input("Type in your message: ")
    choice = input("Do you wish to: \n1-Code\n2-Decode\n")
    if choice != "1" and choice != "2":
        print("You have to type either 1 or 2")
        Main()
    if choice == "1":
        print("Coded message: " + Code(message))
    elif choice == "2":
        print("Decoded message: " + Decode(message))
        print('\n')


while True:
    Main()
