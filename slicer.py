# get user email address

email = input("What is your email address?:").strip()

# slice out user name

user = email[:email.index("@")]     # everything before @

# slice domain name
domain = email[email.index("@")+1:]   # everything after @ but exclude @

# format message
output = "Your username is {} and your domain name is {}".format(user, domain)

# display output 
print(output)
