def is_palindrome(string):
    s = string.lower()
    a, b = 0, len(string) - 1
    flag = "YES"
    while a < b:
        while not string[a].isalpha():
            a += 1
        while not string[b].isalpha():
            b -= 1
        if string[a] != string[b]:
            flag = "NO"
            break
        else:
            a += 1
            b -= 1
    return flag
