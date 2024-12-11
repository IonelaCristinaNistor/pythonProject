# customer = {
#     "name": "John Smith",
#     "age": 30,
#     "is_verified": True
# }
# customer["birthdate"] = "Jan 1 1980"
#
# print(customer["name"])
# print(customer.get("birthdate"))

# ***** exercise *****

# phone = input("Phone: ")
# digits_mapping = {
#     "0": "Zero",
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
#     "5": "Five",
#     "6": "Six",
#     "7": "Seven",
#     "8": "Eight",
#     "9": "Nine"
# }
#
# output = ""
# for character in phone:
#     output += digits_mapping.get(character, "!") + " "
# print(output)

# ***** another exercise ******

# message = input(">")
# words = message.split(' ') # separate the words
# emojis = {
#     ":)": "😊",
#     ":(": "😔"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)