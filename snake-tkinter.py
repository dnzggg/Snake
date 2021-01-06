from tkinter import *
import random
import ctypes
import random


class snake(object):
    def __init__(self, tk):
        self.h = 0
        self.score = 0
        self.cors = []
        self.tk = tk
# self.tk.attributes('-transparent','black')
        self.label = Label(tk, text='Snake Game        To Exit Press <Esc> Key         Your Score   ' + str(self.score), font=("Helvetica", 20), fg='black')
        self.label.pack()
        self.tk.title('Snake')
        self.tk.overrideredirect(True)
        self.tk.geometry("{0}x{1}+0+0".format(self.tk.winfo_screenwidth(), self.tk.winfo_screenheight()))
        user32 = ctypes.windll.user32
        self.width,self.height = user32.GetSystemMetrics(0),user32.GetSystemMetrics(1)
        self.can = Canvas(tk, width=self.width, height=self.height - 30, background='black')
        self.can.pack()
        self.tk.bind("<Escape>",self.exit)
        self.tk.bind("<Right>", self.moverigth)
        self.tk.bind("<Left>", self.moveleft)
        self.tk.bind("<Up>", self.moveup)
        self.tk.bind("<Down>", self.movedown)
        self.afood()
        self.snake()


    def snake(self):
        self.snake = self.can.create_rectangle(0, 0, 20, 20, fill='blue', tags='snake')
        self.moverigth(event=None)


    def afood(self):
        self.x = random.randrange(20, self.width - 20, 20)
        self.y = random.randrange(20, self.height - 60, 20)
        self.food = self.can.create_rectangle(self.x, self.y, self.x + 20, self.y + 20, fill='red')


    def moverigth(self, event):
        self.h += 1
        print (self.h)
        self.stop = 'r'
        self.tk.bind("<Up>",self.moveup)
        self.tk.bind("<Down>",self.movedown)
        self.tk.unbind("<Left>")
        self.tk.unbind("<Right>")
        while True:
            if self.stop != 'r':
                break
            self.can.move('snake', 20, 0)
            self.tk.update()
            if self.stop != 'r':
                break
            self.tk.after(50)
            if self.stop != 'r':
                break
            self.eat()
            if self.stop != 'r':
                break

    def moveleft(self, event):
        self.h += 1
        print (self.h)
        self.stop = 'l'
        self.tk.bind("<Up>",self.moveup)
        self.tk.bind("<Down>",self.movedown)
        self.tk.unbind("<Right>")
        self.tk.unbind("<Left>")
        while True:
            if self.stop != 'l':
                break
            self.can.move('snake', -20, 0)
            self.tk.update()
            if self.stop != 'l':
                break
            self.tk.after(50)
            if self.stop != 'l':
                break
            self.eat()
            if self.stop != 'l':
                break

    def moveup(self, event):
        self.h += 1
        print (self.h)
        self.stop = 'u'
        self.tk.unbind("<Down>")
        self.tk.bind("<Left>",self.moveleft)
        self.tk.bind("<Right>",self.moverigth)
        self.tk.unbind("<Up>")
        while True:
            if self.stop != 'u':
                break
            self.can.move('snake', 0, -20)
            self.tk.update()
            if self.stop != 'u':
                break
            self.tk.after(50)
            if self.stop != 'u':
                break
            self.eat()
            if self.stop != 'u':
                break

    def movedown(self, event):
        self.h += 1
        print (self.h)
        self.stop = 'd'
        self.tk.bind("<Left>",self.moveleft)
        self.tk.bind("<Right>",self.moverigth)
        self.tk.unbind("<Up>")
        self.tk.unbind("<Down>")
        while True:
            if self.stop != 'd':
                break
            self.can.move('snake', 0, 20)
            self.tk.update()
            if self.stop != 'd':
                break
            self.tk.after(50)
            if self.stop != 'd':
                break
            self.eat()
            if self.stop != 'd':
                break


    def tail(self):
        for a in range(0,self.score + 1):
                if a > 0:
                    try:
                        self.can.coords('tail1',self.cors[0],self.cors[1],self.cors[2],self.cors[3])
                    except:
                        pass;
                if a > 1:
                    try:
                        self.can.coords('tail' + str(a),self.cors[(a ) * 4 - 4] ,self.cors[(a ) * 4 - 3],self.cors[(a ) * 4 - 2],self.cors[(a ) * 4 - 1])
                    except:
                        pass;


    def eat(self):
      try:
          self.scoor = self.can.coords(self.snake)
          self.fcoor = self.can.coords(self.food)
      except:
          pass;
      self.x1 = self.scoor[0]
      self.x2 = self.scoor[2]
      self.y1 = self.scoor[1]
      self.y2 = self.scoor[3]
      self.cors.append(self.x1)
      self.cors.append(self.y1)
      self.cors.append(self.x2)
      self.cors.append(self.y2)
      if self.x1<0 or self.x2>self.width or self.y1<0 or self.y1>self.height - 50:
              self.stop = 'a'
              self.tk.unbind("<Down>")
              self.tk.unbind("<Up>")
              self.tk.unbind("<Right>")
              self.tk.unbind("<Left>")
              pass
      if self.scoor == self.fcoor:
          self.score += 1
          self.label.config(text='Snake Game        To Exit Press <Esc> Key         Your Score   ' + str(self.score))
          self.can.delete(self.food)
          self.afood()
          for a in range(self.score, self.score + 1):
              if a == 1:
                  self.atail = self.can.create_rectangle(self.cors[0],self.cors[1],self.cors[2],self.cors[3], fill='white',tags='tail' + str(a))
              else:
                  self.tcoor = self.can.coords('tail' + str(a - 1))
                  self.x3 = self.tcoor[0]
                  self.x4 = self.tcoor[2]
                  self.y3 = self.tcoor[1]
                  self.y4 = self.tcoor[3]
                  self.cors.append(self.x3)
                  self.cors.append(self.y3)
                  self.cors.append(self.x4)
                  self.cors.append(self.y4)
                  self.atail = self.can.create_rectangle(self.cors[a * 4 - 4] ,self.cors[a * 4 - 3],self.cors[a * 4 - 2],self.cors[a * 4 - 1], fill='white',tags='tail' + str(a))
      self.tail()
      del self.cors[3]
      del self.cors[2]
      del self.cors[1]
      del self.cors[0]


    def exit(self,event):
      self.stop = 'a'
      #self.tk.destroy()


tk = Tk()
snake(tk)
