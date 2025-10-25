def main():
    wind_speed = int(input("Enter the windspeed in km/h: "))
    temperature = int(input("Enter the temperature in C: "))
    precipitation = str(input("Is there precipitation (Yes/No): ")).strip().lower()
    
    if precipitation == "yes":
        if wind_speed <= 50 or (wind_speed <= 30 and temperature > 0):
            print("You are not allowed to go outside.")
            return
    else:
        if wind_speed > 80 or not (-25 <= temperature < 37):
            print("You are not allowed to go outside.")
            return
    
    print("You are allowed to go outside.")

main()
