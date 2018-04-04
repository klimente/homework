"""Convert str in int through 'ord()'"""


def convert(string: str) -> int:
    """A function to convert str in int through multiplying on 10 and addition.
    """
    result = ord(string[0])
    for i in range(1, len(string)):
        number = ord(string[i])
        if number > 100:
            result = result*1000+number
        else:
            result = result*100+number
    return result


print(convert("abadss\ds"))
print(convert("andrey999"))

for i in "andrey999":
    print(ord(i))