import sys


def titled_print(title, content, style=6, left="", right=""):
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
            print("\n\n"+left, title, right+"\n")

    print(content)


if __name__ == '__main__':
    titled_print("consolePrint","You just ran the consolePrint file.")
    print("These functions require Python version 3.10 or later.")
    print("Your Python Version:", sys.version.split()[0])