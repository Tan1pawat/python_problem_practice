# my_solution

# def odd_or_even(arr):
#     sumofarr = sum(arr)
#     if sumofarr%2 ==0:
#         return "even"
#     else:
#         return "odd"

# better solution

def odd_or_even(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'

print(odd_or_even([0, 1, 2]))