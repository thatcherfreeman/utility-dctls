import math
import random

# Python implementation of the binary search methodology used in the Rebind LGGO dctl.

def powf(x, gamma):
    """Safer x^gamma function that works for negative x values."""
    if x < 0:
        return -math.pow(-x, gamma)
    return math.pow(x, gamma)

def powf_prime(base, x):
    """Derivative of powf(base, x) with respect to x."""
    if base == 0:
        return 0
    else:
        return powf(base, x) * math.log(abs(base))

def forwards(x, offset, gamma, gain):
    """The desired function"""
    return powf(gain * x + offset, gamma)

def f(gamma, a, b, c):
    """Error Function"""
    term1 = powf(c, 1.0 / gamma)
    term2 = powf(b, 1.0 / gamma)
    term3 = powf(a, 1.0 / gamma)
    return powf(term1 - term2 + term3, gamma) - b

def f_prime(gamma, a, b, c):
    """Derivative of Error Function"""
    term1 = powf(c, 1.0 / gamma)
    term2 = powf(b, 1.0 / gamma)
    term3 = powf(a, 1.0 / gamma)
    log_term1 = math.log(abs(c)) / (gamma * gamma)
    log_term2 = math.log(abs(b)) / (gamma * gamma)
    log_term3 = math.log(abs(a)) / (gamma * gamma)
    base = term1 - term2 + term3
    exponent = gamma
    derivative_base = base * (log_term1 - log_term2 + log_term3)
    derivative_exponent = math.log(abs(base)) * powf(base, gamma)
    return derivative_base * exponent + derivative_exponent - math.log(abs(b)) * powf(base, gamma)

def newtons_method(initial_guess, a, b, c, tolerance, max_iterations):
    gamma = initial_guess
    for i in range(max_iterations):
        f_val = f(gamma, a, b, c)
        f_prime_val = f_prime(gamma, a, b, c)
        gamma_next = gamma - f_val / f_prime_val
        error = abs(gamma_next - gamma)
        if error > 0.05:
            if gamma_next > gamma:
                gamma_next = gamma + 0.05
            else:
                gamma_next = gamma - 0.05
        print(gamma_next)
        if error < tolerance:
            return gamma_next, i, error
        gamma = gamma_next
    return gamma, i, error

def continuous_binary_search(initial_guess, a, b, c, tolerance, max_iterations, lower_bound=0, upper_bound=5):
    gamma = initial_guess
    # pos_slope = f_prime(gamma, a, b, c) > 0
    pos_slope = f(lower_bound + 0.01, a, b, c) < f(upper_bound, a, b, c)
    # print("gamma, lower_bound, upper_bound: ", gamma, lower_bound, upper_bound)
    # print("pos_slope: ", pos_slope)
    for i in range(max_iterations):
        value = f(gamma, a, b, c)
        error = abs(value)
        if error < tolerance:
            break
        if (pos_slope and value > 0) or (not pos_slope and value < 0):
            upper_bound = gamma
        else:
            lower_bound = gamma
        # print("gamma, lower_bound, upper_bound, value: ", gamma, lower_bound, upper_bound, value)
        gamma = (lower_bound + upper_bound) / 2
    return gamma, i, error

def test(gamma, gain, offset):
    a = forwards(0.0, offset, gamma, gain)
    b = forwards(0.5, offset, gamma, gain)
    c = forwards(1.0, offset, gamma, gain)
    print("a b c: ", a, b, c)
    print("gamma, gain, offset: ", gamma, gain, offset)

    initial_guess = math.log((b - a) / (c - a)) / math.log(0.5)
    # initial_guess = 1.0
    tolerance = 1e-7
    max_iterations = 30
    print("initial_guess: ", initial_guess)

    est_gamma, num_iterations, error = continuous_binary_search(initial_guess, a, b, c, tolerance, max_iterations)
    # gamma, num_iterations, error = newtons_method(initial_guess, a, b, c, tolerance, max_iterations)
    print(f"Estimated gamma: {est_gamma}")
    print(f"number of iterations: {num_iterations}")
    print(f"error: {abs(est_gamma - gamma)}")
    success = (abs(est_gamma - gamma) < 1e-4)
    return success


def main():

    offset = -0.3
    gain = 2.0
    gamma = 0.3

    successes = 0
    failures = 0

    # test(1.0, 0.287046, 0.0)

    for _ in range(100000):
        offset = random.uniform(-0.5, .5)
        gain = random.uniform(0.2, 3)
        gamma = random.uniform(0.1, 4.5)
        try:
            result = test(gamma, gain, offset)
            if result:
                successes += 1
            else:
                failures += 1
        except Exception as e:
            print(f"Error: {e}")
            failures += 1
    print(f"Successes: {successes}")
    print(f"Failures: {failures}")


if __name__ == "__main__":
    main()
