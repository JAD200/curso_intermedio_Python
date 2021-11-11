def run():
#     squares = []
#     for i in range(1, 101):
#         if i%3 != 0:
#             squares.append(i**2)
    #   This is a list comprehension - for more info: https://bit.ly/3bZiM5U
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    print (squares)
    #   Challenge of the class
    # squares = [i for i in range(1, 10000) if i % 36 == 0]
    # print (squares)


if __name__ == '__main__':
    run()