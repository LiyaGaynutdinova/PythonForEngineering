def sum_digits(string):
    sum = 0
    for char in string:
        if char in '0123456789':
            sum += int(char)
    return sum

if __name__ == '__main__':
    print(sum_digits('Hello World! 1, 2, 3, 4'))