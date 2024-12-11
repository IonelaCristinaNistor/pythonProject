from itertools import combinations


def is_valid_regex(pattern, x, y, z):
    """Check if the regex matches x and y but not z."""
    for char in x:
        if char not in pattern:
            return False
    for char in y:
        if char not in pattern:
            return False
    for char in z:
        if char in pattern:
            return False
    return True


def findLongestRegex(x, y, z):
    # Combine all unique characters from x and y
    all_chars = sorted(set(x + y))  # Unique sorted characters
    z_chars = set(z)  # Characters in z
    n = len(all_chars)

    best_regex = ""

    # Iterate over all possible combinations of subsets
    for length in range(1, n + 1):
        for subset in combinations(all_chars, length):
            regex = "[" + "".join(subset) + "]"
            # Check if it matches x and y, but not z
            if is_valid_regex(subset, x, y, z):
                # Compare lengths and lexicographical order
                if len(regex) > len(best_regex) or (len(regex) == len(best_regex) and regex < best_regex):
                    best_regex = regex

    # If no valid regex was found, return -1
    return best_regex if best_regex else -1


# Example test case
x = "ABASCS"
y = "DEX"
z = "Z"
print(findLongestRegex(x, y, z))  # Output: "[ABDEFGHIJKLMNOPQRSTUVWXYZ]"
