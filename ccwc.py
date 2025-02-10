import sys

ERROR_MESSAGES = {
    "arguments": "Please Enter the command and file name",
    "command": "Please enter the Correct command '-c','-l','-w','-m'",
}

INPUT_COMMANDS = ["-c", "-l", "-w", "-m"]


def check_arguments():
    if len(sys.argv) > 3:
        raise Exception(ERROR_MESSAGES["arguments"])


def check_command():
    if sys.argv[1] not in INPUT_COMMANDS:
        raise Exception(ERROR_MESSAGES["command"])


def read_bytes(file_name: str):
    file = open(file_name, "rb")
    return len(file.read())


def read_line(file):
    with open(file, "rb") as f:
        lines = [line.rstrip() for line in f]

    return len(lines)


def read_word(file):
    data = open(file, "rb").read()
    return len(data.split())


def read_character(file):
    data = open(file, "rb").read()
    return len(data)


def main():
    check_arguments()

    if len(sys.argv) == 2:
        file_name = sys.argv[1]
        print(
            "\t",
            read_line(file_name),
            read_word(file_name),
            read_character(file_name),
            file_name,
        )
    else:
        check_command()
        file_name = sys.argv[2]
        command = sys.argv[1]
        res = 0
        if command == "-c":
            res = read_bytes(file_name)
        elif command == "-l":
            res = read_line(file_name)
        elif command == "-w":
            res = read_word(file_name)
        elif command == "-m":
            res = read_character(file_name)

        print(res, file_name)


main()
