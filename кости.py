from tkinter import *
import random, time
#funkisya yaratmiz
def bros():
    x = random.choice(['b.png', 'b2.png', 'b3.png',
                       'b4.png', 'b5.png', 'b6.png',])
    return x
def img(event):
    global b1, b2
    for i in range(10):
        b1 = PhotoImage(file=(bros()))
        b2 = PhotoImage(file=(bros()))
        labl['image'] = b1 
        lab2['image'] = b2
        time.sleep(0.1)
        root.update()
#O'zgaruvchi orqali tkinter ni chaqidik tk - tkinterni qisqa varianti
root = Tk()
#maydon kengligi
root.geometry('400x200')
#programmani tepadagi nomi ya'ni title
root.title('Игры в кости, Сделай бросок!!!')
#yaratga maydonimiz oz'garmas bo'ladi kicraytiribam kattartiribam bo'lmaydi
root.resizable(height = False, width = False)
#programmaizga icon ka qo'yamiz
root.iconphoto(True, PhotoImage(file=('iconka.png')))
#programmiz ichiga background photo qo'yamiz
font = PhotoImage(file=('holst.png'))
Label(root, image=font).pack() #label orqali finksiyani chaqiramiz
#pack orqali programmamizga background image joylashtiramiz
#labl o'zgaruvchi orqali Labelni chaqirdik
labl = Label(root)
#USHBU KODIMIZ ORQALI programmamizda joy ajratdik
labl.place(relx = 0.3, rely = 0.5, anchor=CENTER)   #anchor=CENTER O'RTADAGI KORDINATNI BERADI
lab2 = Label(root)
lab2.place(relx = 0.7, rely = 0.5, anchor=CENTER)
#knopka yasaymiz
root.bind('<1>', img)
#srazu kpikni tashedi
img('event')
root.mainloop()
