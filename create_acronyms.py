user = str(input("Enter the text : ")).split()
text = " "
for i in user:
    text = text + str(i[0].upper())

print(text)

# Example
# Enter the text :  machine learning
# ML
