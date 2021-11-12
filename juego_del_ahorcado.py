import random
import os

#   Import and read the data
def read_data(filepath="./archivos/data.txt"):
    words = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip().upper())
    return words


def run():
    data = read_data(filepath='./files/data.txt')


if __name__ == '__main__':
    run()