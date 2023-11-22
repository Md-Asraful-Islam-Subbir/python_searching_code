from itertools import product
variables = ['p', 'q', 'r', 't']
combinations = list(product([True, False], repeat=len(variables)))
def logic_expression(p, q, r,t):
    return (p and q) or (not p and r) and (t or p)
header = '\t\t\t\t\t'.join(variables + [' Expression'])
print(header)
for combo in combinations:
    values = list(combo)
    result = logic_expression(*values)
    row = '\t\t\t\t'.join([str(value) for value in values + [result]])
    print(row)