from tkinter import *
from tkinter import ttk
from wgWindow import *
from random import randint


class WWidget:
    def __init__(self, nomeVar):
        self.nomeVar = nomeVar
        
        self.props_inicial = {}
        for k in self.keys():
            self.props_inicial[k] = self[k]
            
    def code(self, props_diff):
        write = "### %s ###\n" % self.widgetName
        write += "%s = %s(%s, **%s)\n" % (self.nomeVar, self.widgetName[5:].capitalize(), self.master.nomeVar, props_diff)
        write += "%s.place(x=%s, y=%s)\n" % (self.nomeVar, self.winfo_x(), self.winfo_y())
        write += "#################\n\n"
        return(write)
            
    def drag_n_drop(self, mf):
        # eventos drag'n'drop
        self.bind('<Button-1>', mf.drag_start)
        self.bind('<B1-Motion>', mf.drag_motion)
        self.bind('<ButtonRelease>', mf.on_release)

   
class WLabelFrame(ttk.LabelFrame, WWidget):
    def __init__(self, mf, nomeVar):
        ttk.LabelFrame.__init__(self, mf)
        WWidget.__init__(self, nomeVar)
        self.place(x=randint(20, 330), y=randint(20, 380))
        self.drag_n_drop(mf)
        self['text'] = 'Frame'
        self['width'] = 100
        self['height'] = 50
        
    def code(self, props_diff):
        write = "### %s ###\n" % self.widgetName
        write += "%s = ttk.LabelFrame(%s, **%s)\n" % (self.nomeVar, self.master.nomeVar, props_diff)
        write += "%s.place(x=%s, y=%s)\n" % (self.nomeVar, self.winfo_x(), self.winfo_y())
        write += "#################\n\n"
        return(write)
                

class WButton(ttk.Button, WWidget):
    def __init__(self, mf, nomeVar):
        ttk.Button.__init__(self, mf)
        WWidget.__init__(self, nomeVar)
        self.place(x=randint(20, 330), y=randint(20, 380))
        self.drag_n_drop(mf)
        self['text']='btn'


class WLabel(ttk.Label, WWidget):
    def __init__(self, mf, nomeVar):
        ttk.Label.__init__(self, mf)
        WWidget.__init__(self, nomeVar)
        self.place(x=randint(20, 330), y=randint(20, 380))
        self.drag_n_drop(mf)
        self['text'] = 'label'

    
class WEntry(ttk.Entry, WWidget):
    def __init__(self, mf, nomeVar):
        ttk.Entry.__init__(self, mf)
        WWidget.__init__(self, nomeVar)
        self.place(x=randint(20, 330), y=randint(20, 380))
        self.drag_n_drop(mf)


class WText(Text, WWidget):
    def __init__(self, mf, nomeVar):
        Text.__init__(self, mf)
        WWidget.__init__(self, nomeVar)
        self.place(x=randint(20, 330), y=randint(20, 380))
        self.drag_n_drop(mf)
        self['width'] = 10
        self['height'] = 10

    def code(self, props_diff):
        write = "### %s ###\n" % self.widgetName
        write += "%s = Text(%s, **%s)\n" % (self.nomeVar, self.master.nomeVar, props_diff)
        write += "%s.place(x=%s, y=%s)\n" % (self.nomeVar, self.winfo_x(), self.winfo_y())
        write += "#################\n\n"
        return(write)
    

class WScale(ttk.Scale, WWidget):
    def __init__(self, mf, nomeVar):
        ttk.Scale.__init__(self, mf)
        WWidget.__init__(self, nomeVar)
        self.place(x=randint(20, 330), y=randint(20, 380))
        self.drag_n_drop(mf)
        self['from_'] = 0
        self['to'] = 100
        self['orient'] = 'horizontal'

        
class WCheckbutton(ttk.Checkbutton, WWidget):
    def __init__(self, mf, nomeVar):
        ttk.Checkbutton.__init__(self, mf)
        WWidget.__init__(self, nomeVar)
        self.place(x=randint(20, 330), y=randint(20, 380))
        self.drag_n_drop(mf)
        self['text'] = 'check'


class WOptionMenu(ttk.OptionMenu, WWidget):
    def __init__(self, mf, nomeVar):
        self.nomeVar = nomeVar
        self.opc = IntVar()
        self.lista = [1, 2, 3]
        self.opc.set(self.lista[0])
        ttk.OptionMenu.__init__(self, mf, self.opc, *self.lista)
        WWidget.__init__(self, nomeVar)
        self.place(x=randint(20, 330), y=randint(20, 380))
        self.drag_n_drop(mf)

    def code(self, props_diff):
        write = "### OptionMenu ###\n"
        write += "opc = IntVar()\n"
        write += "lista = [1,2,3]\n"
        write += "opc.set(lista[0])\n"
        write += "%s = ttk.OptionMenu(%s, opc, *lista, **%s)\n" % (self.nomeVar, self.master.nomeVar, props_diff)
        write += "%s.place(x=%s, y=%s)\n" % (self.nomeVar, self.winfo_x(), self.winfo_y())
        write += "#################\n\n"
        return(write)


class WRadiobutton(ttk.LabelFrame, WWidget):
    def __init__(self, mf, nomeVar):
        ttk.LabelFrame.__init__(self, mf)
        WWidget.__init__(self, nomeVar)

        self.opc = IntVar()
        self.dic = {'um':1,
                    'dois':2,
                    'tres':3}

        for k, w in self.dic.items():
            ttk.Radiobutton(self, text=k, value=w).pack(anchor=W)

        self.place(x=randint(20, 330), y=randint(20, 380))
        self.drag_n_drop(mf)
        self['text'] = 'RadioButtons'

    def code(self, props_diff):
        write = "### Radiobutton ###\n"
        write += "lf = ttk.LabelFrame(%s, text='Radio Buttons')\n" % self.master.nomeVar
        write += "opc = IntVar()\n"
        write += "dic = {'um':1, 'dois':2,'tres':3}\n"
        write += "for k, w in dic.items():\n"
        write += "    ttk.Radiobutton(lf, text=k, variable=opc, value=w).pack(anchor=W)\n"
        write += "lf.place(x=%s, y=%s)\n" % (self.winfo_x(), self.winfo_y())
        write += "#################\n\n"
        return(write)
    

if __name__=='__main__':
    top = Tk()
    
    f = ScrollerLabelFrame(top)

    for i in range(30):
        Button(f.frame_inner, text='foo').pack()

    


