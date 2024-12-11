
def is_square(n):
    if n < 0:
        return False
    if n == 0:
        return True
    x = 1
    while x * x <= n:
        if n % x == 0 and x * x == n:
            return True
        x += 1
    return False


def fixed_tests():
    def basic_test_cases():
        (is_square(-1), False, "-1: Negative numbers cannot be square numbers")
        (is_square( 0), True, "0 is a square number (0 * 0)")
        (is_square( 3), False, "3 is not a square number")
        (is_square( 4), True, "4 is a square number (2 * 2)")
        (is_square(25), True, "25 is a square number (5 * 5)")
        (is_square(26), False, "26 is not a square number")

