import numpy as np

# Figures out what luminance norm the gain wheel normalizes to in the primaries panel.
# (spoiler: it's rec709 coefficients).

foo = np.array([
    [0.728502, 1.166897, 0.143659],
    [1.774562, 0.769122, 0.999615],
    [0.490387, 1.076027, 1.741670],
])

target = np.array([1., 1., 1.])

print(np.linalg.lstsq(foo, target, rcond=None)[0])