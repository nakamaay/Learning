# モジュールのインポート
import tkinter as tk



root = tk.Tk()
root.title("top")
root.geometry("600x600")

# 問題文ファイルの読み込み
path = '問題/問題文.txt'
with open(path) as f:
    l_strip = [s.strip() for s in f.readlines()]
# 答えファイルの読み込み
path1 = '問題/答え.txt'
with open(path1) as f:
    l_strip1 = [s.strip() for s in f.readlines()]



def start(event):
    start1 = tk.Tk()
    start1.title("start")
    start1.geometry("600x600")
    lbl = tk.Label(start1, text=l_strip[0])
    lbl.place(x=300, y=300)
    txt = tk.Entry(start1,width=20)
    txt.place(x=250, y=100)
    Button = tk.Button(text='回答',font=("",30))
    Button.place(x=250,y=200)

# ボタン
Button = tk.Button(text='暗記開始',font=("",30))
Button.place(x=250,y=150)
Button.bind("<Button-1>",start)
root.mainloop()
