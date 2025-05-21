#!/usr/bin/env python3
"""
decrypt_flags.py

Prompt for a UID, then decrypt and display the corresponding flag
using the ft_des algorithm, matching the original C logic.
"""

def ft_des(param: str) -> str:
    """
    Reimplementation of the C `ft_des` logic in Python.
    """
    arr = list(param)
    idx = 0       # position in string
    cycle = 0     # index into digits
    digits = "0123456"

    while idx < len(arr):
        if cycle == 6:
            cycle = 0

        count = ord(digits[cycle])

        if (idx & 1) == 0:
            # Even index: shift backwards
            for _ in range(count):
                arr[idx] = chr(ord(arr[idx]) - 1)
                if arr[idx] == chr(0x1F):
                    arr[idx] = '~'
        else:
            # Odd index: shift forwards
            for _ in range(count):
                arr[idx] = chr(ord(arr[idx]) + 1)
                if arr[idx] == chr(0x7F):
                    arr[idx] = ' '

        idx += 1
        cycle += 1

    return "".join(arr)


def main():
    try:
        raw = input("Enter your UID (decimal or 0xHEX): ").strip()
        uid = int(raw, 0) + 1000
    except ValueError:
        print("Invalid UID format. Please enter a decimal or hex number (e.g. 3000 or 0xBB8).")
        return

    if uid == 0xBBE:
        print(ft_des("H8B8h_20B4J43><8>\\ED<;j@3"))
    elif uid < 0xBBF:
        if uid == 0xBBA:
            print(ft_des("<>B16\\AD<C6,G_<1>^7ci>l4B"))
        elif uid < 0xBBB:
            if uid == 3000:
                print(ft_des("I`fA>_88eEd:=`85h0D8HE>,D"))
            elif uid < 0xBB9:
                if uid == 0:
                    print("You are root are you that dumb ?")
                else:
                    print("Nope there is no token here for you sorry. Try again :)")
            else:
                print(ft_des("7`4Ci4=^d=J,?>i;6,7d416,7"))
        elif uid == 0xBBC:
            print(ft_des("?4d@:,C>8C60G>8:h:Gb4?l,A"))
        elif uid < 0xBBD:
            print(ft_des("B8b:6,3fj7:,;bh>D@>8i:6@D"))
        else:
            print(ft_des("G8H.6,=4k5J0<cd/D@>>B:>:4"))
    elif uid == 0xBC2:
        print(ft_des("74H9D^3ed7k05445J0E4e;Da4"))
    elif uid < 0xBC3:
        if uid == 0xBC0:
            print(ft_des("bci`mC{)jxkn<\"uD~6%g7FK`7"))
        elif uid < 0xBC1:
            print(ft_des("78H:J4<4<9i_I4k0J^5>B1j`9"))
        else:
            print(ft_des("Dc6m~;}f8Cj#xFkel;#&ycfbK"))
    elif uid == 0xBC4:
        print(ft_des("8_Dw\"4#?+3i]q&;p6 gtw88EC"))
    elif uid < 0xBC4:
        print(ft_des("70hCi,E44Df[A4B/J@3f<=:`D"))
    elif uid == 0xBC5:
        print(ft_des("boe]!ai0FB@.:|L6l@A?>qJ}I"))
    elif uid == 0xBC6:
        print(ft_des("g <t61:|4_|!@IF.-62FH&G~DCK/Ekrvvdwz?v|"))
    else:
        print("Nope there is no token here for you sorry. Try again :)")

if __name__ == "__main__":
    main()
