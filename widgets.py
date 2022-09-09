from tkinter import *
from wgWindow import *
from random import randint


class WWidget:
    def __init__(self):
        self.props_inicial = {}
        for k in self.keys():
            self.props_inicial[k] = self[k]

        self.nomeVar = self._name[1:]
        self.idx = 0
            
    def code(self, props_diff):
        write = "### %s ###\n" % self.widgetName
        write += "%s = %s(%s, **%s)\n" % (self.nomeVar, self.widgetName.capitalize(), self.master.nomeVar, props_diff)
        write += "%s.place(x=%s, y=%s)\n" % (self.nomeVar, self.winfo_x(), self.winfo_y())
        write += "#################\n\n"
        return(write)
            
    def drag_n_drop(self, master):
        # eventos drag'n'drop
        self.bind('<Button-1>', master.drag_start)
        self.bind('<B1-Motion>', master.drag_motion)
        self.bind('<ButtonRelease>', master.on_release)

   
class WLabelFrame(LabelFrame, WWidget):
    def __init__(self, master):
        LabelFrame.__init__(self, master)
        WWidget.__init__(self)
        self.place(x=randint(20, 330), y=randint(20, 380))
        self.drag_n_drop(master)
        self['text'] = 'Frame'
        self['width'] = 100
        self['height'] = 50
        
    def code(self, props_diff):
        write = "### %s ###\n" % self.widgetName
        write += "%s = LabelFrame(%s, **%s)\n" % (self.nomeVar, self.master.nomeVar, props_diff)
        write += "%s.place(x=%s, y=%s)\n" % (self.nomeVar, self.winfo_x(), self.winfo_y())
        write += "#################\n\n"
        return(write)
                

class WButton(Button, WWidget):
    def __init__(self, master):
        Button.__init__(self, master)
        WWidget.__init__(self)
        self.place(x=randint(20, 330), y=randint(20, 380))
        self.drag_n_drop(master)
        self['text']='btn'


class WLabel(Label, WWidget):
    def __init__(self, master):
        Label.__init__(self, master)
        WWidget.__init__(self)
        self.place(x=randint(20, 330), y=randint(20, 380))
        self.drag_n_drop(master)
        self['text'] = 'label'

    
class WEntry(Entry, WWidget):
    def __init__(self, master):
        Entry.__init__(self, master)
        WWidget.__init__(self)
        self.place(x=randint(20, 330), y=randint(20, 380))
        self.drag_n_drop(master)


class WText(Text, WWidget):
    def __init__(self, master):
        Text.__init__(self, master)
        WWidget.__init__(self)
        self.place(x=randint(20, 330), y=randint(20, 380))
        self.drag_n_drop(master)
        self['width'] = 10
        self['height'] = 10


class WScale(Scale, WWidget):
    def __init__(self, master):
        Scale.__init__(self, master)
        WWidget.__init__(self)
        self.place(x=randint(20, 330), y=randint(20, 380))
        self.drag_n_drop(master)
        self['from_'] = 0
        self['to'] = 100
        self['orient'] = 'horizontal'

        
class WCheckbutton(Checkbutton, WWidget):
    def __init__(self, master):
        Checkbutton.__init__(self, master)
        WWidget.__init__(self)
        self.place(x=randint(20, 330), y=randint(20, 380))
        self.drag_n_drop(master)
        self['text'] = 'check'


class WOptionMenu(OptionMenu, WWidget):
    def __init__(self, master):
        self.opc = IntVar()
        self.lista = [1, 2, 3]
        self.opc.set(self.lista[0])
        OptionMenu.__init__(self, master, self.opc, *self.lista)
        WWidget.__init__(self)
        self.place(x=randint(20, 330), y=randint(20, 380))
        self.drag_n_drop(master)

    def code(self, props_diff):
        write = "### OptionMenu ###\n"
        write += "opc = IntVar()\n"
        write += "lista = [1,2,3]\n"
        write += "opc.set(lista[0])\n"
        write += "%s = OptionMenu(%s, opc, *lista, **%s)\n" % (self.nomeVar, self.master.nomeVar, props_diff)
        write += "%s.place(x=%s, y=%s)\n" % (self.nomeVar, self.winfo_x(), self.winfo_y())
        write += "#################\n\n"
        return(write)


class WRadiobutton(LabelFrame, WWidget):
    def __init__(self, master):
        LabelFrame.__init__(self, master)
        WWidget.__init__(self)

        self.opc = IntVar()
        self.dic = {'um':1,
                    'dois':2,
                    'tres':3}

        for k, w in self.dic.items():
            Radiobutton(self, text=k, value=w).pack(anchor=W)

        self.place(x=randint(20, 330), y=randint(20, 380))
        self.drag_n_drop(master)
        self['text'] = 'RadioButtons'

    def code(self, props_diff):
        write = "### Radiobutton ###\n"
        write += "lf = LabelFrame(%s, text='Radio Buttons')\n" % self.master.nomeVar
        write += "opc = IntVar()\n"
        write += "dic = {'um':1, 'dois':2,'tres':3}\n"
        write += "for k, w in dic.items():\n"
        write += "\tRadiobutton(lf, text=k, value=w).pack(anchor=W)\n"
        write += "lf.place(x=%s, y=%s)\n" % (self.winfo_x(), self.winfo_y())
        write += "#################\n\n"
        return(write)
    

if __name__=='__main__':
    top = Tk()
    
    f = ScrollerLabelFrame(top)

    for i in range(30):
        Button(f.frame_inner, text='foo').pack()

    


