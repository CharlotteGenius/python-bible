# print number 1 to 10

i = 1
while i<=10:
    print(i)
    i = i+1

# print even number
j = 1
while j<=50:
    j = j+1
    if j % 2 == 0:
        print(j)
        
        
# print odd number
k = 1
while k<=50:
    if k%2 != 0:
        print(k)
    k = k+1

# add new names to a list

L = []

while len(L)<5:
    new_name = input("Please add a new name:").strip().capitalize()
    L.append(new_name)

print("Sorry list is full.")
print(L)

# as soon as the loop goes false, the loop will stop
