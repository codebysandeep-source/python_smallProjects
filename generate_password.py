import random
length = int(input("Enter the length for Password : "))
string = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()-_=+,<.>/?[{]}"
output = "".join(random.sample(string,length ))
print(output)