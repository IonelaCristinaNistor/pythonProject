# def greet_user(first_name, last_name): #this is a function with 2 parameters
#     print(f'Hi {first_name} {last_name}!')
#     print('Welcome aboard!')
#
# print("Start")
# greet_user("John", "Smith")
# print("Finish")

# def greet_user(first_name, last_name): #this is a function with 2 parameters
#     print(f'Hi {first_name} {last_name}!')
#     print('Welcome aboard!')
#
# print("Start")
# greet_user(first_name="John", last_name="Smith") # keyword arguments
# greet_user("John", last_name="Smith") # order: positional argument > keyword argument
# #calc_cost(total = 50, shipping = 5, discount = 0.1) #example using keyword arguments
# print("Finish")

# ***** return statement ******

# def square(number):
#     return number * number
#
# print(square(4))


# ***** Emoji Converter Function *****

# def emoji_converter(input_message):
#     words = input_message.split(' ')  # separate the words
#     emojis = {
#         ":)": "😊",
#         ":(": "😔"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#
#     return output
#
# message = input(">")
# print(emoji_converter(message))