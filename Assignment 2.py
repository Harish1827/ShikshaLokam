def transform_string(s):
    ascii_values = [ord(char) for char in s]
    changed_chars = set()

    for i in range(len(ascii_values)):
        if i not in changed_chars:
            if ascii_values[i] % 2 == 0:
                if i < len(ascii_values) - 1:
                    ascii_values[i + 1] += ascii_values[i] % 7
                    changed_chars.add(i + 1)
            else:
                if i > 0:
                    ascii_values[i - 1] -= ascii_values[i] % 5
                    changed_chars.add(i - 1)

            if ascii_values[i] < 0 or ascii_values[i] > 127:
                ascii_values[i] = 83

    transformed_string = ''.join([chr(ascii_value) for ascii_value in ascii_values])
    return transformed_string

# Example usage
s = input()
result = transform_string(s)
print("Final Answer:", result)
