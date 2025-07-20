import win32com.client
import subprocess
import pandas as pd
from time import sleep as slp

class SapGui(object):
    def __init__(self):
        self.path = "C:\\Program Files\\SAP\\FrontEnd\\SAPGUI\\saplogon.exe"
        subprocess.Popen(self.path)
        
        self.SapGuiAuto = win32com.client.GetObject("SAPGUI")
        application = self.SapGuiAuto.GetScriptingEngine
        
        self.connection = application.OpenConnection("SAP - ECC 6.0 EHP7", True)
        slp(3)
        self.session = self.connection.Children(0)
        self.session.findById("wnd[0]").maximize