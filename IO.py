import sys
from os import path

move_file_name = "move_file"
end_file_name = "end_game"


class IO:
    name: str

    def __init__(self, name):
        self.name = name

    def ready(self):
        return path.exists(self.name + ".go")


def read_move():
    min_chars_in_line = 3
    with open(move_file_name, 'r') as move_file:
        for line in move_file.readlines():
            if len(line) > min_chars_in_line:
                line = line.strip()
                name, col, row = line.split(' ')
                print("Move: " + name + " at (" + row + "," + col + ")")


def write_move(move):
    with open(move_file_name, 'w') as move_file:
        move_txt = str(move)
        move_file.write(move_txt)
        move_file.write("\n")
        move_file.flush()


def game_over():
    return path.exists(end_file_name)