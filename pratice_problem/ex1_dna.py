# my_solution

# def DNA_strand(dna):
#     ans=[]
#     for i in dna:
#         if i == 'A':
#             ans.append('T')
#         if i == 'T':
#             ans.append('A')
#         if i == 'C':
#             ans.append('G')
#         if i == 'G':
#             ans.append('C')
#     return ''.join(ans)

# better solution

pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
    return ''.join([pairs[x] for x in dna])

print(DNA_strand('AAA'))