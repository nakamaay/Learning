import os

path = "/mnt/c/Users/nakah/OneDrive/デスクトップ/test.zip"
basename = os.path.basename(path)
print(basename.replace('.zip', ''))
