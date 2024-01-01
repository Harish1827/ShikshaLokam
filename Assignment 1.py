def print_shortest_substrings(s, x):
    n = len(s)
    result = []

    for i in range(n):
        for j in range(i + x - 1, n):
            if s[i] == s[j]:
                substring = s[i:j + 1]
                result.append(substring)

    if result:
        shortest_length = min(len(substring) for substring in result)
        shortest_substrings = [substring for substring in result if len(substring) == shortest_length]
        print("Answer:", ' '.join(shortest_substrings))
    else:
        print("Answer: not-found")

# Example usage
s = "abccdbacca"

x = 3
print("x =", x)
print_shortest_substrings(s, x)

x = 4
print("\nx =", x)
print_shortest_substrings(s, x)

x = 5
print("\nx =", x)
print_shortest_substrings(s, x)

x = 6
print("\nx =", x)
print_shortest_substrings(s, x)

x = 7
print("\nx =", x)
print_shortest_substrings(s, x)

x = 8
print("\nx =", x)
print_shortest_substrings(s, x)
