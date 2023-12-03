import sys
import numpy as np


# Part 2: sum of the product of min num of cubes for each game
def get_game_power(cube_list):

    dict = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    
    pairs = [val.strip().split(" ") for val in cube_list]
    for [num, color] in pairs: 
        if int(num) > dict[color]:
            dict[color] = int(num)

    return np.prod(list(dict.values()))

# PART 1: sum of ids of possible games 
def is_possible_game(cube_list):

    dict = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    
    pairs = [val.strip().split(" ") for val in cube_list]
    for [num, color] in pairs: 
        if int(num) > dict[color]:
            return False
    return True


def process(file_path):
    try:
        with open(file_path, 'r') as file:

            part_1_total = 0
            part_2_total = 0
            
            for line in file:
                game_id = int(line.split(":")[0].split(" ")[-1])
                cube_list = line.split(":")[1].strip().replace(";", ",").split(",")
                
                if is_possible_game(cube_list):
                    part_1_total += game_id
                
                game_power = get_game_power(cube_list)
                part_2_total += game_power

            # set which problem to solve
            total = part_2_total
            print(f"FINAL {total=}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path_path>")
    else:
        file_path = sys.argv[1]
        process(file_path)