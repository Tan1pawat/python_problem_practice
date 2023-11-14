# my_solution

# def printer_error(s):
#     ans = ""
#     word_count=0
#     err_count=0
#     for i in s:
#         if(ord(i)>ord("m") or ord(i)< ord("a")): 
#             err_count+=1
#         word_count+=1
#     ans = str(err_count)+"/"+str(word_count)
#     return ans

# better solution

def printer_error(s):
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))

print(printer_error("aaaaaxmmlf;gk;ofds;mm"))