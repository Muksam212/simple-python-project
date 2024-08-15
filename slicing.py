#input -> email -> ram@gmail.com
#output -> username is ram and the domain is gmail
#this is the simply slicing project.

#To understand this program you have to know about how slicing works

email = input("Enter a email: ")

username = email[:email.index("@"):]
domain = email[email.index("@") + 1: email.index("."):]

print(f"Username is {username} and domain is {domain}")