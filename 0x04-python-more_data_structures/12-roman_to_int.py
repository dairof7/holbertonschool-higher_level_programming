def roman_to_int(roman_string):
    if roman_string and type(roman_string) is str:
        suma = 0
        suma += 1 * roman_string.count("I")
        suma += 5 * roman_string.count("V")
        suma += 10 * roman_string.count("X")
        suma += 50 * roman_string.count("L")
        suma += 100 * roman_string.count("C")
        suma += 500 * roman_string.count("D")
        suma += 1000 * roman_string.count("M")

        if "CM" in roman_string:
            suma -= 200
        if "CD" in roman_string:
            suma -= 200
        if "XC" in roman_string:
            suma -= 20
        if "XL" in roman_string:
            suma -= 20
        if "IX" in roman_string:
            suma -= 2
        if "IV" in roman_string:
            suma -= 20
        return suma
    else:
        return 0
