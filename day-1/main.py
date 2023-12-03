import sys

text_to_num = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def parse_line_2(line):
    num_list = []
    for c in line:
        if c.isnumeric():
            num_list.append(c)
        else: # c is alpha
            # do something
            pass 
    val = num_list[0] + num_list[-1]
    return val


def parse_line(line):
    num_list = [c for c in line if c.isnumeric()]
    val = num_list[0] + num_list[-1]
    return val


def crack_code(file_path):
    try:
        with open(file_path, 'r') as file:
            total = 0
            line_count = 1
            for line in file:
                print(f"{line_count=}")
                val = parse_line_2(line)
                print(f"{val=}")
                total += int(val)
                print(f"{total=}")
                line_count += 1
    except Exception as e:

        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
    else:
        file_path = sys.argv[1]
        crack_code(file_path)


