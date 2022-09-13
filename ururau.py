from tkinter import *
from wgWindow import *
from wgToolbox import *
from wgInspector import *

if __name__=='__main__':
    Tk().withdraw()

    inspector = WidgetInspector()
    window = WidgetWindow(inspector)
    toolbox = WidgetToolbox(window, inspector)
    window.set_toolbox(toolbox)

    print('Ururau Tkinter GUI Designer ok')

        

