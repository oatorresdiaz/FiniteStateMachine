from Tkinter import *

class GUI:
    'Tool to draw GUI'

    window = Tk()
    graphic = Canvas()
    entry = Entry()

    def __init__(self, windowTitle, windowSize):
        self.window.wm_title(windowTitle)
        self.window.minsize(width = windowSize, height = windowSize)

    def drawState(self, x, y, dm, state, isFinalState, isUsed):
        if(isUsed):
            color = "red"
        else:
            color = "black"
        self.graphic.create_text(x + dm/2, y + dm/2,fill= color,font="Times 20 bold",
                        text= state)
        self.graphic.create_oval(x, y, x + dm, y + dm, outline = color)
        if(isFinalState):
            self.graphic.create_oval(x + 5, y + 5, x + dm - 5, y + dm - 5, outline = color)

    def drawTransitionLine(self, x1, y1, x2, y2, isUsed):
        if(isUsed):
            color = "red"
        else:
            color = "black"
        self.graphic.create_line(x1, y1, x2, y2, fill = color)
        self.graphic.create_oval(x2 - 3, y2 - 3, x2 + 3, y2 + 3, fill = color, outline = color) #pointhead

    def drawTransitionArc(self, x1, y1, x2, y2, startAngle, endAngle, isUsed):
        if(isUsed):
            color = "red"
        else:
            color = "black"
        self.graphic.create_arc(x1 - 5, y1 - 10, x2 + 5, y2, start=startAngle, extent=endAngle, style = "arc", outline = color)

    def drawLabel(self, x, y, text, isUsed):
        if(isUsed):
            color = "red"
        else:
            color = "black"
        self.graphic.create_text(x, y, fill= color,font="Times 20 bold",
                        text= text)

    def drawPointhead(self,x,y, isUsed):
        if(isUsed):
            color = "red"
        else:
            color = "black"
        self.graphic.create_oval(x - 3, y - 3, x + 3, y + 3, fill=color, outline = color)

    def drawEntryBox(self, x, y, width):
        self.entry.place(x = x, y = y, width = width)

    def drawButton(self, x, y, width, text, action):
        button = Button(text = text, width = width)
        button.place(x = x, y = y)
        button.bind("<Button-1>", action)

    def drawStateMachineOutputLabel(self, x, y, accepted):
        self.graphic.create_text(x, y, fill= "black",font="Times 20 bold",
                        text= accepted)

    def renderGraphics(self):
        self.graphic.pack(fill=BOTH, expand=1)

    def getEntryText(self):
        return self.entry.get()

    def clear(self):
        self.graphic.delete("all")

    def runMainLoop(self):
        self.window.mainloop()


