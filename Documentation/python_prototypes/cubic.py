# Quadratic Solver

from sympy import symbols, Eq, solve
import re

d0, b0 = symbols("d0 b0", nonnegative=True)
k = symbols("k", positive=True)
o = symbols("o")

# f(0, k, o, b) = d0
deriv1 = Eq(-2 * ((-1 * o)/k)**3 + 3 * ((-1 * o)/k)**2, d0)
# f(t, k) = 1 # By definition of t = k+o
# deriv1 = Eq(6 * ((t-o)/k)**5 - 15*((t-o)/k)**4 + 10*((t-o)/k)**3, 1)

# g(0, k, o) = b0
poly2 = Eq(k * (- 1 / 2 * ((-1 * o) / k)**4 + ((-1 * o)/k)**3) + (k/2) + o, b0)

solns = solve([poly2, deriv1], [k, o], dict=True)


s = []
for k, v in solns[0].items():
    s.append((str(k), str(v)))

out = open("solns_mod.txt", "w+")
new_s = []
for var, expression in s:
    pattern = r"(x1|x2|x3|d1|d3)\*\*(\d)"
    expression = re.sub(
        pattern, lambda m: f"powi({m.group(1)}, {m.group(2)})", expression
    )
    new_s.append(var)
    new_s.append(expression)

out.writelines("\n".join(new_s))
