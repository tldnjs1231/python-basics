import os
from random import randint as ri
from PIL import ImageTk
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry("500x900")
window.title("뭘까요?")
window.resizable(False, False)

score = 0
life = 5
포켓몬목록 = os.listdir("shadow")

la = tk.Label(window)
la.pack()

lalife = tk.Label(window, font=("맑은고딕", 30, "bold"), fg="red")
lalife.pack()

보기인덱스 = set()

def 문제출제():
    global 정답인덱스, 보기인덱스
    정답인덱스 = ri(0, len(포켓몬목록)-1)
    img = ImageTk.PhotoImage(file=f"shadow/{포켓몬목록[정답인덱스]}")
    la["image"] = img
    la.image = img
    보기인덱스 = set()
    보기인덱스.add(정답인덱스)

    while True:
        보기인덱스.add(ri(0, len(포켓몬목록)-1))
        if len(보기인덱스) == 5:
            break
    보기인덱스 = list(보기인덱스)

    for i in range(5):
        button[i]["text"] = 포켓몬목록[보기인덱스[i]].split("_")[1].split(".")[0]
    
    lalife["text"] = "♥ "*life + "♡ "* (5-life)

def 채점(idx):
    global 정답인덱스, 보기인덱스, score, life
    
    if 보기인덱스[idx] == 정답인덱스:
        score += 100
        img = ImageTk.PhotoImage(file=f"poke500/{포켓몬목록[정답인덱스]}")
        la["image"] = img
        la.image = img
        messagebox.showinfo("CORRECT!!", "정답입니다.")
        문제출제()
    else:
        life -= 1
        if life == 0:
            messagebox.showinfo("GAME OVER", f"당신의 점수는 {score} 입니다.")
            exit()
    lalife["text"] = "♥ "*life + "♡ "* (5-life)
    

button = [None]*5
for i in range(5):
    button[i] = tk.Button(window, command=lambda x=i:채점(x), width=20, font=("맑은고딕", 20, "bold"), fg="blue")
    button[i].pack()


문제출제()

window.mainloop()
