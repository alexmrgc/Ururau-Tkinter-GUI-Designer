#!/usr/bin/python
#-*- coding: utf-8 -*-

from tkinter import *
from wgInspector import *
from tkinter.filedialog import asksaveasfilename


class WidgetWindow(Toplevel):
    def __init__(self, inspector):
        super().__init__()
        self.geometry('350x400+230+20')
        self.title('Widget Window')
        self.inspector = inspector
        self.filename = ''
        self.nomeObj = self._name[1:]
        # se fechar a janela abre dialogo de salvar arqquivo
        self.protocol('WM_DELETE_WINDOW', self.salvar)
        
    def drag_start(self, event):
        wg = event.widget
        wg.startX = event.x
        wg.startY = event.y
        
    def drag_motion(self, event):
        wg = event.widget
        x = wg.winfo_x() - wg.startX + event.x
        y = wg.winfo_y() - wg.startY + event.y
        wg.place(x=x, y=y)

    def on_release(self, event):
        self.inspector.inspect_widget(event.widget)

    def salvar(self):        
        code = self._parser()
        print(code)

##        # message file dialog
##        if self.filename:
##            with open(self.filename,'w') as arq:
##                arq.write(code)
##        else:
##            fn = asksaveasfilename(initialfile='app.py', defaultextension='*.py', filetypes=[('arquivos .py','*.py'),('todos arquivos','*.*')])
##            with open(fn,'w') as arq:
##                arq.write(code)
##
##            self.title(fn)
##            self.filename = fn

    def _parser(self):                        
        code = """#!/usr/bin/python\n#-*- coding: utf-8 -*-\n\nfrom tkinter import *\n\ntop = Tk()\ntop.geometry('%s')\n\n""" % self.winfo_geometry()

        # pega todos os widgets dentro de window
        for wg in self.children.values():
            props_atual = {}
            props_diff = {}
            
            # pega as propriedades atuais do widget
            for k in wg.keys():
                props_atual[k] = wg[k]

            # compara as propriedades iniciais e atuais do widget
            for p in props_atual.keys():
                if props_atual[p] != wg.props_inicial[p]:
                    props_diff[p] = props_atual[p]

            # add widget ao code
            write = wg.code(props_diff)
            code += write

        code += "\n\ntop.mainloop()"
        return(code)

        
if __name__=='__main__':
    Tk().withdraw()
    top = WidgetWindow()
    print('Widget Window ok')
##    top.mainloop()

    
