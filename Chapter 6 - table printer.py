
def print_table(table):

    col_widths = []
    for i in range(len(table)):
        col_widths.append(len(max(table[i], key=len)))

    for y in range(len(table[0])):
        for x in range(len(table)):
            print(table[x][y].rjust(col_widths[x]+2), end='')
        print()


def main():

    table_data = [['apples', 'oranges', 'cherries', 'banana', 'kiwi', 'blueberry'],
                  ['Alice', 'Bob', 'Carol', 'David', 'Luke', 'Laura'],
                  ['dogs', 'cats', 'moose', 'goose', 'bears', 'fish'],
                  ['green', 'blue', 'red', 'purple', 'orange', 'pink']]

    print_table(table_data)


main()