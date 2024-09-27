from time import asctime

if __name__ == "__main__":
    name = input("What is your name: ")
    print("Hello, " + name)
    print("Current time: " + asctime())