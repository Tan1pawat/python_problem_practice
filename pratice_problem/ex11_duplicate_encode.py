# my_solution

# def duplicate_encode(word):
#     Mem = []
#     ans=""
#     count = 0
#     word_count = 0
#     for i in word:
#         i = i.upper()
#         Mem.append(ord(i))
#     for j in Mem[count:]:
#         for k in Mem:
#             if k == j:
#                 word_count+=1
#         if word_count >1:
#             ans +=")"
#         else:
#             ans+="("
#         count+=1
#         word_count = 0
#     return ans

# Alternative solution

def duplicate_encode(word):
    """a new string where each character in the new string is '(' 
    if that character appears only once in the original word, or ')' 
    if that character appears more than once in the original word. 
    Ignores capitalization when determining if a character is a duplicate. """
    word = word.upper()
    result = ""
    for char in word:
        if word.count(char) > 1:
            result += ")"
        else:
            result += "("
            
    return result

# better solution

def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

print(duplicate_encode("Success"))