# while loop

# i = 1
# while i <= 5:
#     print(' * ' * i)
#     i += 1
# print("Done")

# little game: Guess the number

# secret_number = 9
# guess_count = 0 #shift + f6 to rename
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print("You won!")
#         break
# else:
#     print("Sorry you failed!")

# another game: Simulation Car Game

# command = ""
# started = False # we set this to False because the car is not started yet
#
# while True: #infinite loop
#     command = input(" > ").lower() # the input always be in lower case
#     if command == "start":
#         if started: # if the started = True 2
#             print("Car is already started!") # this message will be printed
#         else:
#             started = True # we set this to True to start de car 1
#             print("The car started!")
#     elif command == "stop":
#         if not started: # started == False
#             print("Car is already stopped!")
#         else:
#             started = False
#             print("Car stopped!")
#     elif command == "help":
#         print("""
# start - to start de car
# stop - to stop de car
# quit - to quit de car
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("Sorry, I don't understand that!")