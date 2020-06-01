
def print_table(table):

    # establish a list of integers equal to the length of the longest
    # string in each sub-list. (Each sub-list will be a column)
    col_widths = []
    for i in range(len(table)):
        col_widths.append(len(max(table[i], key=len)))

    # print each row
    for y in range(len(table[0])):
        for x in range(len(table)):
            print(table[x][y].rjust(col_widths[x]+2), end='')
        print()


def main():

    print("This program will display a 2D list in a nice \nand pretty series of right-justified columns")
    print()
    print("It will work as long as the quantity of items \nin each sub-list is equal")
    print()
    print()
    
    table_data = [['apples', 'oranges', 'cherries', 'banana', 'kiwi', 'blueberry'],
                  ['Alice', 'Bob', 'Carol', 'David', 'Luke', 'Laura'],
                  ['dogs', 'cats', 'moose', 'goose', 'bears', 'fish'],
                  ['green', 'blue', 'red', 'purple', 'orange', 'pink']]

    print_table(table_data)


main()
