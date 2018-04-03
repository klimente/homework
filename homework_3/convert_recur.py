"""Convert str in int trough ord function"""


def convert(input_str):
    """A function to convert string in int by using recursion
    return an integer representing of all string

    :param input_str: input string
    :param input_str: str
    :returns: int -- concatenation of a integer representing of input_string

    >>>convert('abc')
    979899
    """
    if input_str:
        if len(input_str) < 2:
            return ord(input_str[0])
        power = 0
        substr = convert(input_str[1:])
        tmp = substr
        while tmp > 0:
            tmp = tmp // 10
            power += 1
        return ord(input_str[0])*(10**power) + substr


if __name__ == "__main__":
    print(convert("abcd"))
    print(convert("hopethat'sbetterthanprevios"))
    print(convert(""))
    print(convert("\t"))
