#!/usr/bin/python
#-*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from wgWindow import *
from wgInspector import *
from widgets import *
import sys


class WidgetToolbox(Tk):    
    def __init__(self, window, inspector):
        super().__init__()
        self.resizable(True, True)
        self.geometry("210x350+0+10")
        self.title('Widget ToolBox')
        self.window = window
        self.inspector = inspector
        self.idx = 0
        # se fechar a janela
        self.protocol('WM_DELETE_WINDOW', self.sair)

        mainframe = ttk.Frame(self)
        
        # frame top
        self.frame_top = ttk.LabelFrame(mainframe, text='Actions')
        self.novo = ttk.Button(self.frame_top, text='novo', width=7, command=self.new_window, state=DISABLED)
        self.abrir = ttk.Button(self.frame_top, text='abrir', width=7, state=DISABLED)
        self.salvar = ttk.Button(self.frame_top, text='salvar', width=7, command=self.window.salvar)
        
        # frame main
        self.frame_main = ttk.LabelFrame(mainframe, text='Widgets')        
        self.toplevel = ttk.Button(self.frame_main, text='Configurar janela', command=lambda: self.inspector.inspect_widget(self.window))        
        self.frame = ttk.Button(self.frame_main, text='LabelFrame', command=lambda: self.add_widget('WLabelFrame'))
        self.button = ttk.Button(self.frame_main, text='Button', command=lambda: self.add_widget('WButton'))
        self.label = ttk.Button(self.frame_main, text='Label', command=lambda: self.add_widget('WLabel'))
        self.entry = ttk.Button(self.frame_main, text='Entry', command=lambda: self.add_widget('WEntry'))
        self.text = ttk.Button(self.frame_main, text='Text', command=lambda: self.add_widget('WText'))
        self.scale = ttk.Button(self.frame_main, text='Scale', command=lambda: self.add_widget('WScale'))
        self.check = ttk.Button(self.frame_main, text='Checkbutton', command=lambda: self.add_widget('WCheckbutton'))
        self.drop = ttk.Button(self.frame_main, text='OptionMenu', command=lambda: self.add_widget('WOptionMenu'))
        self.radio = ttk.Button(self.frame_main, text='RadioButton', command=lambda: self.add_widget('WRadiobutton'))

        # layout frame top
        self.frame_top.pack(side=TOP, fill=X)
        self.novo.pack(side=LEFT)
        self.abrir.pack(side=LEFT)
        self.salvar.pack(side=RIGHT)

        # layout frame main
        self.frame_main.pack(side=BOTTOM, fill=BOTH)
        self.toplevel.pack(fill=X)
        self.frame.pack(fill=X)
        self.button.pack(fill=X)
        self.label.pack(fill=X)
        self.entry.pack(fill=X)
        self.text.pack(fill=X)
        self.scale.pack(fill=X)
        self.check.pack(fill=X)
        self.drop.pack(fill=X)
        self.radio.pack(fill=X)

        mainframe.grid(sticky=(N, S, W, E))

        
    def new_window(self):
        self.inspector.deiconify()
        self.window.deiconify()
        self.inspector.inspect_widget(self.window)
        # estado dos botões de toolbox
        self.buttons_on()

    def add_widget(self, tipo):
        nomeVar = tipo + str(self.idx)
        nomeVar = nomeVar.lower()
        
        # cria o widget
        if tipo == 'WOptionMenu':
            exec("%s = WOptionMenu(self.window.mainframe, '%s')" % (nomeVar, nomeVar))
        else:
            exec("%s = %s(self.window.mainframe, '%s')" % (nomeVar, tipo, nomeVar))

        # chama inspector com o widget criado
        exec("self.inspector.inspect_widget(%s)" % nomeVar)

        self.idx += 1

    def buttons_on(self):
        for b in self.frame_main.children.values():
            b['state'] = 'normal'

        self.novo['state'] = 'disabled'
        self.salvar['state'] = 'normal'

    def buttons_off(self):
        for b in self.frame_main.children.values():
            b['state'] = 'disabled'

        self.novo['state'] = 'normal'
        self.salvar['state'] = 'disabled'

    def sair(self):
        self.inspector.destroy()
        self.window.destroy()
        self.destroy()
        

if __name__=='__main__':
    Tk().withdraw()

    inspector = WidgetInspector()
    window = WidgetWindow()
    toolbox = WidgetToolbox(window, inspector)

    window.set_toolbox(toolbox)
    inspector.set_toolbox(toolbox)

    inspector.inspect_widget(window)


    print('Widget ToolBox ok')
##    toolbox.mainloop()
    
