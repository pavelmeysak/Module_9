import itertools
def all_variants(text: str):
    for i in range(1, len(text)+1):
        for comb in itertools.combinations(text,i):
            formated_comb = ''
            for elem in range(0, len(comb)):
                formated_comb += comb[elem]
            yield formated_comb


a = all_variants('abc')
for i in a:
    print(i)


