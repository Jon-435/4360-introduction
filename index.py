import sys

try:
    option = sys.argv[1].lower()
except IndexError:
    print("Error: No arguments provided. This is a PEBKAC error. Please provide an option argument like '/name', '/why', '/what', or '/fact'.")
    exit()

if option == "/name":
    print("My name is Jon. I am a senior and will be graduating in Spring 2025")
    input()
    exit()
elif option == "/why":
    print("I have enjoyed computers from a young age. Recently I have really enjoyed building systems and watching them do incredible tasks!")
    input()
    exit()
elif option == "/what":
    print("I actually don't like writing code and to be quite honest with you, I would much rather do IT \ Networking where I can build and configure systems.")
    input()
    exit()
elif option == "/fact":
    print("The National Weather Service has issued a Required Weekly Test for Otter Tail, MN, all of Minnesota, Becker, MN, Wadena, MN, 27993, and Hubbard, MN beginning at 10:49 AM and ending at 11:04 AM (KFGF/NWS)")
    print("This actually pertains to a project I wrote with a junior software dev two summers ago.")
    input()
    exit()
else:
    print("A PEBKAC error has occurred and the program will now exit. Check your arguments.")
    exit()