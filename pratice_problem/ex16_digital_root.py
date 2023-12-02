# my_solution
# def digital_root(n):
#     ans =0
#     s_n = str(n)
#     l_n = [int(x) for x in s_n ]
#     for i in l_n:
#         i = int(i)
#         ans+=i
#     if len(l_n)>1:
#         return digital_root(ans)
#     else:
#         return ans
    
# better solution
def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))

print(digital_root(942))