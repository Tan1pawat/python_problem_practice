# my_solution
# def create_phone_number(n):
#     return  '('+ ''.join(str(x) for x in n[0:3]) +') '+ ''.join(str(x) for x in n[3:6])+'-'+''.join(str(x) for x in n[6:])

# better solution

def create_phone_number(n):
	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))