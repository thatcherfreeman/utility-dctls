import numpy as np

# Figures out what luminance norm the gain wheel normalizes to in the primaries panel.
# (spoiler: it's rec709 coefficients).

foo = np.array([
    [0.873890, 1.021421, 1.147617],
    [0.897023, 1.037554, 0.899107],
    [1.215246, 0.927278, 1.038223],
    [1.001595, 0.958062, 1.346834],
    [0.60604599, 1.14880383, 0.64562735],
    [1.48584356, 0.89247183, 0.57840046],
    [1.33161653, 0.83063243, 1.65016344],
    [1.01631355, 0.93194120, 1.56302800],
])

target = np.ones((foo.shape[0], 1))

rec709 = np.array([[0.212639, 0.71517, 0.072192]])
rec709 = np.array([[0.214, 0.716, 0.073]])

result = np.linalg.lstsq(foo, target, rcond=None)[0]
print(result)


print(np.abs((foo) @ result - 1.0))

print(np.abs((foo) @ rec709.T - 1.0))

print(np.mean(np.abs((foo) @ result - 1.0)))
print(np.mean(np.abs((foo) @ rec709.T - 1.0)))