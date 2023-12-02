# my_solution

# def in_array(array1, array2):
#     ans= []
#     key = False
#     for i in array1:
#         print(i)
#         for j in array2:
#             if i in j :
#                 key =True
#         if key:
#             ans.append(i)
#             key =False
#     return sorted(list(set(ans)))

# better solution
def in_array(a1, a2):
    return sorted(set(s1 for s1 in a1 if any(s1 in s2 for s2 in a2)))

a1 = ["live", "arp", "strong"] 
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

print(in_array(a1,a2))