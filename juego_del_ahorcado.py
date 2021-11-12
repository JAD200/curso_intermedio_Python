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
    chosen_word = random.choice(data)# Choise a  random word from data
    chosen_word_list = [letter for letter in chosen_word]
    # Replaces al the words with "_" based on the lenght of the word
    chosen_word_list_underscores = ["_"] * len(chosen_word_list)
    letter_index_dict = {}

    for idx, letter in enumerate(chosen_word):
        if not letter_index_dict.get(letter):
            letter_index_dict[letter] = []
        letter_index_dict[letter].append(idx)
    intentos = 0
    while True:
        os.system("clear") # Si estás en Unix (Mac o Linux) cambia cls por clear
        print("¡Adivina la palabra!")
        for element in chosen_word_list_underscores:
            print(element + " ", end="")
        print("\n")

        letter = input("Ingresa una letra: ").strip().upper()
        assert letter.isalpha(), "Solo puedes ingresar letras"

        if letter in chosen_word_list:
            for idx in letter_index_dict[letter]:
                chosen_word_list_underscores[idx] = letter

        intentos +=1
        if "_" not in chosen_word_list_underscores:
            os.system("clear") # Si estás en Unix (Mac o Linux) cambia cls por clear
            print("\n* * * ¡Ganaste! * * * \nLa palabra era", chosen_word)
            print('Cantidad de intentos: ', intentos)
            break

if __name__ == '__main__':
    run()