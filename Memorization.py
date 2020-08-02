# モジュールのインポート
import tkinter as tk
import tkinter.messagebox as tkmsg
import random

# メイン画面表示
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


# 問題仮面
def problem(event):
    global r
    global txt

    # 問題画面表示
    problem1 = tk.Tk()
    problem1.title("problem")
    problem1.geometry("600x600")


    l = len(l_strip)
    r = random.randint(0,l-1)
    print(r)
    lbl = tk.Label(problem1, text=l_strip[r])
    lbl.place(x=300, y=300)
    txt = tk.Entry(problem1,width=20)
    txt.place(x=250, y=100)

    # 回答ボタン表示
    Button1= tk.Button(problem1,text='回答',font=("",30))
    Button1.place(x=250,y=200)
    Button1.bind("<Button-1>",Answer)

# 正解不正解判定
def Answer(event):
    global txt
    global r
    tmp = txt.get()
    if tmp == l_strip1[r]:
        tkmsg.showinfo(title="正解", message="正解")
    else:
        tkmsg.showinfo(title="不正解", message="不正解答えは"+l_strip1[r])



# 開始ボタン表示
Button = tk.Button(text='暗記開始',font=("",30))
Button.place(x=250,y=150)
Button.bind("<Button-1>",problem)
root.mainloop()
