# my_solution
def first_non_repeating_letter(s):
    count = 0
    pos = 0
    temp = s.lower()
    for i in temp :
        for j in temp:
            if i == j:
                count += 1
            
        if count == 1:
            return s[pos]
        count = 0
        pos +=1
    return ''

print(first_non_repeating_letter('sTreSS'))