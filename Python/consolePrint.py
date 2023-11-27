import sys


def titled_print(title: str, content: str, style: int = 6, left: str = "", right: str = "") -> None:
    """
    Prints to console the given content with a title that adds new lines
    to make the content more easily identifiable and readable.

    Method requires Python 3.10 or later.

    :param title: String title of the content to be printed
    :param content: String of content to be printed
    :param style: Integer of the style of printout desired
    :param left: String custom left side design of title
    :param right: String custom right side design of title
    :return: None
    """

    match style:
        case 1:
            print("\n\n*****(", title, ")*****\n")
        case 2:
            print("\n\n*****[", title, "]*****\n")
        case 3:
            print("\n\n-----(", title, ")-----\n")
        case 4:
            print("\n\n-----[", title, "]-----\n")
        case 5:
            print("\n\n=====(", title, ")=====\n")
        case 6:
            print("\n\n=====[", title, "]=====\n")
        case _:
            print("\n\n" + left, title, right + "\n")

    print(content)


def grid_print(grid: list[list[str | int | float | bool]], title: str = "Grid", space: bool = True) -> None:
    """
    Prints out a given grid to the console that is a list of lists of strings, integers,
    floats, and/or boolean values.

    ex1. grid_print([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    ex2. grid_print([[True, False], [4.0, 5.0, 6.0], [7, 8, 9], ["Ten"]])

    :param grid: List of Lists of type string, integer, float, and/or boolean
    :param title: String title of the grid output
    :param space: Boolean if the grid output should have 1 line spacing at the top
    :return: None
    """
    if space:
        print()

    print(title)

    for x in range(0, len(grid)):
        output = str(x) + ": "
        for y in range(0, len(grid[x])):
            output += str(grid[x][y])
            if y < (len(grid[x]) - 1):
                output += ", "
        print(output)


if __name__ == '__main__':
    titled_print("consolePrint","You just ran the consolePrint file.")
    print("These functions require Python version 3.10 or later.")
    print("Your Python Version:", sys.version.split()[0])
