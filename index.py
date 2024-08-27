import sys

option = sys.argv[1].lower()

if option == "/name":
    print("My name is Jon. I am a senior and will be graduating in Spring 2025")
    input()
    exit()
elif option == "/why":
    print("I have enjoyed computers from a young age. Recently I have really enjoyed building systems and watching them do incredable tasks!")
    input()
    exit()
elif option == "/what":
    print("I actually don't like wirting code and to be quite honest with you, I would much rather do IT \ Networking where I can build and configure systems.")
    input()
    exit()
elif option == "/fact":
    print("The National Weather Service has issued a Required Weekly Test for Otter Tail, MN, all of Minnesota, Becker, MN, Wadena, MN, 27993, and Hubbard, MN beginning at 10:49 AM and ending at 11:04 AM (KFGF/NWS)")
    print("This actaully pertains to a project I wrote with a junior software dev two summers ago.")
    input()
    exit()
else:
    print("A PEBKAC error has occured and the program will now exit. Check your arguements lil bro.")
    exit()