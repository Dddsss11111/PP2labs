import os

path = input("Enter the path: ")

if not os.path.exists(path):
    print("The specified path does not exist.")
else:
    print("\nOnly Directories:")
    for name in os.listdir(path):
        if os.path.isdir(os.path.join(path, name)):
            print(name)

    print("\nOnly Files:")
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path, name)):
            print(name)

    print("\nAll Directories and Files:")
    for name in os.listdir(path):
        print(name)