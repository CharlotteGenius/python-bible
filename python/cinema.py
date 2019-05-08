films = {
    "Antman":[3,5],     # 3 is the minimum age that can watch it; 5 is the seats available
    "Baby Boss":[5,6],
    "Fifty Shade":[18,10],
    "Tatinic":[13,7]
    }

while True:
# the code is running over and over gain using while loop

    film = input("What film do you want to watch?:").strip().title()
    if film in films:
    # check if the choice is in the list
        age = int(input("How old are you?:").strip())
        # int() to cast; it's string type without casting
        if age >= films[film][0]:
        # check the age first
            tickets = int(input("How many tickets do you need?:").strip())
            if tickets <= films[film][1]:
            # check if the tickets are available
                print("Enjoy the film!")
                films[film][1] = films[film][1] - tickets
            else:
                print("Sorry we are sold out!")
        else:
            print("Sorry you are not able to watch this film.")    
    else:
        print("We don't have that film...")

