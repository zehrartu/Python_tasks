height = int(input("Enter the height of the Christmas tree: "))

for i in range(1, height + 1):
   
    for j in range(height - i):
        print(" ", end="")
    
    for k in range(2 * i - 1):
        print("*", end="")

    print()

for i in range(height // 2):
    for j in range(height - 1):
        print(" ", end="")
    print("|")
