# my_solution

# def comp(array1, array2):
#     if array1 is None or array2 is None or array1 == "nil" or array2 == "nil"or array1 == "null" or array2 == "null":
#         return False
#     if len(array1) != len(array2):
#         return False
#     array1 = list(array1)
#     array2 = list(array2)
#     count = 0
#     num_array = 0
#     for i in array1:
#         for j in array2:
#             if (i**2) == j:
#                 array2.pop(num_array)
#                 count+=1
#                 break
#             num_array += 1
#         num_array = 0
#         if count != 0:
#             count = 0
#         else:
#             return False
#     return True

# better solution

def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False

a1 = {19}
a2 = [ 19*19, 19*19]
print(comp(a1, a2))