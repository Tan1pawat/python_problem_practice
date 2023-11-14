# my_solution

# def solution(s):
#     ans=""
#     for i in s:
#         if ord(i)>=65 and ord(i)<=90:
#             ans+=" "
#         ans += i
#     return ans

# better solution

def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)

print(solution("helloWorld"))