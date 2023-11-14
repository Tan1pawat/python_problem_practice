# my_solution

# def find_even_index(arr):
#     size =len(arr)
#     Left_value = 0
#     Right_value = 0
#     for i in range(size):
#         for r in arr[(i+1):]:
#             Right_value += r
#         print(Right_value,i)            
#         for l in arr[:i]:
#             Left_value +=l
#         if Left_value == Right_value:
#             return i
#         Left_value,Right_value = 0,0
#     return -1

# better solution

def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1

print(find_even_index([20,10,-80,10,10,15,35]))