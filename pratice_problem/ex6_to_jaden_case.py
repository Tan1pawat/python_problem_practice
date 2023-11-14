# my_solution
# def to_jaden_case(string):
#     ans = ""
#     key = True
#     for i in string:
#         if key == True:
#             i=i.upper()
#             key = False
#         else:
#             i=i.lower()
#         if i == " ":
#             key = True
#         ans += i
#     return ans

# better solution

def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))