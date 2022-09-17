#!/usr/bin/python
#-*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from wgWindow import *
from widgets import *


class ScrollerLabelFrame(ttk.Frame):
    def __init__(self, master, text=''):
        ttk.Frame.__init__(self, master)

        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)

        # cria o frame externo e canvas dentro dele    
        self.frame_outer = ttk.Frame(master)
        self.canvas = Canvas(self.frame_outer)

        # cria scrollbar no frame externo e conecta com canvas
        self.scrollbar = Scrollbar(self.frame_outer, orient='vertical', command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # cria o frame interno rolável dentro de canvas
        self.frame_inner = ttk.LabelFrame(self.canvas, text=text)
        # evento <Configure> é chamado sempre que adicionamos / removemos widgets do frame interno
        self.frame_inner.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox('all')))

        # exibe o frame externo, canvas e scrollbar
        self.frame_outer.grid(sticky=(N,S,W,E))
        self.canvas.pack(side='left', fill='both', expand=True)
        self.scrollbar.pack(side='right', fill='y', expand=True)
        # exibe frame_inner dentro de canvas
        self.frame_id = self.canvas.create_window((0,0), window=self.frame_inner, anchor='nw')


class EntryInspector(ttk.Entry):
    def __init__(self, master, wg, prop):
        ttk.Entry.__init__(self, master)
        self.wg = wg
        self.prop = prop
        

class WidgetInspector(Toplevel):
    def __init__(self):
        super().__init__()
        self.resizable(True, True)
        self.geometry('390x500+780+0')
        self.title('Widget Inspector')
        
    def set_toolbox(self, toolbox):
        self.toolbox = toolbox
        # fechar o inspector, fecha window também
        self.protocol('WM_DELETE_WINDOW', self.toolbox.window.close)

    def set_widget_name(self, event):
        nome = event.widget.get()
        self.wg.nomeVar = nome

    def set_widget(self, event):
        # altera propriedade do widget
        e = event.widget
        valor = e.get()
        wg = e.wg
        try:
            wg[e.prop] = valor
        except TclError as erro:
            self.erro['text'] = erro
            self.erro['fg'] = 'red'

    def inspect_widget(self, wg):
        # cria o inspector dinamicamente com widget.keys()
        self.wg = wg
        self.prop = self.wg.keys()
       
        if hasattr(self, 'main'):
            self.main.frame_outer.destroy()
            self.main.frame_outer.pack_forget()
            self.frame_erro.destroy()
            self.frame_erro.pack_forget()
            
        # cria frames
        self.main = ScrollerLabelFrame(self, text=str(self.wg))
        self.create_code_frame()
        self.create_propertys_frame()
        self.create_error_frame()
        # layout
        self.frame_code.grid(row=0, columnspan=2, sticky=EW)
        self.frame_prop.grid(row=1, columnspan=2, sticky=EW)      
        self.frame_erro.grid(sticky=(W,E))

    def create_code_frame(self):
        self.frame_code = ttk.LabelFrame(self.main.frame_inner, text='Código:')
        ttk.Label(self.frame_code, text='Nome da variável', font='Helvetica 10 bold').grid(row=0, column=0, sticky=W)
        e = ttk.Entry(self.frame_code)
        e.bind('<FocusOut>', self.set_widget_name)
        e.bind('<Return>', self.set_widget_name)        
        e.grid(row=0, column=1)
        e.insert(0, self.wg.nomeVar)

            
        if self.wg.widgetName == 'tk_optionMenu':
            ttk.Label(self.frame_code, text='Valores', font='Helvetica 10 bold').grid(row=1, column=0, sticky=W)
            v = ttk.Entry(self.frame_code)
            v.bind('<FocusOut>', self.set_widget)
            v.bind('<Return>', self.set_widget)        
            v.grid(row=1, column=1)
            v.insert(0, self.wg.lista)

    def create_propertys_frame(self):
        self.frame_prop = ttk.LabelFrame(self.main.frame_inner, text='Propriedades:')
        i = 1
        for p in self.prop:
            # cria label : entry
            ttk.Label(self.frame_prop, text=p).grid(row=i, column=0, sticky=W)
            exec("e_%s = EntryInspector(self.frame_prop, self.wg, '%s')" % (p, p))
            # cria eventos de entry
            exec("e_%s.bind('<FocusOut>', self.set_widget)" % p)
            exec("e_%s.bind('<Return>', self.set_widget)" % p)
            # exibe o valor da propriedade em entry            
            exec("""e_%s.insert(0, "%s")""" % (p, self.wg[p]))
            exec("e_%s.grid(row=%i, column=1)" % (p, i))
            i += 1

    def create_error_frame(self):
        self.frame_erro = ttk.LabelFrame(self, text='Erro:')
        self.erro = ttk.Label(self.frame_erro, text=' ')
        self.erro.pack()

        
        

if __name__=='__main__':
    Tk().withdraw()
    inspector = WidgetInspector()
    print('Widget Inspector ok')

