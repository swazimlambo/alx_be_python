positive_integer = int(input("Enter the size of the pattern: "))
size = 0

while size < positive_integer:
    for i in range(positive_integer):
        print("*", end="")
    size = size + 1
    print()
print()