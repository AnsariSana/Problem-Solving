# Enter your code here. Read input from STDIN. Print output to STDOUT
def findContact(phoneBook):
    while True:
        name = input()
        if name == "":
            break
        if phoneBook.get(name):
            print(name+"="+phoneBook.get(name))
        else:
            print("Not found")

if __name__ == "__main__":
    n = int(input())
    phoneBook = dict()
    for i in range(n):
        contact = input().strip().split(" ")
        phoneBook[contact[0]] = contact[1]
    findContact(phoneBook)
