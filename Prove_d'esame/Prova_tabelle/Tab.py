import random


def main():
    ROWS = 5
    COLUMN = 3

    tabella = []

    for i in range(ROWS):
        row = []
        for j in range(COLUMN):
            row.append(random.randint(0,10))
        tabella.append(row)
    return tabella

def stampatabella(tabella):
    '''for i in range(len(tabella)):
        for j in range(len(tabella[0])):
            print("%8d" % tabella[i][j], end="")
        print()'''

    for i in range(len(tabella)):
        print("|".join(f"{j: ^5d}"for j in tabella[i]))


if __name__ == "__main__":
    tabella = main()
    print(tabella)
    stampatabella(tabella)

