from tkinter import *


def destroy():
    window.destroy()


def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True


winner = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]


def checking_tru():
    count_x = 0
    count_y = 0
    for i in range(3):
        for j in range(3):
            if winner[i][j] == 1:
                count_x += 1
            elif winner[i][j] == 2:
                count_y += 1
    if count_x <= count_y:
        print("x :", count_x, " y:", count_y)
        return True
    elif count_x > count_y:
        print("x :", count_x, " y:", count_y)
        return False


def next_turn(row, column):
    if checking_tru() is True:
        buttons[row][column]['text'] = 'X'
        winner[row][column] = 1
        if check_winner() is True:
            print("check 1")
            new_win = Toplevel()
            Label(new_win, text="Congratulations! Player 1 WIN (X)", font=('consoles', 20)).pack()
            Button(new_win, text="EXIT", font=('consoles', 20), bg="red", command=destroy).pack()

    else:
        buttons[row][column]['text'] = 'O'
        winner[row][column] = 2
        if check_winner() is True:
            print("check 2")
            new_win = Toplevel()
            Label(new_win, text="Congratulations! Player 2 WIN (O)", font=('consoles', 20)).pack()
            Button(new_win, text="EXIT", font=('consoles', 20), bg="red", command=destroy).pack()


window = Tk()
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(window, text="", font=('consoles', 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
