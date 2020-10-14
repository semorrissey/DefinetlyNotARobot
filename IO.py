import sys
from os import path
from Board import *

move_file_name = "move_file"
end_file_name = "end_game"


class IO:
    name: str

    def __init__(self, name):
        self.name = name

    def ready(self):
        return path.exists(self.name + ".go")

    def write_move(self, move):
        with open(move_file_name, 'w') as move_file:
            move_file.seek(0)
            move_txt = self.name + " " + str(chr(move.col + 97)) + " " + str(move.row + 1)
            print("My Move: " + move_txt + "\n")
            move_file.write(move_txt)
            move_file.write("\n")
            move_file.flush()


def read_move():
    min_chars_in_line = 5
    name = ""
    col = ""
    row = ""
    with open(move_file_name, 'r') as move_file:
        for line in move_file.readlines():
            if len(line) >= min_chars_in_line:
                line = line.strip()
                name, col, row = line.split(' ')
                print("Their Move: " + name + " at (" + row + "," + col + ")")
                return Location(int(row) - 1, ord(col) - 97)
        print("Me First!!!")
        return -1


def game_over():
    return path.exists(end_file_name)
