attendees = int(input("Enter number of attendees (0-100):"))
venue = input("large hall,audio system,projector")
#variables / function 
if attendees >= 100:
    if venue == "large hall":
        print("venue")
    
else:
    print("conference room")
    
    
    if venue == "audio system":
        if attendees < 100:
            print("You should try the audio system")
            
            #variable add on
            vegetarian = True
            meal = input("Do you like vegetarian food?(yes or no):")
            
        if vegetarian == True:
            print("Veggie delight cater")
            pass 
        else:
            print("Gournment meal caters")
            
  