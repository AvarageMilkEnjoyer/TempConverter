import base64

# Encode the string using UTF-8
encoded_string = """
while True:
    try:
        orgTemp = int(input("Enter the temperature: "))
        typeTemp = input("Enter the unit it is in (F, C, K): ")

        if typeTemp == "F" or typeTemp == "f":
            print("Fahrenheit Selected")
            print(orgTemp, "F is equal to: ")

            celcius = (orgTemp - 32) / 1.8 
            print(celcius, "°C")

            kelvin = celcius + 273.15
            print(kelvin, "K")

        elif typeTemp == "C" or typeTemp == "c":
            print("Celsius Selected")
            print(orgTemp, "°C is equal to: ")

            fahrenheit = (orgTemp * 1.8) + 32
            print(fahrenheit, "F")

            kelvin = orgTemp + 273.15
            print(kelvin, "K")

        elif typeTemp == "K" or typeTemp == "k":
            print("Kelvin Selected")
            print(orgTemp, "K is equal to: ")
            celcius3 = orgTemp - 273.15
            print(celcius3, "°C")

            fahrenheit1 = orgTemp - 273.15 * 1.8 + 32
            print(fahrenheit1, "F")

        else:
            print("You didn't give a correct unit")

    except ValueError as e:
        print("Only enter numbers!")
    finally:
        if input("Do you want to convert another temperature? (y/n): ").lower() != "y":
            break
""".encode('utf-8')

# Encode the string using base64
your_code = base64.b64encode(encoded_string)

# Decode and execute the code
exec(base64.b64decode(your_code))
