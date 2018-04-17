import tkinter
import os
import random

FIELD_SIZE = 4

main_window = tkinter.Tk()
main_window.title('Game')

files_list = sorted(os.listdir('nums'))

images_list = []
for file_name in files_list:
    full_path = os.path.join('nums', file_name)
    image = tkinter.PhotoImage(file=full_path)
    images_list.append(image)

labels_list = []
for row in range(FIELD_SIZE):
    buf = []
    for column in range(FIELD_SIZE):
        x = row * FIELD_SIZE + column
        label = tkinter.Label(main_window, image=images_list[x])
        # label.x = x
        label.row = row
        label.column = column
        label.grid(row=row, column=column)
        buf.append(label)

    labels_list.append(buf)
curr = labels_list[-1][-1]

def exchange_items(arg):
    arg.row, curr.row = curr.row, arg.row
    arg.column, curr.column = curr.column, arg.column
    labels_list[arg.row][arg.column], arg = arg, labels_list[arg.row][arg.column]


def render_item(arg):
    arg.grid(row=arg.row, column=arg.column)

def key_press(arg):
    print(arg)
    near = None

    if arg == 'Up' and curr.row > 0:
        near = labels_list[curr.row - 1][curr.column]
    elif arg == 'Down' and curr.row < FIELD_SIZE - 1:
        near = labels_list[curr.row + 1][curr.column]
    elif arg == 'Left' and curr.column > 0:
        near = labels_list[curr.row][curr.column - 1]
    elif arg == 'Right' and curr.column < FIELD_SIZE - 1:
        near = labels_list[curr.row][curr.column + 1]

    if near:
        exchange_items(near)
        render_item(near)
        render_item(curr)

def shyffle_game():
    action = ['Up', 'Down', 'Left', 'Right']
    for _ in range(100):
        current_action = random.sample(action, 1)[0]
        key_press(current_action)
        # print(current_action)

shyffle_game()

main_window.after(2000, shyffle_game)

main_window.bind('<KeyPress>', lambda x: key_press(x.keysym))

main_window.mainloop()
