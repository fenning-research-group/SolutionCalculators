# SolutionCalculators

Most up to date python gui for making perovskite solutions 

Use "fbs" packager to turn into executable

to convert designer file use following code in terminal, careful not to overwrite ! ! ! 
pyuic5 -x /Users/deniz/Documents/PythonScripts/PSK_MV_Calc_3.ui > /Users/deniz/Documents/PythonScripts/PSK_MV_Calc_UI.py
pyinstaller -w -n Calc /Users/deniz/Documents/PythonScripts/PSK_MV_Calc_4.py
pyinstaller --onefile /Users/deniz/Documents/PythonScripts/PSK_MV_Calc_4.py
if pyinstaller doesnt work use "fbs startproject" in terminal to begin the packaging
def setupUi and def retranslateUi are coded through PyDesigner software