import re

print("\n ///////////////////// \n")

password = input("Please enter your password: ")


while not re.match('[A-Za-z0-9@#$%^&+=]', password):
    print ("Error! Enter a valid password")
    user_name = input("Please enter your user name: ")

print("Your password is ", password)










print("\n ///////////////////// \n")

email = input("Please enter your email: ")


while not re.match("^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$", email):
    print ("Error! Enter a valid email")
    email = input("Please enter your email: ")

print("Your email is ", email)











print("\n ///////////////////// \n")

url = input("Please enter your url: ")


while not re.findall('www.([\w\-\.]+)', url):
    print ("Error! Enter a valid url")
    url = input("Please enter your url: ")

print("Your url is ", url)








print("\n ///////////////////// \n")

ipv4 = input("Please enter your ipv4: ")


while not re.match("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ipv4):
    print ("Error! Enter a valid ipv4")
    ipv4 = input("Please enter your ipv4: ")

print("Your ipv4 is ", ipv4)








