weather = input("Enter the weather. (sunny,rainy,cold):")
clothing = input("sunglasses, hats,boots, sweater? ")

if weather == "sunny":
    print("Wear sunglasses")
elif weather == "rainy":
    print("Wear boots")
    
else:
    print("Take umbrella")
    
    if weather == "cold":
        print("Wear Hat")
    elif clothing == "sunglasses":
        print("Sunscreen")
        
    else:
        print("sweater")