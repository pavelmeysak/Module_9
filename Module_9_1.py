def apply_all_func(int_list, *functions):
    result = {}
    for functions in functions:
        result[functions.__name__] = functions(int_list)
    return result


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))


