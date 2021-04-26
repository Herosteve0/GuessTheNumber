from tkinter import *
from tkinter.ttk import *
import random
import time

win = Tk()
win.title("Guess The Number")
mainbg = '#e5964a'
win.config(bg=mainbg)
geox = 430
geoy = round(geox*0.9)
win.geometry(str(geox)+'x'+str(geoy))

def gtn():
    def endgame(*args):
        global entnum, lblanimation1, run

        run = 0
        entnum.delete(0, 'end')
        entnum.config(state=DISABLED)

        def restart(f):
            global run, entnum, lblanimation1, btnstart, progrbar
            if f == 0:
                win.destroy()
            elif f == 1:
                progrbar.destroy()
                lblanimation1.destroy()
                exit.destroy()
                reset.destroy()
                btnstart = Label(win)
                entnum.delete(0, 'end')
                setup(1)

        exit = Button(win, text="Exit")
        reset = Button(win, text="Play Again")

        starty = geoy
        endy = 300

        y1 = starty
        y2 = starty
        step = 75
        exit.place(x=75, y=y1)
        reset.place(x=280, y=y2)
        for i in range(step):
            y1 += (endy-y1)/15
            y2 += (endy-y2)/15
            exit.place(x=75, y=y1)
            reset.place(x=280, y=y2)
            exit.update()
            reset.update()
            time.sleep(0.01)

        exit.config(command= lambda: restart(0))
        reset.config(command= lambda: restart(1))

    def selectnumber(*args):
        global entnum, rn, dif, progrbar
        entnum.config(state=DISABLED)
        speed = 200
        steps = 15
        swaps = 15
        mainx = 300
        starty = 225
        endy = 275
        lblnum1 = Label(win, font=("Comic Sans", 15), background=mainbg)
        lblnum2 = Label(win, font=("Comic Sans", 15), background=mainbg)
        lblnum3 = Label(win, font=("Comic Sans", 15), background=mainbg)
        lblblank1 = Label(win)
        lblblank2 = Label(win)
        lblblank3 = Label(win)
        y1 = starty
        r = random.randint(1, 100)
        lblnum1.config(text=str(r))
        y2 = starty-25
        r = random.randint(1, 100)
        lblnum2.config(text=str(r))
        y3 = starty-50
        r = random.randint(1, 100)
        lblnum3.config(text=str(r))
        for i in range(swaps*steps):
            lblnum1.place(x=mainx, y=y1)
            lblnum2.place(x=mainx, y=y2)
            lblnum3.place(x=mainx, y=y3)
            lblblank1.destroy()
            lblblank2.destroy()
            lblblank1 = Label(win, font=("Comic Sans", 15), text="     ", background=mainbg)
            lblblank2 = Label(win, font=("Comic Sans", 15), text="     ", background=mainbg)
            lblblank3 = Label(win, font=("Comic Sans", 15), text="     ", background=mainbg)
            lblblank1.place(x=mainx, y=starty-12)
            lblblank2.place(x=mainx, y=endy+12)
            lblblank3.place(x=mainx, y=starty-38)
            y1 += (endy-starty)/steps
            y2 += (endy-starty)/steps
            y3 += (endy-starty)/steps
            if y1 >= endy:
                y1 = starty
                r = random.randint(1, 100)
                lblnum1.config(text=str(r))
            if y2 >= endy:
                y2 = starty
                r = random.randint(1, 100)
                lblnum2.config(text=str(r))
            if y3 >= endy:
                y3 = starty
                r = random.randint(1, 100)
                lblnum3.config(text=str(r))
            lblnum1.update()
            lblnum2.update()
            lblnum3.update()
            lblblank1.update()
            lblblank2.update()
            time.sleep(1/speed)
        lblnum1.destroy()
        lblnum2.destroy()
        lblblank1.destroy()
        lblblank2.destroy()
        lblblank3.destroy()
        lblnum3.place(x=mainx-25, y=starty+((endy-starty)/3))
        for i in range(4):
            lblnum3.config(text=" Number\nSelected!")
            lblnum3.update()
            time.sleep(0.5)
            lblnum3.config(text="")
            lblnum3.update()
            time.sleep(0.5)
        lblnum3.destroy()
        rn = random.randint(1, 100)
        dif = ""
        entnum.config(state=WRITABLE)
        progrbar = Progressbar(win, orient=HORIZONTAL, length=geox, mode='determinate')
        progrbar.place(x=0, y=200)

    def setup(f):
        global entnum, btnstart, background, prtext, an, dif, run, predif
        if f == 0:
            lbltitle = Label(win, text="Weclome!", font=("Comic Sans", 57), background=mainbg)
            lbltitle.place(x=0, y=0)
            lblisn1 = Label(win, text="Instructions!", font=("Comic Sans", 20), background=mainbg)
            lblisn1.place(x=0, y=90)
            lblisn2 = Label(win, text="-Type a number between 1 and 100", font=("Comic Sans", 15), background=mainbg)
            lblisn2.place(x=0, y=125)
            lblisn3 = Label(win, text="-The arrow next to the entry will tell you whether\nyou are higher or lower!", font=("Comic Sans", 15), background=mainbg)
            lblisn3.place(x=0, y=150)
            btnstart = Button(win, text="Start", command= lambda: setup(1))
            btnstart.place(x=geox*0.4, y=260)
            entnum = Entry(win, width=3, font=("Comic Sans", 20), background=mainbg)
        elif f == 1:
            prtext = ""
            an = 0
            dif = ""
            predif = dif
            run = 1
            btnstart.destroy()
            entnum.place(x=50, y=250)
            selectnumber()
            win.after(100, mainloop)
            entnum.bind('<Return>', checkanswer)

    def entcheck(*args):
        global entnum, prtext
        text = entnum.get()
        if text.isdecimal():
            if int(text) >= 1 and int(text) <= 100:
                prtext = text
            else:
                entnum.delete(0, 'end')
                entnum.insert(0, prtext)
        elif text == "":
            prtext = text
        else:
            entnum.delete(0, 'end')
            entnum.insert(0, prtext)

    def checkanswer(*args):
        global entnum, rn, dif, predif, an, at, progrbar

        if entnum.get() != "":
            a = int(entnum.get())

            predif = dif
            progrbar['value'] = a

            if a == rn:
                dif = "correct"
            elif a < rn:
                dif = "up"
            elif a > rn:
                dif = "down"

            if predif != dif:
                an = 1
                at = 5

            if a != rn:
                entnum.delete(0, 'end')

    def numdiranimation(*args):
        global dif, an, mainbg, lblanimation1, at

        mainx = 300

        if an == 0:
            lblanimation1 = Label(win, background=mainbg)
            an = 1
            at = 0

        if at == 5:
            if dif == "correct":
                lblanimation1.config(text="√", font=("Comic Sans", 30))
                lblanimation1.place(x=mainx, y=250)
                an = 1
                endgame()
            elif dif == "":
                t = ""
                for i in range(an):
                    t = t+"."
                lblanimation1.config(text=t, font=("Comic Sans", 15))
                lblanimation1.place(x=mainx-(an*2), y=265)
                an += 1
                if an == 4:
                    an = 1
            elif dif == "up":
                t = ""
                for i in range(an):
                    t = t+"ᐱ\n"
                lblanimation1.config(text=t, font=("Comic Sans", 10))
                lblanimation1.place(x=mainx, y=273-((an-1)*15))
                an += 1
                if an == 4:
                    an = 1
            elif dif == "down":
                t = ""
                for i in range(an):
                    t = t+"ᐯ\n"
                lblanimation1.config(text=t, font=("Comic Sans", 10))
                lblanimation1.place(x=mainx, y=273-((an-1)*15))
                an += 1
                if an == 4:
                    an = 1
            at = 0
        else:
            at += 1

    def mainloop(*args):
        global run
        if run == 1:
            entcheck()
            numdiranimation()
            win.after(100, mainloop)

    setup(0)

gtn()
win.mainloop()