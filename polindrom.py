def isPalindrome(x):
z = numToList(x)
length = math.floor(len(z) / 2)
if length < 2:
    if z[0] == z[-1]:
        return True
    else:
        return False
else:
    if z[0] == z[-1]:
        del z[0]
        del z[-1]
        return isPalindrome(z)
    else:
        return False
