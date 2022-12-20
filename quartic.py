# Quartic Solver

from sympy import symbols, Eq, solve
import re

x1, y1, x2, y2, x3, y3 = symbols('x1 y1 x2 y2 x3 y3')
a1, a2, a3, a4, a5 = symbols('a1 a2 a3 a4 a5')
d1, d3 = symbols('d1 d3')


poly1 = Eq(a1 * (x1**4) + a2 * (x1**3) + a3 * (x1**2) + a4 * x1 + a5, y1)
poly2 = Eq(a1 * (x2**4) + a2 * (x2**3) + a3 * (x2**2) + a4 * x2 + a5, y2)
poly3 = Eq(a1 * (x3**4) + a2 * (x3**3) + a3 * (x3**2) + a4 * x3 + a5, y3)

deriv1 = Eq(4 * a1 * (x1**3) + 3 * a2 * (x1**2) + 2 * a3 * x1 + a4, d1)
deriv3 = Eq(4 * a1 * (x3**3) + 3 * a2 * (x3**2) + 2 * a3 * x3 + a4, d3)

solns = solve([poly1, poly2, poly3, deriv1, deriv3], [a1, a2, a3, a4, a5], dict=True)


s = []
for k,v in solns[0].items():
    s.append((str(k), str(v)))

out = open('solns_mod.txt', 'w+')
new_s = []
for var, expression in s:
    pattern = r'(x1|x2|x3|d1|d3)\*\*(\d)'
    expression = re.sub(pattern, lambda m: f"powi({m.group(1)}, {m.group(2)})", expression)
    new_s.append(var)
    new_s.append(expression)

out.writelines('\n'.join(new_s))