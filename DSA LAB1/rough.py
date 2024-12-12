def PalindromRecursive(str):
    if len(str) == 0 or len(str) == 1:
        return "palindrome"
    if str[0] == str[-1]:
        return PalindromRecursive(str[1:-1])
    else:
        return False

print(PalindromRecursive("raaar"))