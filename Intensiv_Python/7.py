import tkinter
import os

main_window = tkinter.Tk()
main_window.title('Game')

files_list = sorted(os.listdir('nums'))
print(files_list)

images_list = []
for file_name in files_list:
    full_path = os.path.join('nums', file_name)
    image = tkinter.PhotoImage(file=full_path)
    images_list.append(image)

labels_list = []
for num, image in enumerate(images_list):
    label = tkinter.Label(main_window, image=image)
    _row = num // 4
    _column = num % 4
    print(num, _row, _column)
    label.grid(row=_row, column=_column)
    labels_list.append(label)

print(labels_list)

main_window.mainloop()

# while True:
#     pass
