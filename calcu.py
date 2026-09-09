temp = float(input("Enter the temperature: "))

if temp < 15:
    print("Temperature is cold")
elif 15 <= temp <= 30:
    print("Temprature is Normal")
else: 
    print("Temperature is Hot")