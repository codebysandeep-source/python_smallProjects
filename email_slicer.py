email = input("Enter Your Email: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
# domain_name1 = email[email.index("@") and email.index("."):]

print(f"Your user name is '{username}' and your domain is '{domain_name}'")