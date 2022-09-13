#!/usr/bin/python
#-*- coding: utf-8 -*-

from tkinter import *
from wgInspector import *
from tkinter.filedialog import asksaveasfilename
import sys


class WidgetWindow(Toplevel, WWidget):
    def __init__(self, inspector):
        super().__init__()
        WWidget.__init__(self)
        self.geometry('350x400+230+20')
        self.title('Widget Window')
        self.inspector = inspector
        self.filename = ''

        # se fechar a janela abre dialogo de salvar arqquivo
        self.protocol('WM_DELETE_WINDOW', self.close)

    def set_toolbox(self, tb):
        self.toolbox = tb
        
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

    def close(self):
        self.salvar()
        self.toolbox.novo['state'] = 'normal'
        self.inspector.destroy()
        self.destroy()
        

    def salvar(self):        
        intro = """#!/usr/bin/python\n#-*- coding: utf-8 -*-\n\nfrom tkinter import *\n\n"""
        window = """%s = Tk()\n%s.geometry('%s')\n\n""" % (self.nomeVar, self.nomeVar, self.winfo_geometry())
        wg_code = self._parser_widget()
        rodape = "\n\n%s.mainloop()" % self.nomeVar
        
        code = intro + window + wg_code + rodape
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

    def _parser_widget(self):
        wg_code = ''
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

            wg_code += wg.code(props_diff)
            
        
        return(wg_code)

        
if __name__=='__main__':
    Tk().withdraw()
    top = WidgetWindow()
    print('Widget Window ok')
##    top.mainloop()

    
