#! python 3

# strong password must be at least 8 chars long
# uppercase, lowercase, number and special character

import re, getpass, time, random, sys, string, pyperclip
# ----------------------------psswdCheck-------------------------------


def psswdCheck(psswd):

    regexList = [re.compile(r".{8}"),
    re.compile(r".*[a-z]+.*"),
    re.compile(r".*[A-Z]+.*"),
    re.compile(r".*[0-9]+.*"),
    re.compile(r".*[!@#$%^&*()<>\-+=,.?/\\]+.*")]

    checkList = ["length","lowercase","uppercase","number","special character"]

    for i in range(0, len(regexList)):
        print("checking " + checkList[i])
        dotTime(3)
        varMatch = regexList[i].match(psswd)
        if varMatch:
            print("OK!")
        else:
            print("Error!")

# ----------------------------start-------------------------------


def start():
    print("\nDo you want to do a strong password check or generate a strong password?")
    print("press 1 for check")
    print("press 2 for generate")
    choice = input("(1/2): ")

    if choice == "1":
        print("Type your password:")
        password = getpass.getpass()

        psswdCheck(password)

    elif choice == "2":
        generator()

# ----------------------------dotTime-------------------------------


def dotTime(amount):
    for i in range(0,amount):
        time.sleep(1)
        sys.stdout.write(".")
        sys.stdout.flush()

# ----------------------------generator-------------------------------


def generator():
    lowChars = list(string.ascii_lowercase)
    uppChars = list(string.ascii_uppercase)
    numChars = list(string.digits)
    specChars = list("!@#$%^&*()_-+=<>\|[]?/")

    newPsswdList = []

    for i in range(0,5):
        ranNum = random.randint(0,len(lowChars) - 1)
        newPsswdList.append(lowChars[ranNum])

    newPsswdList.append(uppChars[random.randint(0, len(uppChars) - 1)])
    newPsswdList.append(numChars[random.randint(0, len(numChars) - 1)])
    newPsswdList.append(specChars[random.randint(0, len(specChars) - 1)])

    random.shuffle(newPsswdList)
    newPsswd = ''.join(newPsswdList)
    pyperclip.copy(newPsswd)
    print(f"your new password is copied to the clipboard:\n{newPsswd}")

    print("do you want to generate a new one?")
    while True:
        userInput = input("(y/n): ")

        if userInput == "y" or userInput == "yes":
            generator()
        elif userInput == "n" or userInput == "no":
            break
        else:
            continue

