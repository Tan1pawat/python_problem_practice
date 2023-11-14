# my_solution

# def find_missing_letter(chars):
#     temp = chars[0]
#     for i in chars[1:]:
#         if ord(temp)+1 != ord(i):
#             return chr(ord(i)-1)
#         else:
#             temp = i

# Alternative solution

def find_missing_letter(chars):
    n = 0
    while ord(chars[n]) == ord(chars[n+1]) - 1:
        n += 1
    return chr(1+ord(chars[n]))

print(find_missing_letter(['O','Q','R','S']))