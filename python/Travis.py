known_users = ["Charlotte", "Yeldon", \
                "辉", "小拳拳", \
                "Xiping", "Sophie", \
                "Gale", "Jessie", \
                "Coach", "Co妹",\
                "Uncle", "雪桃"]
print(known_users)
l = len(known_users)
print(l)

for i in range(int(l/2)):
    print(known_users[2*i], "*", known_users[2*i+1])

while True:
        print("Hi! I'm Travis!")
        name = input("What's your name?:").strip().capitalize()

        if name in known_users:
                print("Hello, {}~~!".format(name))
                remove = input("Would you like to be removed from the team (y/n)?:").strip().capitalize()
                if remove == "Y":
                    known_users.remove(name)
                    # remove()  function to remove the term
                    # del known_users[start:end:step]    this is also useful
                    print("{}, wish to see you again!".format(name))
                    print(known_users)
                else:
                    print("Great! We don't want to see you leave either!")
        else:
                print("{}, You little bitch~".format(name))
                add_me = input("Would you like to join(y/n)?").strip().capitalize()
                if  add_me == "Y":
                    known_users.append(name)
                    # append()  add fuction
                    print("Congrats! {}, you're now one of the members!".format(name))
                    print(known_users)
                else:
                    print("It's alright! See you next time!")
