# my_solution

# def order_weight(strng):
#     string_list = sorted(list(map(str,strng.split())))
#     Mem=[]
#     ans =[]
#     for i in string_list:
#         temp = sum(int(n) for n in str(i))
#         Mem.append((i,temp))
#     temp=list(sorted(Mem,key=lambda w:w[1]))
#     for j,k in temp:
#         ans.append(j)
#     return " ".join(map(str,ans))

# better solution
def order_weight(_str):
    return ' '.join(sorted(sorted(_str.split(' ')), key=lambda x: sum(int(c) for c in x)))

print(order_weight("103 123 4444 99 2000"))