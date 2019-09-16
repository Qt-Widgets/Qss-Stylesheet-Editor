import os
dir=os.path.dirname(__file__)+"/img"
os.chdir(os.path.dirname(__file__))

s='<!DOCTYPE RCC>\n<RCC version="1.0">\n<qresource prefix="img">\n'

for f in os.listdir(dir):
    if(f.endswith(".png") or f.endswith(".jpg")
        or f.endswith(".ico") or f.endswith(".icon")):
        l='    <file alias="{0}">img/{0}</file>\n'.format(f)
        s+=l
        print("added "+f)
        
s+="</qresource>\n</RCC>\n"
print("\ncreate qrcfile")
with open("img.qrc","w",newline="") as out:
    out.write(s)
   
print("\ncompile qrc to py")

import os
os.system("pyrcc5 img.qrc -o img_rc.py")

input()