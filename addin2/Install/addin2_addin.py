import arcpy
import pythonaddins

class RiskButton(object):
    """Implementation for addin2_addin.RiskButton (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog("m:/Documents/Programming2/Prac1/Models.tbx", "TraffordModelScript")
       