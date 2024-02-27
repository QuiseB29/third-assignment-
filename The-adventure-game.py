place = input("Choose a place, (forest or cave?):")
action = input("climb a tree or cross a river?")

if place == "forest": 
 if action == "climb a tree":
    print("you found a bird nest")

elif place == "cave":
    print("you find a hidden treasure")
    
else:
     print("you found a boat")
     
action2 = input("light a torch or proceed in the dark?")

if place == "cave":
 if action2 == "light a torch":
     print("Lets Regroup")
     pass
 if action2 == "proceed in the dark" and place == "cave":
     print("onwards")