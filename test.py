import tkinter as tk
a=tk.Tk()
root = tk.Tk()
button=tk.Button(a, text='aaaa', command=root.destroy)
button.pack()


root.mainloop()