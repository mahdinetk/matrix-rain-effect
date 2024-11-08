import curses
import time
from random import randint


stdscr = curses.initscr()
curses.start_color()
curses.noecho()
curses.cbreak()
stdscr.nodelay(True)
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
# set the main variables
letters = "いうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんアイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン"
lines = curses.LINES - 1
cols = curses.COLS - 1
matrix = []
count = []
max = []
min = []
y = []
x = []



def init():
    global count, max, min, y, x, matrix, cols

    #to make the x coordinates of matrix rains according to the number of cols of each terminal
    for i in range(1, cols, 5):
            x.append(i)

    # to make a 2D list that each list is used for a set of consecutive letters
    for i in range(len(x)):
        matrix.append([])
        y.append(-1)
        count.append(0)
        max.append(randint(14, lines - 1))
        min.append(randint(8, lines - 6))


# this function removes letters when they reach the bottom of the terminal space
def end_of_matrix():
    global matrix, cols

    for i in matrix:
        letter, y, x = i[-1].split(",")
        if int(y) + 1 == lines:
            stdscr.addstr(int(y) + 1, int(x), " ", curses.color_pair(1))
            y = str(-2)
            matrix[matrix.index(i)].insert(0, f"{letter},{y},{x}")
            del matrix[matrix.index(i)][-1]



# the function to move the letters from the top to the bottom
def move(matrix_index):
    global matrix

    for i in reversed(matrix[matrix_index]):
        letter, y, x = i.split(",")
        y = int(y)
        x = int(x)
        stdscr.addstr(y + 2, x, letter, curses.color_pair(1))
        if y > -2:
             stdscr.addstr(y + 1, x, " ", curses.color_pair(1))
        stdscr.refresh()

        # update the y coordinate for each letter
        new_y = str(y + 1)
        matrix[matrix_index][matrix[matrix_index].index(i)] = f"{letter},{new_y},{str(x)}"


# changing the last letter of matrix rain randomly
def change_the_last_letter(matrix_index):
    global matrix
    letter, y, x = matrix[matrix_index][0].split(",")
    y = int(y)
    x = int(x)

    if not letter == " ":
        num = randint(0, len(letters) - 1)
        letter = letters[num]
        matrix[matrix_index][0] = f"{letter},{y},{x}"

    letter, y, x = matrix[matrix_index][-1].split(",")
    y = int(y)
    x = int(x)

    stdscr.addstr(y, x, letter)



# main function to draw the matrix rain
def draw(item, letter):
    global matrix, y, x
    matrix[item].append(f"{letter},{y[item]},{x[item]}")

    y[item] += 1
    count[item] += 1

    stdscr.addstr(y[item], x[item], letter, curses.color_pair(1))
    stdscr.refresh()


init()

# the main function that continues the loop of program and rain matrix
def continue_():
    global count, matrix, letters, max, y, x

    for i in range(len(matrix)):
        if min[i] < count[i] < max[i]:
           letter = " "
           draw(i, letter)

        elif count[i] < max[i]:
            # choosing a letter randomly
            num = randint(0, len(letters) - 1)
            letter = letters[num]
            draw(i, letter)

        else:
            end_of_matrix()
            move(i)
            change_the_last_letter(i)


# the main loop of the program that ends after pressing 'q'
raining = True
while raining:
    time.sleep(0.06)
    try:
        key = stdscr.getch()
    except:
        key = -1

    if key == ord("q"):
        raining = False
    else:
        continue_()

curses.endwin()
