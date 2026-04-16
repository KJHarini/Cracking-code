import string

def print_rangoli(size):
    alpha = string.ascii_lowercase
    lines = []
    for i in range(size):
        s = "-".join(alpha[i:size][::-1] + alpha[i+1:size])
        lines.append(s.center(4 * size - 3, "-"))
    print('\n'.join(lines[::-1] + lines[1:]))