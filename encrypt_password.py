import hashlib

password = "sandeep"

MD5 = (hashlib.md5(password.encode()).hexdigest())
print("MD5 : ",MD5)

db_password = "00dcf16d903e5890aaba465b0b1ba51f"


if (hashlib.md5(password.encode()).hexdigest() == db_password):
   print("Login Successfully!")
else:
   print("Incorrect Password!")
  