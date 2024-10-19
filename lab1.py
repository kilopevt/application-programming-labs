import argparse
import re


def parsers() -> str:
    """
    Parse command arguments

    :return: file
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, help='name of the file')
    args = parser.parse_args()
    return args.file


def file_read(file: str):
    """
    Function for opening and reading files

    :return: text
    """
    with open(file, "r", encoding="utf-8") as file:
        text = file.read()
    return text


def finding_mans(text: str) -> int:
    """
    Finding the count of profiles with te pattern "Мужской"

    :return: count of mens
    """
    pattern = r'Мужской'
    count = re.findall(pattern, text)
    return len(count)


def main():
    file = parsers()
    try:
        file_open = file_read(file)
        print("The count of mens:", finding_mans(file_open))
    except FileNotFoundError:
        print("File is not found")


if __name__ == '__main__':
    main()
