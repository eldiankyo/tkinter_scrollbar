import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Tkinter Scrollbar Demo')
root.resizable(0, 0)
root.config(bg='#d9d9d9')

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

text = tk.Text(root, height=10, bg='white', fg='black')
text.grid(row=0, column=0, sticky='ew')

scrollbar = ttk.Scrollbar(root, orient='v', command=text.yview)
scrollbar.grid(row=0, column=1, sticky='ns')

text['yscrollcommand'] = scrollbar.set

for i in range(1, 50):
    position = f'{i}.0'
    text.insert(position, f'Line {i}\n')

root.mainloop()