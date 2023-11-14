# my_solution

# def row_sum_odd_numbers(n):
#     ans = 0
#     temp = pow(n,2)-(n-1)
#     for i in range(n):
#         ans += temp
#         temp +=2
#     return ans

# better solution

def row_sum_odd_numbers(n):
    if type(n)==int and n>0:
        return n**3 # meaning pow(n,3)
    else:
        return "Input a positive integer"

print(row_sum_odd_numbers(13))