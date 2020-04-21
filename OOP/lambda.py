

def alter(values, check):
    return [val for val in values if check(val)]

def remove_number(value):
    return alter(value,lambda x: x not in [str(n) for n in range(10)])

string = "abc1d234ef5"

print(remove_number(string))
