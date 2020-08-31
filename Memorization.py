# モジュールのインポート
import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk
from tkinter import filedialog
import random
import os
import zipfile

a = 0
b = 0

# メイン画面表示
root = tk.Tk()
root.title("top")
root.geometry('600x600')
root.configure(bg='blue')






# 学習セット読み込み画面
def  Learning_set_Read(event):
    fTyp = [("",".zip")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    filepath = filedialog.askopenfilename(filetypes = fTyp, initialdir = iDir)
    with open("設定.txt", mode='w') as f:
        f.write(filepath)




def One_choice(event):
    global a
    a = 1


def Two_choices(event):
    global a
    a = 2


def Three_choices(event):
    global a
    a = 3







# 問題画面
def problem(event):
    global a
    a = 0



    # 問題画面表示
    with open("設定.txt") as f:
        zipfilepath = f.read()

    # ファイルを解凍する
    with zipfile.ZipFile(zipfilepath) as zf:
        zf.extractall()

    # ファイルパスからフォルダ名取得
    basename = os.path.basename(zipfilepath)
    Folder_name = basename.replace('.zip', '')

    # 学習フォルダのファイル数
    files = os.listdir(Folder_name)
    # ファイル数割る4
    count = len(files)/4
    r = random.randint(1, count)


    # 学習画面表示
    problem1 = tk.Tk()
    problem1.title("problem")
    problem1.geometry("600x600")
    problem1.lower()

    # 問題文ファイル読み込み
    with open(Folder_name+"/"+str(r)+"-1.txt") as f:
        # ラベルに表示
        lbl =  tk.Label(problem1, text=f.read(), font =("",20))
        lbl.place(x=200,y=50)


    # 問題選択肢ファイル読み込み
    with open(Folder_name+"/"+str(r)+"-2.txt") as f:
        l_strip = [s.strip() for s in f.readlines()]



    # 説明文ファイル読み込み
    with open(Folder_name+"/"+str(r)+"-3.txt") as f:
        # ラベルに表示
        lbl =  tk.Label(problem1, text=f.read(), font =("",20))
        lbl.place(x=200,y=100)

    # 答えファイル読み込み
    with open(Folder_name+"/"+str(r)+"-4.txt") as f:
        global b
        b=f.read()
    # 問題選択肢をボタンに表示
    One_choice_button = tk.Button(problem1, text=l_strip[0], font=("",20))
    One_choice_button.place(x=200,y=150)
    One_choice_button.bind("<Button-1>", One_choice)


    Two_choices_button = tk.Button(problem1, text=l_strip[1], font=("",20))
    Two_choices_button.place(x=250,y=150)
    Two_choices_button.bind("<Button-1>", Two_choices)


    Three_choices_button = tk.Button(problem1, text=l_strip[2], font=("",20))
    Three_choices_button.place(x=300,y=150)
    Three_choices_button.bind("<Button-1>", Three_choices)



    # 正解不正解判定
    def Answer(event):
        if (a == int(b)):
            res = messagebox.showinfo("正解", "正解")
            if res == "ok":
                button = tk.Button(problem1, text='次の問題へ',command=problem1.destroy , font=("",20))
                button.place(x=200,y=400)
                button.bind("<Button-1>",problem)

        else:
            res = messagebox.showinfo("不正解", "不正解:"+l_strip[int(b)-1])
            if res == "ok":
                button = tk.Button(problem1, text='次の問題へ',command=problem1.destroy , font=("",20))
                button.place(x=200,y=400)
                button.bind("<Button-1>",problem)

    button = tk.Button(problem1, text='回答', font=("",20))
    button.place(x=200, y=300)
    button.bind("<Button-1>", Answer)


# トップ画面のボタン

# 学習開始ボタン
Button = tk.Button(text='学習開始',font=("",30))
Button.place(x=200,y=150)
Button.bind("<Button-1>",problem)

# 学習セットの読み込みボタン
Learning_set_Read_Button = tk.Button(text='学習セット読み込み',font=("",30))
Learning_set_Read_Button.place(x=200,y=250)
Learning_set_Read_Button.bind("<Button-1>",Learning_set_Read)


root.mainloop()
