# モジュールのインポート
import tkinter as tk
import random


root = tk.Tk()
root.title("top")
root.geometry("600x600")

# 問題文ファイルの読み込み
path = '問題/問題文.txt'
with open(path, encoding="utf-8") as f:
    l_strip = [s.strip() for s in f.readlines()]
# 答えファイルの読み込み
path1 = '問題/答え.txt'
with open(path1, encoding="utf-8") as f:
    l_strip1 = [s.strip() for s in f.readlines()]



def start(event):
    global r
    global txt
    start1 = tk.Tk()
    start1.title("start")
    start1.geometry("600x600")
    l = len(l_strip)
    r = random.randint(0,l-1)
    print(r)
    lbl = tk.Label(start1, text=l_strip[r])
    lbl.place(x=300, y=300)
    txt = tk.Entry(start1,width=20)
    txt.place(x=250, y=100)
    Button1= tk.Button(start1,text='回答',font=("",30))
    Button1.place(x=250,y=200)
    Button1.bind("<Button-1>",Answer)


def Answer(event):
    global txt
    global r
    tmp = txt.get()
    if tmp == l_strip1[r]:
        print("正解")
    else:
        print("不正解答えは"+l_strip1[r])

# ボタン
Button = tk.Button(text='暗記開始',font=("",30))
Button.place(x=250,y=150)
Button.bind("<Button-1>",start)
root.mainloop()
