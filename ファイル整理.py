import os
from os import path
import shutil

src = "/Users/kimihiro/Downloads/"
dst = "/Users/kimihiro/Downloads/csvファイル"
files = [i for i in os.listdir(src) if i.endswith("csv") and path.isfile(path.join(src, i))]
for f in files:
    print(f)
    shutil.move(path.join(src, f), dst)
