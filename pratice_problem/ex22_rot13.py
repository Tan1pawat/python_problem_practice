# my_solution
# def rot13(message):
#     ans= ""
#     for i in message:
#         temp = ord(i)
#         if i.isupper():
#             temp += 13
#             if temp > 90:
#                 temp -= 26
#                 ans+= chr(temp)
#             else: ans+=chr(temp)
#         elif i.islower():
#             temp +=13
#             if temp > 122:
#                 temp -= 26
#                 ans+= chr(temp)
#             else: ans+=chr(temp)
#         else:
#             ans +=i
#     return ans

# better solution
def rot13(message):
    return message.translate(message.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'))

print(rot13('Test !'))