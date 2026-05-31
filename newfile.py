# data
gmail = "xyz@gmail.com"
password = '123456'
# code
x = input("please enter your email id:")
y = input("please enter your password:")
while x != gmail or y != password:
    print("Incorrect email or password")
    x = input("please enter your email id:")
    y = input("please enter your password:")
print("Account logged in!")
