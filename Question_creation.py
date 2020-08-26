import os
import shutil
path = "問題/"
a = 1


Folder_name = input("フォルダ名\n")
os.mkdir(path+Folder_name)
while True:
    Problem_statement = input("問題文\n")
    with open(path+Folder_name+"/"+str(a)+"-1.txt", mode='w') as f:
        f.write(Problem_statement)

    Choice_one = input("選択肢1\n")
    with open(path+Folder_name+"/"+str(a)+"-2.txt", mode='a') as f:
        f.write(Choice_one+"\n")

    Option_two = input("選択肢2\n")
    with open(path+Folder_name+"/"+str(a)+"-2.txt", mode='a') as f:
        f.write(Option_two+"\n")

    Option_three = input("選択肢3\n")
    with open(path+Folder_name+"/"+str(a)+"-2.txt", mode='a') as f:
        f.write(Option_three)

    Explanatory_text = input("説明文\n")
    with open(path+Folder_name+"/"+str(a)+"-3.txt", mode='w') as f:
        f.write(Explanatory_text)

    Answer_number = (input("答え番号\n"))
    with open(path+Folder_name+"/"+str(a)+"-4.txt", mode='w') as f:
        f.write(Answer_number)

    End = input("保存しますか y/n")
    if End == "y":
        shutil.make_archive(Folder_name, 'zip', root_dir=path)

    a +=1
