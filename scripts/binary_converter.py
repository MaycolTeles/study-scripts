
def convert_binary_to_integer(binary_string: str) -> int:
    """
    Function to convert a binary string to an integer.

    Parameters
    -----------
    binary_string : str
        - The binary number in a string format.

    Returns
    --------
    int
        The integer number.
    """
    if binary_string == '0':
        return 0

    if binary_string == '1':
        return 1

    if binary_string[-1] == '0':
        return 2 * convert_binary_to_integer(binary_string[0:-1])

    if binary_string[-1] == '1':
        return 2 * convert_binary_to_integer(binary_string[0:-1]) + 1


def main() -> None:
    """
    Main function. This is where your application starts.
    """
    binary_string = '1001'

    binary_integer = convert_binary_to_integer(binary_string)

    print(binary_integer)


if __name__ == '__main__':
    main()
