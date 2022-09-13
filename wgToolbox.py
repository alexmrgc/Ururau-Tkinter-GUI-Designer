#!/usr/bin/python
#-*- coding: utf-8 -*-

from tkinter import *
from wgWindow import *
from wgInspector import *
from widgets import *
import sys

class WidgetToolbox(Tk):    
    def __init__(self, window, inspector):
        super().__init__()
        self.resizable(True, True)
        self.geometry("200x400+0+10")
        self.title('Widget ToolBox')
        self.window = window
        self.inspector = inspector
        self.idx = 0
        # se fechar a janela
        self.protocol('WM_DELETE_WINDOW', self.sair)

        # frame top
        frame_top = LabelFrame(self, text='Actions')
        self.novo = Button(frame_top, text='novo', command=self.new_window, state=DISABLED)
        abrir = Button(frame_top, text='abrir', state=DISABLED)
        salvar = Button(frame_top, text='salvar', command=self.window.salvar)
        # frame main
        frame_main = LabelFrame(self, text='Widgets')        
        toplevel = Button(frame_main, text='Configurar janela', command=lambda: self.inspector.inspect_widget(self.window))        
        frame = Button(frame_main, text='LabelFrame', command=lambda: self.add_widget('WLabelFrame'))
        button = Button(frame_main, text='Button', command=lambda: self.add_widget('WButton'))
        label = Button(frame_main, text='Label', command=lambda: self.add_widget('WLabel'))
        entry = Button(frame_main, text='Entry', command=lambda: self.add_widget('WEntry'))
        text = Button(frame_main, text='Text', command=lambda: self.add_widget('WText'))
        scale = Button(frame_main, text='Scale', command=lambda: self.add_widget('WScale'))
        check = Button(frame_main, text='Checkbutton', command=lambda: self.add_widget('WCheckbutton'))
        drop = Button(frame_main, text='OptionMenu', command=lambda: self.add_widget('WOptionMenu'))
        radio = Button(frame_main, text='RadioButton', command=lambda: self.add_widget('WRadiobutton'))

        # layout frame top
        frame_top.pack(side=TOP, expand=True, fill=X)
        self.novo.pack(side=LEFT, expand=True, fill=X)
        abrir.pack(side=LEFT, expand=True, fill=X)
        salvar.pack(side=RIGHT, expand=True, fill=X)
        # layout frame main
        frame_main.pack(side=BOTTOM, expand=True, fill=X)
        toplevel.pack(fill=X)
        frame.pack(fill=X)
        button.pack(fill=X)
        label.pack(fill=X)
        entry.pack(fill=X)
        text.pack(fill=X)
        scale.pack(fill=X)
        check.pack(fill=X)
        drop.pack(fill=X)
        radio.pack(fill=X)

    def new_window(self):
        pass
##        self.inspector.destroy()
##        self.inspector = WidgetInspector()
##        self.window = WidgetWindow(self.inspector)
##        self.window.set_toolbox(self)
    
    def add_widget(self, tipo):
        strWg = tipo + str(self.idx)
        strWg = strWg.lower()

        # cria o widget
        if tipo == 'WOptionMenu':
            exec("%s = WOptionMenu(self.window)" % strWg)
        else:
            exec("%s = %s(self.window)" % (strWg, tipo))

        # chama inspector com o widget criado
        exec("self.inspector.inspect_widget(%s)" % strWg)

        self.idx += 1

    def sair(self):
        self.inspector.destroy()
        self.window.destroy()
        self.destroy()
        

if __name__=='__main__':
    Tk().withdraw()

    inspector = WidgetInspector()
    window = WidgetWindow(inspector)
    toolbox = WidgetToolbox(window, inspector)
    inspector.set_toolbox(toolbox)
    window.set_toolbox(toolbox)


##    print('Widget ToolBox ok')
##    toolbox.mainloop()
    
