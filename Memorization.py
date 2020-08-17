# モジュールのインポート
import tkinter as tk
import tkinter.messagebox as tkmsg
import tkinter.ttk as ttk
from tkinter import filedialog
import random
import os
import zipfile


# メイン画面表示
root = tk.Tk()
root.title("top")
root.geometry("600x600")

# 問題文ファイルの読み込み
# path = '問題/問題文.txt'
# with open(path, encoding="utf-8") as f:
#     l_strip = [s.strip() for s in f.readlines()]





# 学習セット読み込み画面
def  Learning_set_Read(event):
    fTyp = [("",".zip")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    filepath = filedialog.askopenfilename(filetypes = fTyp, initialdir = iDir)
    with open("設定.txt", mode='w') as f:
        f.write(filepath)

# 問題画面
def problem(event):


    # 問題画面表示
    with open("設定.txt") as f:
        zipfilepath = f.read()


    # ファイルを解凍する
    with zipfile.ZipFile(zipfilepath) as zf:
        zf.extractall()

    # ファイルパスからフォルダ名取得
    basename = os.path.basename(zipfilepath)
    Folder_name = basename.replace('.zip', '')


    files = os.listdir(Folder_name)  
    count = len(files)/4
    print(count)
    r = random.randint(1, count)



    problem1 = tk.Tk()
    problem1.title("problem")
    problem1.geometry("600x600")


    with open(Folder_name+"/"+str(r)+"-1.txt") as f:
        lbl =  tk.Label(problem1, text=f.read(), font =("",20))
        lbl.place(x=200,y=50)
 


        with open(Folder_name+"/"+str(r)+"-2.txt") as f:
            l_strip = [s.strip() for s in f.readlines()]
            print(l_strip)


            One_choice_button = tk.Button(problem1, text=l_strip[0], font=("",20))
            One_choice_button.place(x=50,y=100)
            # One_choice_button.bind("<Button-1>",)

            Two_choices_button = tk.Button(problem1, text=l_strip[1], font=("",20))
            Two_choices_button.place(x=100,y=100)

            Three_choices_button = tk.Button(problem1, text=l_strip[2], font=("",20))
            Three_choices_button.place(x=150,y=100)

# Learning_set_Read_Button.bind("<Button-1>",Learning_set_Read)


"""
def Question_creation(event):
    Question_creation1 = tk.Tk()
    Question_creation1.title("Question_creation")
    Question_creation1.geometry("600x600")


    # 問題文
    lbl = tk.Label(Question_creation1, text='問題文', font=("",20))
    lbl.place(x=200,y=50)

    txt = tk.Entry(Question_creation1,width=20)
    txt.place(x=200,y=150)



    Question1_lbl = tk.Label(Question_creation1, text='選択肢１',font=("",20))
    Question1_lbl.place(x=50,y=250)


    Question1_txt = tk.Entry(Question_creation1, width=20)
    Question1_txt.place(x=50,y=300)


    Question2_lbl = tk.Label(Question_creation1, text='選択肢2',font=("",20))
    Question2_lbl.place(x=200,y=250)


    Question2_txt = tk.Entry(Question_creation1, width=20)
    Question2_txt.place(x=200,y=300)

    Question3_lbl = tk.Label(Question_creation1, text='選択肢3',font=("",20))
    Question3_lbl.place(x=350,y=250)


    Question3_txt = tk.Entry(Question_creation1, width=20)
    Question3_txt.place(x=350,y=300)

    Question4_lbl = tk.Label(Question_creation1, text='説明文',font=("",20))
    Question4_lbl.place(x=200,y=350)


    Question4_txt = tk.Entry(Question_creation1, width=20)
    Question4_txt.place(x=200,y=400)





# 正解不正解判定
def Answer(event):
    global txt
    global r
    tmp = txt.get()
    if tmp == l_strip1[r]:
        tkmsg.showinfo(title="正解", message="正解")
    else:
        tkmsg.showinfo(title="不正解", message="不正解答えは"+l_strip1[r])
"""


# トップ画面のボタン

# 開始
Button = tk.Button(text='暗記開始',font=("",30))
Button.place(x=200,y=150)
Button.bind("<Button-1>",problem)

# 学習セットの読み込み
Learning_set_Read_Button = tk.Button(text='学習セット読み込み',font=("",30))
Learning_set_Read_Button.place(x=200,y=250)
Learning_set_Read_Button.bind("<Button-1>",Learning_set_Read)

# 問題作成
# Question_creation_Button = tk.Button(text='問題作成',font=("",30))
# Question_creation_Button.place(x=200,y=350)
# Question_creation_Button.bind("<Button-1>",Question_creation)


root.mainloop()
