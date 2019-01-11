# range(1,11)
# range() is a function giving a list of 1,2,...,10

#for number in range(1,11):
#    print(number)
# to let the loop runs 10 times.
# the value is changed in sequence in every for loop


#for letter in "abcdef":
#    print(letter)


#for N in range(10,50,2):
#    print(N)
# print the numbers with a step of 2

# in thia case, x is the value stored in the list
#even_numbers = [x for x in range(1,101) if x%2==0]
#print(even_numbers)

# to count the vowels in a letter
vowels = 0           # 元音 state the value as 0 first
consonants = 0       # 辅音

for letter in "Tallahassee":
# letter will run from "T" to the last "e" in sequence
# Try "supercalifragilisticexpialidocious"
    if letter.lower() in "aeiou":
        vowels = vowels + 1
    elif letter == " ":
        pass         # pass the space
    else:
        consonants = consonants + 1

print("There are {} vowels".format(vowels))
print("There are {} consonants".format(consonants))



friends = {
    "male":["Yeldon","Xiping","DickArm"],
    "female":["Gale","Jessie","Charlotte"]
    }

for key in friends.keys():
    for name in friends[key]:
        if "e" in name:
            print(name)
