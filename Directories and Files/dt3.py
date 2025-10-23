import os

path = input("Enter the path: ")

if os.path.exists(path):
    print("\nThe specified path exists!")

    directory = os.path.dirname(path)

    filename = os.path.basename(path)

    print("Directory portion:", directory)
    print("File name portion:", filename)
else:
    print("\nThe specified path does NOT exist.")