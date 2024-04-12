def get_hello():
    print("Hello")

def get_bye():
    print("Good Bye")

def print_person(name,age):
    print(f"Name: {name}")
    print(f"Age: {age}")

def get_hi(name):
    return f"Hello {name}"

def main():
    get_hello()
    get_bye()
    print_person(name1, age1)
    print(get_hi("Tom"))

name1 = "Tom"
age1 = 13

main()

