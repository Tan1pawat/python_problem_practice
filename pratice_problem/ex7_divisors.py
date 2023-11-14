# my_solution

# def divisors(integer):
#     ans =[]
#     for i in range(1,integer):
#         if integer % i == 0:
#             ans.append(i)
#     ans.remove(1)
#     if ans == []:
#         ans = str(integer)+" is prime"
#     return ans

# better solution

def divisors(num):
    l = [a for a in range(2,num) if num%a == 0]
    if len(l) == 0:
        return str(num) + " is prime"
    return l

print(divisors(13))