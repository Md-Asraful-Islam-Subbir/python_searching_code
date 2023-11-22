from sympy import symbols
from sympy.logic.boolalg import truth_table

a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')

expression = input("\n(& = And, | = Or, ~ = Not,>> implies,(p<<q)&(q<<p),(p&~q)|(~p&q) use lowercase alphabets, exp: a | b & ~c)\n \nEnter Expression:")

expression_chars = set([c for c in str(expression) if c.isalpha()])

print("Logical Expression:", expression)



tt = list(truth_table(expression, list(expression_chars)))
is_tautology = all(row[-1] for row in tt)
print("\nTruth Table:")
for row in tt:
    print(row)
