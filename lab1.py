import argparse
import re


def parsers() -> str:
    """
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, help='name of the file')
    args = parser.parse_args()
    return args.file


def file_read(file: str):
    """
    :return:
    """
    with open(file, "r") as file:
        text = file.read()
    return text


def finding_mans(text: str) -> int:
    """
    :return:
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
