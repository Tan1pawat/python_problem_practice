# my_solution
# def solution(n):
#     ans = ""
#     pairs = {'I': 1,'IV': 4,'V': 5,'IX': 9,'X': 10,'XL': 40,'L': 50,'XC': 90,'C': 100,'CD': 400,'D': 500,'CM': 900,'M': 1000}
#     pairs = {v: k for k, v in pairs.items()}
#     print(pairs)
#     for i in range(len(str(n))):
#         if i == 0:
#             first_digit = n%10
#             try:
#                 ans = ans + pairs[first_digit]
#             except:
#                 if first_digit >5:
#                     for j in range(first_digit -5):
#                         ans = pairs[1]+ans
#                     ans = pairs[5]+ans
#                 else:
#                     for j in range(first_digit):
#                         ans = pairs[1]+ans
#             n //=10
#         if i == 1:
#             second_digit = n%10
#             try:
#                 ans = pairs[second_digit*10]+ans
#             except:
#                 if second_digit >5:
#                     for j in range(second_digit -5):
#                         ans = pairs[10]+ans
#                     ans = pairs[50]+ans
#                 else:
#                     for j in range(second_digit):
#                         ans = pairs[10]+ans
#             n //=10
#         if i == 2:
#             print(ans)
#             thrid_digit = n%10
#             try:
#                 ans = pairs[thrid_digit*100]+ans
#             except:
#                 if thrid_digit >5:
#                     for j in range(thrid_digit -5):
#                         ans = pairs[100]+ans
#                     ans = pairs[500]+ans
#                 else:
#                     for j in range(thrid_digit):
#                         ans = pairs[100]+ans
#             n //=10
#         if i == 3:
#             print(ans)
#             fourth_digit = n%10
#             try:
#                 ans = pairs[fourth_digit*1000]+ans
#             except:
#                 for j in range(fourth_digit):
#                     ans = pairs[1000]+ans
#             n //=10                
#     return ans

# better solution_1

# units = " I II III IV V VI VII VIII IX".split(" ")
# tens = " X XX XXX XL L LX LXX LXXX XC".split(" ")
# hundreds = " C CC CCC CD D DC DCC DCCC CM".split(" ")
# thousands = " M MM MMM".split(" ")

# def solution(n):
#     return thousands[n//1000] + hundreds[n%1000//100] + tens[n%100//10] + units[n%10]

# better solution_2

def solution(n):
    roman_numerals = {1000:'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
    }
    roman_string = ''
    for key in sorted(roman_numerals.keys(),reverse=True):
        print(key)
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    return roman_string

print(solution(3989))