# Deniz Cakan 
# Last updated: 02/02/2020

# mods to import
import sys, csv, os
import numpy as np
import pandas as pd
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon

# to convert designer file use following code in terminal, careful not to overwrite ! ! ! 
# pyuic5 -x /Users/deniz/Documents/PythonScripts/PSK_MV_Calc_3.ui > /Users/deniz/Documents/PythonScripts/PSK_MV_Calc_UI.py
# pyinstaller -w -n Calc /Users/deniz/Documents/PythonScripts/PSK_MV_Calc_4.py
# pyinstaller --onefile /Users/deniz/Documents/PythonScripts/PSK_MV_Calc_4.py
# if pyinstaller doesnt work use "fbs startproject" in terminal to begin the packaging

# def setupUi and def retranslateUi are coded through PyDesigner software

############################
# GUI Aesthetic & Naming 
############################

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(577, 659)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 0, 530, 602))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 0, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(80, 0, 60, 16))
        self.label_2.setObjectName("label_2")
        self.savebutton_send = QtWidgets.QPushButton(self.tab)
        self.savebutton_send.setGeometry(QtCore.QRect(340, 520, 171, 20))
        self.savebutton_send.setObjectName("savebutton_send")
        self.label_47 = QtWidgets.QLabel(self.tab)
        self.label_47.setGeometry(QtCore.QRect(140, 0, 60, 16))
        self.label_47.setObjectName("label_47")
        self.totalvolumeoutput = QtWidgets.QTextBrowser(self.tab)
        self.totalvolumeoutput.setGeometry(QtCore.QRect(130, 20, 61, 21))
        self.totalvolumeoutput.setObjectName("totalvolumeoutput")
        self.solventdensity = QtWidgets.QLineEdit(self.tab)
        self.solventdensity.setGeometry(QtCore.QRect(10, 70, 61, 21))
        self.solventdensity.setObjectName("solventdensity")
        self.solventtotalvolume = QtWidgets.QTextBrowser(self.tab)
        self.solventtotalvolume.setGeometry(QtCore.QRect(10, 120, 61, 21))
        self.solventtotalvolume.setObjectName("solventtotalvolume")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(10, 50, 111, 16))
        self.label_15.setObjectName("label_15")
        self.PbI2deinsitycheck = QtWidgets.QLineEdit(self.tab)
        self.PbI2deinsitycheck.setGeometry(QtCore.QRect(90, 320, 61, 21))
        self.PbI2deinsitycheck.setObjectName("PbI2deinsitycheck")
        self.PbI2solventaddition_final = QtWidgets.QTextBrowser(self.tab)
        self.PbI2solventaddition_final.setGeometry(QtCore.QRect(170, 290, 61, 21))
        self.PbI2solventaddition_final.setObjectName("PbI2solventaddition_final")
        self.PbI2addition = QtWidgets.QTextBrowser(self.tab)
        self.PbI2addition.setGeometry(QtCore.QRect(170, 260, 61, 21))
        self.PbI2addition.setObjectName("PbI2addition")
        self.PbI2weight = QtWidgets.QLineEdit(self.tab)
        self.PbI2weight.setGeometry(QtCore.QRect(90, 260, 61, 21))
        self.PbI2weight.setObjectName("PbI2weight")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(90, 240, 60, 16))
        self.label_3.setObjectName("label_3")
        self.FAPI_v = QtWidgets.QTextBrowser(self.tab)
        self.FAPI_v.setGeometry(QtCore.QRect(260, 320, 61, 21))
        self.FAPI_v.setObjectName("FAPI_v")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(10, 240, 60, 16))
        self.label_4.setObjectName("label_4")
        self.label_17 = QtWidgets.QLabel(self.tab)
        self.label_17.setGeometry(QtCore.QRect(260, 300, 51, 20))
        self.label_17.setObjectName("label_17")
        self.label_16 = QtWidgets.QLabel(self.tab)
        self.label_16.setGeometry(QtCore.QRect(170, 240, 101, 16))
        self.label_16.setObjectName("label_16")
        self.label_21 = QtWidgets.QLabel(self.tab)
        self.label_21.setGeometry(QtCore.QRect(10, 290, 61, 21))
        self.label_21.setObjectName("label_21")
        self.FAIweight = QtWidgets.QLineEdit(self.tab)
        self.FAIweight.setGeometry(QtCore.QRect(10, 260, 61, 21))
        self.FAIweight.setObjectName("FAIweight")
        self.PbI2solventvoladdition = QtWidgets.QTextBrowser(self.tab)
        self.PbI2solventvoladdition.setGeometry(QtCore.QRect(90, 290, 61, 21))
        self.PbI2solventvoladdition.setObjectName("PbI2solventvoladdition")
        self.label_39 = QtWidgets.QLabel(self.tab)
        self.label_39.setGeometry(QtCore.QRect(10, 380, 60, 16))
        self.label_39.setObjectName("label_39")
        self.PbBr2addition = QtWidgets.QTextBrowser(self.tab)
        self.PbBr2addition.setGeometry(QtCore.QRect(170, 400, 61, 21))
        self.PbBr2addition.setObjectName("PbBr2addition")
        self.MABrweight = QtWidgets.QLineEdit(self.tab)
        self.MABrweight.setGeometry(QtCore.QRect(10, 400, 61, 21))
        self.MABrweight.setObjectName("MABrweight")
        self.PbBr2deinsitycheck = QtWidgets.QLineEdit(self.tab)
        self.PbBr2deinsitycheck.setGeometry(QtCore.QRect(90, 460, 61, 21))
        self.PbBr2deinsitycheck.setObjectName("PbBr2deinsitycheck")
        self.label_40 = QtWidgets.QLabel(self.tab)
        self.label_40.setGeometry(QtCore.QRect(260, 440, 61, 20))
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.tab)
        self.label_41.setGeometry(QtCore.QRect(170, 380, 101, 16))
        self.label_41.setObjectName("label_41")
        self.MAPBr_v = QtWidgets.QTextBrowser(self.tab)
        self.MAPBr_v.setGeometry(QtCore.QRect(260, 460, 61, 21))
        self.MAPBr_v.setObjectName("MAPBr_v")
        self.PbBr2solventaddition_final = QtWidgets.QTextBrowser(self.tab)
        self.PbBr2solventaddition_final.setGeometry(QtCore.QRect(170, 430, 61, 21))
        self.PbBr2solventaddition_final.setObjectName("PbBr2solventaddition_final")
        self.label_42 = QtWidgets.QLabel(self.tab)
        self.label_42.setGeometry(QtCore.QRect(90, 380, 60, 16))
        self.label_42.setObjectName("label_42")
        self.PbBr2solventvoladdition = QtWidgets.QTextBrowser(self.tab)
        self.PbBr2solventvoladdition.setGeometry(QtCore.QRect(90, 430, 61, 21))
        self.PbBr2solventvoladdition.setObjectName("PbBr2solventvoladdition")
        self.PbBr2weight = QtWidgets.QLineEdit(self.tab)
        self.PbBr2weight.setGeometry(QtCore.QRect(90, 400, 61, 21))
        self.PbBr2weight.setObjectName("PbBr2weight")
        self.label_43 = QtWidgets.QLabel(self.tab)
        self.label_43.setGeometry(QtCore.QRect(10, 430, 61, 16))
        self.label_43.setObjectName("label_43")
        self.MAPBr_v_mix = QtWidgets.QTextBrowser(self.tab)
        self.MAPBr_v_mix.setGeometry(QtCore.QRect(90, 530, 61, 21))
        self.MAPBr_v_mix.setObjectName("MAPBr_v_mix")
        self.label_44 = QtWidgets.QLabel(self.tab)
        self.label_44.setGeometry(QtCore.QRect(170, 510, 51, 20))
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.tab)
        self.label_45.setGeometry(QtCore.QRect(10, 510, 51, 20))
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.tab)
        self.label_46.setGeometry(QtCore.QRect(90, 510, 61, 20))
        self.label_46.setObjectName("label_46")
        self.FAPI_v_mix = QtWidgets.QTextBrowser(self.tab)
        self.FAPI_v_mix.setGeometry(QtCore.QRect(10, 530, 61, 21))
        self.FAPI_v_mix.setObjectName("FAPI_v_mix")
        self.CsI_v_mix = QtWidgets.QTextBrowser(self.tab)
        self.CsI_v_mix.setGeometry(QtCore.QRect(170, 530, 61, 21))
        self.CsI_v_mix.setObjectName("CsI_v_mix")
        self.savepath = QtWidgets.QTextBrowser(self.tab)
        self.savepath.setGeometry(QtCore.QRect(340, 540, 171, 31))
        self.savepath.setObjectName("savepath")
        self.datevalue = QtWidgets.QTextBrowser(self.tab)
        self.datevalue.setGeometry(QtCore.QRect(250, 10, 241, 31))
        self.datevalue.setObjectName("datevalue")
        self.DeviceCount = QtWidgets.QLineEdit(self.tab)
        self.DeviceCount.setGeometry(QtCore.QRect(30, 20, 31, 21))
        self.DeviceCount.setObjectName("DeviceCount")
        self.Volumeperdevice = QtWidgets.QLineEdit(self.tab)
        self.Volumeperdevice.setGeometry(QtCore.QRect(80, 20, 31, 21))
        self.Volumeperdevice.setObjectName("Volumeperdevice")
        self.run_send = QtWidgets.QPushButton(self.tab)
        self.run_send.setGeometry(QtCore.QRect(100, 150, 141, 91))
        self.run_send.setObjectName("run_send")
        self.DeviceCount_final = QtWidgets.QTextBrowser(self.tab)
        self.DeviceCount_final.setGeometry(QtCore.QRect(250, 530, 61, 21))
        self.DeviceCount_final.setObjectName("DeviceCount_final")
        self.label_49 = QtWidgets.QLabel(self.tab)
        self.label_49.setGeometry(QtCore.QRect(250, 510, 71, 20))
        self.label_49.setObjectName("label_49")
        self.label_22 = QtWidgets.QLabel(self.tab)
        self.label_22.setGeometry(QtCore.QRect(10, 320, 51, 21))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.tab)
        self.label_23.setGeometry(QtCore.QRect(10, 460, 51, 21))
        self.label_23.setObjectName("label_23")
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(250, 60, 261, 221))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.label_19 = QtWidgets.QLabel(self.tab)
        self.label_19.setGeometry(QtCore.QRect(10, 100, 111, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.tab)
        self.label_20.setGeometry(QtCore.QRect(250, 40, 141, 16))
        self.label_20.setObjectName("label_20")
        self.label_50 = QtWidgets.QLabel(self.tab)
        self.label_50.setGeometry(QtCore.QRect(350, 480, 61, 20))
        self.label_50.setObjectName("label_50")
        self.date_input = QtWidgets.QLineEdit(self.tab)
        self.date_input.setGeometry(QtCore.QRect(340, 500, 71, 21))
        self.date_input.setObjectName("date_input")
        self.solutiontype_input = QtWidgets.QLineEdit(self.tab)
        self.solutiontype_input.setGeometry(QtCore.QRect(410, 500, 61, 21))
        self.solutiontype_input.setObjectName("solutiontype_input")
        self.note_input = QtWidgets.QLineEdit(self.tab)
        self.note_input.setGeometry(QtCore.QRect(470, 500, 41, 21))
        self.note_input.setObjectName("note_input")
        self.label_51 = QtWidgets.QLabel(self.tab)
        self.label_51.setGeometry(QtCore.QRect(410, 480, 61, 20))
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.tab)
        self.label_52.setGeometry(QtCore.QRect(470, 480, 61, 20))
        self.label_52.setObjectName("label_52")
        self.label_48 = QtWidgets.QLabel(self.tab)
        self.label_48.setGeometry(QtCore.QRect(10, 490, 141, 20))
        self.label_48.setObjectName("label_48")
        self.label_27 = QtWidgets.QLabel(self.tab)
        self.label_27.setGeometry(QtCore.QRect(100, 50, 111, 16))
        self.label_27.setObjectName("label_27")
        self.solvent_target_output = QtWidgets.QTextBrowser(self.tab)
        self.solvent_target_output.setGeometry(QtCore.QRect(100, 70, 61, 21))
        self.solvent_target_output.setObjectName("solvent_target_output")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.solventtotalvolume_2 = QtWidgets.QTextBrowser(self.tab_3)
        self.solventtotalvolume_2.setGeometry(QtCore.QRect(0, 120, 61, 21))
        self.solventtotalvolume_2.setObjectName("solventtotalvolume_2")
        self.label_18 = QtWidgets.QLabel(self.tab_3)
        self.label_18.setGeometry(QtCore.QRect(0, 50, 111, 16))
        self.label_18.setObjectName("label_18")
        self.PbI2weight_2 = QtWidgets.QLineEdit(self.tab_3)
        self.PbI2weight_2.setGeometry(QtCore.QRect(80, 260, 61, 21))
        self.PbI2weight_2.setObjectName("PbI2weight_2")
        self.label_24 = QtWidgets.QLabel(self.tab_3)
        self.label_24.setGeometry(QtCore.QRect(0, 100, 111, 16))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.tab_3)
        self.label_25.setGeometry(QtCore.QRect(0, 320, 51, 21))
        self.label_25.setObjectName("label_25")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 60, 16))
        self.label_5.setObjectName("label_5")
        self.solventdensity_2 = QtWidgets.QLineEdit(self.tab_3)
        self.solventdensity_2.setGeometry(QtCore.QRect(0, 70, 61, 21))
        self.solventdensity_2.setObjectName("solventdensity_2")
        self.run_send_2 = QtWidgets.QPushButton(self.tab_3)
        self.run_send_2.setGeometry(QtCore.QRect(100, 150, 141, 91))
        self.run_send_2.setObjectName("run_send_2")
        self.label_26 = QtWidgets.QLabel(self.tab_3)
        self.label_26.setGeometry(QtCore.QRect(0, 290, 61, 21))
        self.label_26.setObjectName("label_26")
        self.Volumeperdevice_2 = QtWidgets.QLineEdit(self.tab_3)
        self.Volumeperdevice_2.setGeometry(QtCore.QRect(70, 20, 31, 21))
        self.Volumeperdevice_2.setObjectName("Volumeperdevice_2")
        self.PbI2solventvoladdition_2 = QtWidgets.QTextBrowser(self.tab_3)
        self.PbI2solventvoladdition_2.setGeometry(QtCore.QRect(80, 290, 61, 21))
        self.PbI2solventvoladdition_2.setObjectName("PbI2solventvoladdition_2")
        self.PbI2deinsitycheck_2 = QtWidgets.QLineEdit(self.tab_3)
        self.PbI2deinsitycheck_2.setGeometry(QtCore.QRect(80, 320, 61, 21))
        self.PbI2deinsitycheck_2.setObjectName("PbI2deinsitycheck_2")
        self.DeviceCount_2 = QtWidgets.QLineEdit(self.tab_3)
        self.DeviceCount_2.setGeometry(QtCore.QRect(20, 20, 31, 21))
        self.DeviceCount_2.setObjectName("DeviceCount_2")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(70, 0, 60, 16))
        self.label_6.setObjectName("label_6")
        self.totalvolumeoutput_2 = QtWidgets.QTextBrowser(self.tab_3)
        self.totalvolumeoutput_2.setGeometry(QtCore.QRect(120, 20, 61, 21))
        self.totalvolumeoutput_2.setObjectName("totalvolumeoutput_2")
        self.label_53 = QtWidgets.QLabel(self.tab_3)
        self.label_53.setGeometry(QtCore.QRect(130, 0, 60, 16))
        self.label_53.setObjectName("label_53")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(80, 240, 60, 16))
        self.label_7.setObjectName("label_7")
        self.label_28 = QtWidgets.QLabel(self.tab_3)
        self.label_28.setGeometry(QtCore.QRect(100, 50, 111, 16))
        self.label_28.setObjectName("label_28")
        self.solvent_target_output_2 = QtWidgets.QTextBrowser(self.tab_3)
        self.solvent_target_output_2.setGeometry(QtCore.QRect(100, 70, 61, 21))
        self.solvent_target_output_2.setObjectName("solvent_target_output_2")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(10, 240, 60, 16))
        self.label_8.setObjectName("label_8")
        self.CsIweight_2 = QtWidgets.QLineEdit(self.tab_3)
        self.CsIweight_2.setGeometry(QtCore.QRect(10, 260, 61, 21))
        self.CsIweight_2.setObjectName("CsIweight_2")
        self.PbI2solventaddition_final_2 = QtWidgets.QTextBrowser(self.tab_3)
        self.PbI2solventaddition_final_2.setGeometry(QtCore.QRect(150, 290, 61, 21))
        self.PbI2solventaddition_final_2.setObjectName("PbI2solventaddition_final_2")
        self.PbI2addition_2 = QtWidgets.QTextBrowser(self.tab_3)
        self.PbI2addition_2.setGeometry(QtCore.QRect(150, 260, 61, 21))
        self.PbI2addition_2.setObjectName("PbI2addition_2")
        self.label_29 = QtWidgets.QLabel(self.tab_3)
        self.label_29.setGeometry(QtCore.QRect(240, 300, 61, 20))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.tab_3)
        self.label_30.setGeometry(QtCore.QRect(150, 240, 101, 16))
        self.label_30.setObjectName("label_30")
        self.CsI_v_2 = QtWidgets.QTextBrowser(self.tab_3)
        self.CsI_v_2.setGeometry(QtCore.QRect(240, 320, 61, 21))
        self.CsI_v_2.setObjectName("CsI_v_2")
        self.note_input_2 = QtWidgets.QLineEdit(self.tab_3)
        self.note_input_2.setGeometry(QtCore.QRect(470, 500, 41, 21))
        self.note_input_2.setObjectName("note_input_2")
        self.label_54 = QtWidgets.QLabel(self.tab_3)
        self.label_54.setGeometry(QtCore.QRect(350, 480, 61, 20))
        self.label_54.setObjectName("label_54")
        self.savebutton_send_2 = QtWidgets.QPushButton(self.tab_3)
        self.savebutton_send_2.setGeometry(QtCore.QRect(340, 520, 171, 20))
        self.savebutton_send_2.setObjectName("savebutton_send_2")
        self.label_55 = QtWidgets.QLabel(self.tab_3)
        self.label_55.setGeometry(QtCore.QRect(410, 480, 61, 20))
        self.label_55.setObjectName("label_55")
        self.savepath_2 = QtWidgets.QTextBrowser(self.tab_3)
        self.savepath_2.setGeometry(QtCore.QRect(340, 540, 171, 31))
        self.savepath_2.setObjectName("savepath_2")
        self.solutiontype_input_2 = QtWidgets.QLineEdit(self.tab_3)
        self.solutiontype_input_2.setGeometry(QtCore.QRect(410, 500, 61, 21))
        self.solutiontype_input_2.setObjectName("solutiontype_input_2")
        self.label_56 = QtWidgets.QLabel(self.tab_3)
        self.label_56.setGeometry(QtCore.QRect(470, 480, 61, 20))
        self.label_56.setObjectName("label_56")
        self.date_input_2 = QtWidgets.QLineEdit(self.tab_3)
        self.date_input_2.setGeometry(QtCore.QRect(340, 500, 71, 21))
        self.date_input_2.setObjectName("date_input_2")
        self.label_57 = QtWidgets.QLabel(self.tab_3)
        self.label_57.setGeometry(QtCore.QRect(250, 40, 141, 16))
        self.label_57.setObjectName("label_57")
        self.listWidget_2 = QtWidgets.QListWidget(self.tab_3)
        self.listWidget_2.setGeometry(QtCore.QRect(250, 60, 261, 221))
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.PbBr2deinsitycheck_2 = QtWidgets.QLineEdit(self.tab_3)
        self.PbBr2deinsitycheck_2.setGeometry(QtCore.QRect(80, 460, 61, 21))
        self.PbBr2deinsitycheck_2.setObjectName("PbBr2deinsitycheck_2")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(80, 380, 60, 16))
        self.label_10.setObjectName("label_10")
        self.label_58 = QtWidgets.QLabel(self.tab_3)
        self.label_58.setGeometry(QtCore.QRect(150, 380, 101, 16))
        self.label_58.setObjectName("label_58")
        self.PbBr2solventaddition_final_2 = QtWidgets.QTextBrowser(self.tab_3)
        self.PbBr2solventaddition_final_2.setGeometry(QtCore.QRect(150, 430, 61, 21))
        self.PbBr2solventaddition_final_2.setObjectName("PbBr2solventaddition_final_2")
        self.label_59 = QtWidgets.QLabel(self.tab_3)
        self.label_59.setGeometry(QtCore.QRect(10, 380, 60, 16))
        self.label_59.setObjectName("label_59")
        self.CsIweight_3 = QtWidgets.QLineEdit(self.tab_3)
        self.CsIweight_3.setGeometry(QtCore.QRect(10, 400, 61, 21))
        self.CsIweight_3.setObjectName("CsIweight_3")
        self.CsI_v_3 = QtWidgets.QTextBrowser(self.tab_3)
        self.CsI_v_3.setGeometry(QtCore.QRect(240, 460, 61, 21))
        self.CsI_v_3.setObjectName("CsI_v_3")
        self.label_60 = QtWidgets.QLabel(self.tab_3)
        self.label_60.setGeometry(QtCore.QRect(240, 440, 71, 20))
        self.label_60.setObjectName("label_60")
        self.label_61 = QtWidgets.QLabel(self.tab_3)
        self.label_61.setGeometry(QtCore.QRect(0, 460, 51, 21))
        self.label_61.setObjectName("label_61")
        self.PbBr2weight_2 = QtWidgets.QLineEdit(self.tab_3)
        self.PbBr2weight_2.setGeometry(QtCore.QRect(80, 400, 61, 21))
        self.PbBr2weight_2.setObjectName("PbBr2weight_2")
        self.label_62 = QtWidgets.QLabel(self.tab_3)
        self.label_62.setGeometry(QtCore.QRect(0, 430, 61, 21))
        self.label_62.setObjectName("label_62")
        self.PbBr2addition_2 = QtWidgets.QTextBrowser(self.tab_3)
        self.PbBr2addition_2.setGeometry(QtCore.QRect(150, 400, 61, 21))
        self.PbBr2addition_2.setObjectName("PbBr2addition_2")
        self.PbBr2solventvoladdition_2 = QtWidgets.QTextBrowser(self.tab_3)
        self.PbBr2solventvoladdition_2.setGeometry(QtCore.QRect(80, 430, 61, 21))
        self.PbBr2solventvoladdition_2.setObjectName("PbBr2solventvoladdition_2")
        self.label_63 = QtWidgets.QLabel(self.tab_3)
        self.label_63.setGeometry(QtCore.QRect(10, 500, 141, 20))
        self.label_63.setObjectName("label_63")
        self.CsPbI_v_mix_2 = QtWidgets.QTextBrowser(self.tab_3)
        self.CsPbI_v_mix_2.setGeometry(QtCore.QRect(10, 540, 61, 21))
        self.CsPbI_v_mix_2.setObjectName("CsPbI_v_mix_2")
        self.label_64 = QtWidgets.QLabel(self.tab_3)
        self.label_64.setGeometry(QtCore.QRect(10, 520, 61, 20))
        self.label_64.setObjectName("label_64")
        self.label_65 = QtWidgets.QLabel(self.tab_3)
        self.label_65.setGeometry(QtCore.QRect(90, 520, 71, 20))
        self.label_65.setObjectName("label_65")
        self.CsPbBr_v_mix_2 = QtWidgets.QTextBrowser(self.tab_3)
        self.CsPbBr_v_mix_2.setGeometry(QtCore.QRect(90, 540, 61, 21))
        self.CsPbBr_v_mix_2.setObjectName("CsPbBr_v_mix_2")
        self.label_66 = QtWidgets.QLabel(self.tab_3)
        self.label_66.setGeometry(QtCore.QRect(170, 520, 71, 20))
        self.label_66.setObjectName("label_66")
        self.DeviceCount_final_2 = QtWidgets.QTextBrowser(self.tab_3)
        self.DeviceCount_final_2.setGeometry(QtCore.QRect(170, 540, 61, 21))
        self.DeviceCount_final_2.setObjectName("DeviceCount_final_2")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.run_send_HTL = QtWidgets.QPushButton(self.tab_2)
        self.run_send_HTL.setGeometry(QtCore.QRect(150, 160, 141, 91))
        self.run_send_HTL.setObjectName("run_send_HTL")
        self.input_HTL_Device_Count = QtWidgets.QLineEdit(self.tab_2)
        self.input_HTL_Device_Count.setGeometry(QtCore.QRect(70, 80, 61, 21))
        self.input_HTL_Device_Count.setObjectName("input_HTL_Device_Count")
        self.input_HTL_vperdevice = QtWidgets.QLineEdit(self.tab_2)
        self.input_HTL_vperdevice.setGeometry(QtCore.QRect(150, 80, 61, 21))
        self.input_HTL_vperdevice.setObjectName("input_HTL_vperdevice")
        self.date_input_HTL = QtWidgets.QLineEdit(self.tab_2)
        self.date_input_HTL.setGeometry(QtCore.QRect(320, 490, 71, 21))
        self.date_input_HTL.setObjectName("date_input_HTL")
        self.note_input_HTL = QtWidgets.QLineEdit(self.tab_2)
        self.note_input_HTL.setGeometry(QtCore.QRect(450, 490, 41, 21))
        self.note_input_HTL.setObjectName("note_input_HTL")
        self.label_67 = QtWidgets.QLabel(self.tab_2)
        self.label_67.setGeometry(QtCore.QRect(330, 470, 61, 20))
        self.label_67.setObjectName("label_67")
        self.solutiontype_input_HTL = QtWidgets.QLineEdit(self.tab_2)
        self.solutiontype_input_HTL.setGeometry(QtCore.QRect(390, 490, 61, 21))
        self.solutiontype_input_HTL.setObjectName("solutiontype_input_HTL")
        self.savebutton_send_HTL = QtWidgets.QPushButton(self.tab_2)
        self.savebutton_send_HTL.setGeometry(QtCore.QRect(320, 510, 171, 20))
        self.savebutton_send_HTL.setObjectName("savebutton_send_HTL")
        self.label_68 = QtWidgets.QLabel(self.tab_2)
        self.label_68.setGeometry(QtCore.QRect(450, 470, 61, 20))
        self.label_68.setObjectName("label_68")
        self.label_69 = QtWidgets.QLabel(self.tab_2)
        self.label_69.setGeometry(QtCore.QRect(390, 470, 61, 20))
        self.label_69.setObjectName("label_69")
        self.savepath_HTL = QtWidgets.QTextBrowser(self.tab_2)
        self.savepath_HTL.setGeometry(QtCore.QRect(320, 530, 171, 31))
        self.savepath_HTL.setObjectName("savepath_HTL")
        self.label_34 = QtWidgets.QLabel(self.tab_2)
        self.label_34.setGeometry(QtCore.QRect(230, 290, 101, 16))
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.tab_2)
        self.label_35.setGeometry(QtCore.QRect(70, 290, 101, 16))
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.tab_2)
        self.label_36.setGeometry(QtCore.QRect(150, 60, 61, 16))
        self.label_36.setObjectName("label_36")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(70, 60, 60, 16))
        self.label_9.setObjectName("label_9")
        self.label_37 = QtWidgets.QLabel(self.tab_2)
        self.label_37.setGeometry(QtCore.QRect(230, 60, 71, 16))
        self.label_37.setObjectName("label_37")
        self.input_Spiro_weight = QtWidgets.QLineEdit(self.tab_2)
        self.input_Spiro_weight.setGeometry(QtCore.QRect(70, 310, 61, 21))
        self.input_Spiro_weight.setObjectName("input_Spiro_weight")
        self.display_HT_V_required = QtWidgets.QTextBrowser(self.tab_2)
        self.display_HT_V_required.setGeometry(QtCore.QRect(230, 80, 61, 21))
        self.display_HT_V_required.setObjectName("display_HT_V_required")
        self.display_HTL_soln_final = QtWidgets.QTextBrowser(self.tab_2)
        self.display_HTL_soln_final.setGeometry(QtCore.QRect(230, 310, 61, 21))
        self.display_HTL_soln_final.setObjectName("display_HTL_soln_final")
        self.display_HTL_CB_V = QtWidgets.QTextBrowser(self.tab_2)
        self.display_HTL_CB_V.setGeometry(QtCore.QRect(70, 360, 61, 21))
        self.display_HTL_CB_V.setObjectName("display_HTL_CB_V")
        self.label_38 = QtWidgets.QLabel(self.tab_2)
        self.label_38.setGeometry(QtCore.QRect(70, 340, 101, 16))
        self.label_38.setObjectName("label_38")
        self.label_70 = QtWidgets.QLabel(self.tab_2)
        self.label_70.setGeometry(QtCore.QRect(70, 390, 101, 16))
        self.label_70.setObjectName("label_70")
        self.display_HTL_LiTFSI_V = QtWidgets.QTextBrowser(self.tab_2)
        self.display_HTL_LiTFSI_V.setGeometry(QtCore.QRect(70, 410, 61, 21))
        self.display_HTL_LiTFSI_V.setObjectName("display_HTL_LiTFSI_V")
        self.label_71 = QtWidgets.QLabel(self.tab_2)
        self.label_71.setGeometry(QtCore.QRect(70, 440, 101, 16))
        self.label_71.setObjectName("label_71")
        self.display_HTL_TBP_V = QtWidgets.QTextBrowser(self.tab_2)
        self.display_HTL_TBP_V.setGeometry(QtCore.QRect(70, 460, 61, 21))
        self.display_HTL_TBP_V.setObjectName("display_HTL_TBP_V")
        self.label_72 = QtWidgets.QLabel(self.tab_2)
        self.label_72.setGeometry(QtCore.QRect(70, 120, 441, 16))
        self.label_72.setObjectName("label_72")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.input_PbI2_nomd = QtWidgets.QLineEdit(self.tab_5)
        self.input_PbI2_nomd.setGeometry(QtCore.QRect(20, 60, 61, 21))
        self.input_PbI2_nomd.setObjectName("input_PbI2_nomd")
        self.input_PbI2_nomM = QtWidgets.QLineEdit(self.tab_5)
        self.input_PbI2_nomM.setGeometry(QtCore.QRect(20, 140, 61, 21))
        self.input_PbI2_nomM.setObjectName("input_PbI2_nomM")
        self.input_FAI_nomM = QtWidgets.QLineEdit(self.tab_5)
        self.input_FAI_nomM.setGeometry(QtCore.QRect(20, 220, 61, 21))
        self.input_FAI_nomM.setObjectName("input_FAI_nomM")
        self.input_PbI2_ratio = QtWidgets.QLineEdit(self.tab_5)
        self.input_PbI2_ratio.setGeometry(QtCore.QRect(20, 300, 61, 21))
        self.input_PbI2_ratio.setObjectName("input_PbI2_ratio")
        self.input_FAI_ratio = QtWidgets.QLineEdit(self.tab_5)
        self.input_FAI_ratio.setGeometry(QtCore.QRect(20, 380, 61, 21))
        self.input_FAI_ratio.setObjectName("input_FAI_ratio")
        self.input_PbBr2_nomd = QtWidgets.QLineEdit(self.tab_5)
        self.input_PbBr2_nomd.setGeometry(QtCore.QRect(180, 60, 61, 21))
        self.input_PbBr2_nomd.setObjectName("input_PbBr2_nomd")
        self.input_MABr_nomM = QtWidgets.QLineEdit(self.tab_5)
        self.input_MABr_nomM.setGeometry(QtCore.QRect(180, 220, 61, 21))
        self.input_MABr_nomM.setObjectName("input_MABr_nomM")
        self.input_MABr_ratio = QtWidgets.QLineEdit(self.tab_5)
        self.input_MABr_ratio.setGeometry(QtCore.QRect(180, 380, 61, 21))
        self.input_MABr_ratio.setObjectName("input_MABr_ratio")
        self.input_PbBr2_nomM = QtWidgets.QLineEdit(self.tab_5)
        self.input_PbBr2_nomM.setGeometry(QtCore.QRect(180, 140, 61, 21))
        self.input_PbBr2_nomM.setObjectName("input_PbBr2_nomM")
        self.input_PbBr2_ratio = QtWidgets.QLineEdit(self.tab_5)
        self.input_PbBr2_ratio.setGeometry(QtCore.QRect(180, 300, 61, 21))
        self.input_PbBr2_ratio.setObjectName("input_PbBr2_ratio")
        self.label_11 = QtWidgets.QLabel(self.tab_5)
        self.label_11.setGeometry(QtCore.QRect(20, 40, 111, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_5)
        self.label_12.setGeometry(QtCore.QRect(20, 120, 111, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_5)
        self.label_13.setGeometry(QtCore.QRect(20, 200, 111, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_5)
        self.label_14.setGeometry(QtCore.QRect(20, 280, 111, 16))
        self.label_14.setObjectName("label_14")
        self.label_31 = QtWidgets.QLabel(self.tab_5)
        self.label_31.setGeometry(QtCore.QRect(20, 360, 111, 16))
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.tab_5)
        self.label_32.setGeometry(QtCore.QRect(180, 280, 111, 16))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.tab_5)
        self.label_33.setGeometry(QtCore.QRect(180, 200, 111, 16))
        self.label_33.setObjectName("label_33")
        self.label_88 = QtWidgets.QLabel(self.tab_5)
        self.label_88.setGeometry(QtCore.QRect(180, 120, 111, 16))
        self.label_88.setObjectName("label_88")
        self.label_85 = QtWidgets.QLabel(self.tab_5)
        self.label_85.setGeometry(QtCore.QRect(180, 40, 111, 16))
        self.label_85.setObjectName("label_85")
        self.label_86 = QtWidgets.QLabel(self.tab_5)
        self.label_86.setGeometry(QtCore.QRect(180, 360, 111, 16))
        self.label_86.setObjectName("label_86")
        self.label_87 = QtWidgets.QLabel(self.tab_5)
        self.label_87.setGeometry(QtCore.QRect(40, 440, 401, 81))
        self.label_87.setObjectName("label_87")
        self.label_89 = QtWidgets.QLabel(self.tab_5)
        self.label_89.setGeometry(QtCore.QRect(20, 410, 111, 16))
        self.label_89.setObjectName("label_89")
        self.input_FAPI_MAPI_ratio = QtWidgets.QLineEdit(self.tab_5)
        self.input_FAPI_MAPI_ratio.setGeometry(QtCore.QRect(20, 430, 61, 21))
        self.input_FAPI_MAPI_ratio.setObjectName("input_FAPI_MAPI_ratio")
        self.input_Final_M = QtWidgets.QLineEdit(self.tab_5)
        self.input_Final_M.setGeometry(QtCore.QRect(280, 430, 61, 21))
        self.input_Final_M.setObjectName("input_Final_M")
        self.label_90 = QtWidgets.QLabel(self.tab_5)
        self.label_90.setGeometry(QtCore.QRect(280, 410, 111, 16))
        self.label_90.setObjectName("label_90")
        self.label_91 = QtWidgets.QLabel(self.tab_5)
        self.label_91.setGeometry(QtCore.QRect(320, 40, 111, 16))
        self.label_91.setObjectName("label_91")
        self.input_solvent_ratio = QtWidgets.QLineEdit(self.tab_5)
        self.input_solvent_ratio.setGeometry(QtCore.QRect(320, 60, 61, 21))
        self.input_solvent_ratio.setObjectName("input_solvent_ratio")
        self.label_92 = QtWidgets.QLabel(self.tab_5)
        self.label_92.setGeometry(QtCore.QRect(150, 410, 111, 16))
        self.label_92.setObjectName("label_92")
        self.input_I_Br_ratio = QtWidgets.QLineEdit(self.tab_5)
        self.input_I_Br_ratio.setGeometry(QtCore.QRect(150, 430, 61, 21))
        self.input_I_Br_ratio.setObjectName("input_I_Br_ratio")
        self.label_73 = QtWidgets.QLabel(self.tab_5)
        self.label_73.setGeometry(QtCore.QRect(290, 200, 111, 16))
        self.label_73.setObjectName("label_73")
        self.input_CsI_nomM = QtWidgets.QLineEdit(self.tab_5)
        self.input_CsI_nomM.setGeometry(QtCore.QRect(290, 220, 61, 21))
        self.input_CsI_nomM.setObjectName("input_CsI_nomM")
        self.tabWidget.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 577, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "# Devices"))
        self.label_2.setText(_translate("MainWindow", "V/device"))
        self.savebutton_send.setText(_translate("MainWindow", "Save"))
        self.label_47.setText(_translate("MainWindow", "V Req"))
        self.solventdensity.setText(_translate("MainWindow", "0.96"))
        self.label_15.setText(_translate("MainWindow", "Solv_density"))
        self.PbI2deinsitycheck.setText(_translate("MainWindow", "1.5"))
        self.PbI2weight.setText(_translate("MainWindow", "1.2"))
        self.label_3.setText(_translate("MainWindow", "PbI2"))
        self.label_4.setText(_translate("MainWindow", "FAI"))
        self.label_17.setText(_translate("MainWindow", "FAPI V"))
        self.label_16.setText(_translate("MainWindow", "PbI2 to FAI"))
        self.label_21.setText(_translate("MainWindow", "Solv_add:"))
        self.FAIweight.setText(_translate("MainWindow", "0.3"))
        self.label_39.setText(_translate("MainWindow", "MABr"))
        self.MABrweight.setText(_translate("MainWindow", "0.06"))
        self.PbBr2deinsitycheck.setText(_translate("MainWindow", "1.4"))
        self.label_40.setText(_translate("MainWindow", "MAPBr V"))
        self.label_41.setText(_translate("MainWindow", "PbBr2 to MABr"))
        self.label_42.setText(_translate("MainWindow", "PbBr2"))
        self.PbBr2weight.setText(_translate("MainWindow", "0.5"))
        self.label_43.setText(_translate("MainWindow", "Solv_add:"))
        self.label_44.setText(_translate("MainWindow", "CsI V"))
        self.label_45.setText(_translate("MainWindow", "FAPI V"))
        self.label_46.setText(_translate("MainWindow", "MAPbr V"))
        self.DeviceCount.setText(_translate("MainWindow", "20"))
        self.Volumeperdevice.setText(_translate("MainWindow", "70"))
        self.run_send.setText(_translate("MainWindow", "Iterate"))
        self.label_49.setText(_translate("MainWindow", "# Devices"))
        self.label_22.setText(_translate("MainWindow", "Density:"))
        self.label_23.setText(_translate("MainWindow", "Density"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Weight = gram, Volume = microliter, Density = g/mL"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "1. Click Initilize"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "2. Adjust # Device & V/device"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "3. Adjust organic precursor weights until desired # Devices"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "4. Create a 9:1 DMF:DMSO solvent vial with displayed amount of solvent + 0.5mL"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "5. Adjust lead salt precursor weight until amount in solution is greater than amount to put into FAI by 300uL"))
        item = self.listWidget.item(6)
        item.setText(_translate("MainWindow", "6. Density check the lead salt solution and input the value"))
        item = self.listWidget.item(7)
        item.setText(_translate("MainWindow", "7. Amount of lead salt solution to put into organic precusor is displayed"))
        item = self.listWidget.item(8)
        item.setText(_translate("MainWindow", "8. Amount of solvent solution to add into the organic precursor is displayed"))
        item = self.listWidget.item(9)
        item.setText(_translate("MainWindow", "9. Use the solution optimizer to make the final mixture"))
        item = self.listWidget.item(10)
        item.setText(_translate("MainWindow", "10. Save your data"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_19.setText(_translate("MainWindow", "Solv_volume"))
        self.label_20.setText(_translate("MainWindow", "How to use:"))
        self.label_50.setText(_translate("MainWindow", "Date"))
        self.date_input.setText(_translate("MainWindow", "20200101"))
        self.solutiontype_input.setText(_translate("MainWindow", "BL"))
        self.note_input.setText(_translate("MainWindow", "ABC"))
        self.label_51.setText(_translate("MainWindow", "Type"))
        self.label_52.setText(_translate("MainWindow", "Note"))
        self.label_48.setText(_translate("MainWindow", "FINAL SOLUTION:"))
        self.label_27.setText(_translate("MainWindow", "Solv_d_target"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Hybrid-PSK"))
        self.label_18.setText(_translate("MainWindow", "Solv_density"))
        self.PbI2weight_2.setText(_translate("MainWindow", "1.2"))
        self.label_24.setText(_translate("MainWindow", "Solv_volume"))
        self.label_25.setText(_translate("MainWindow", "Density:"))
        self.label_5.setText(_translate("MainWindow", "# Devices"))
        self.solventdensity_2.setText(_translate("MainWindow", "0.96"))
        self.run_send_2.setText(_translate("MainWindow", "Iterate"))
        self.label_26.setText(_translate("MainWindow", "Solv_add:"))
        self.Volumeperdevice_2.setText(_translate("MainWindow", "45"))
        self.PbI2deinsitycheck_2.setText(_translate("MainWindow", "1.5"))
        self.DeviceCount_2.setText(_translate("MainWindow", "20"))
        self.label_6.setText(_translate("MainWindow", "V/device"))
        self.label_53.setText(_translate("MainWindow", "V Req"))
        self.label_7.setText(_translate("MainWindow", "PbI2"))
        self.label_28.setText(_translate("MainWindow", "Solv_d_target"))
        self.label_8.setText(_translate("MainWindow", "CsI"))
        self.CsIweight_2.setText(_translate("MainWindow", "0.3"))
        self.label_29.setText(_translate("MainWindow", "CsPbI3 V"))
        self.label_30.setText(_translate("MainWindow", "PbI2 to CsI"))
        self.note_input_2.setText(_translate("MainWindow", "ABC"))
        self.label_54.setText(_translate("MainWindow", "Date"))
        self.savebutton_send_2.setText(_translate("MainWindow", "Save"))
        self.label_55.setText(_translate("MainWindow", "Type"))
        self.solutiontype_input_2.setText(_translate("MainWindow", "BL"))
        self.label_56.setText(_translate("MainWindow", "Note"))
        self.date_input_2.setText(_translate("MainWindow", "20200101"))
        self.label_57.setText(_translate("MainWindow", "How to use:"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("MainWindow", "Weight = gram, Volume = microliter, Density = g/mL"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("MainWindow", "1. Click Initilize"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("MainWindow", "2. Adjust # Device & V/device"))
        item = self.listWidget_2.item(3)
        item.setText(_translate("MainWindow", "3. Adjust organic precursor weights until desired # Devices"))
        item = self.listWidget_2.item(4)
        item.setText(_translate("MainWindow", "4. Create a user specifid ratio of DMF:DMSO solvent vial with displayed amount of solvent + 0.5mL"))
        item = self.listWidget_2.item(5)
        item.setText(_translate("MainWindow", "5. Adjust lead salt precursor weight until amount in solution is greater than amount to put into CsI by 300uL"))
        item = self.listWidget_2.item(6)
        item.setText(_translate("MainWindow", "6. Density check the lead salt solution and input the value"))
        item = self.listWidget_2.item(7)
        item.setText(_translate("MainWindow", "7. Amount of lead salt solution to put into organic precusor is displayed"))
        item = self.listWidget_2.item(8)
        item.setText(_translate("MainWindow", "8. Amount of solvent solution to add into the organic precursor is displayed"))
        item = self.listWidget_2.item(9)
        item.setText(_translate("MainWindow", "9. Use the solution optimizer to make the final mixture"))
        item = self.listWidget_2.item(10)
        item.setText(_translate("MainWindow", "10. Save your data"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.PbBr2deinsitycheck_2.setText(_translate("MainWindow", "1.4"))
        self.label_10.setText(_translate("MainWindow", "PbBr2"))
        self.label_58.setText(_translate("MainWindow", "PbBr2 to CsI"))
        self.label_59.setText(_translate("MainWindow", "CsI"))
        self.CsIweight_3.setText(_translate("MainWindow", "0.1"))
        self.label_60.setText(_translate("MainWindow", "CsPbBr3 V"))
        self.label_61.setText(_translate("MainWindow", "Density:"))
        self.PbBr2weight_2.setText(_translate("MainWindow", "0.5"))
        self.label_62.setText(_translate("MainWindow", "Solv_add:"))
        self.label_63.setText(_translate("MainWindow", "FINAL SOLUTION:"))
        self.label_64.setText(_translate("MainWindow", "CsPbI3 V"))
        self.label_65.setText(_translate("MainWindow", "CsPbBr3 V"))
        self.label_66.setText(_translate("MainWindow", "# Devices"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "In-PSK"))
        self.run_send_HTL.setText(_translate("MainWindow", "Iterate"))
        self.input_HTL_Device_Count.setText(_translate("MainWindow", "20"))
        self.input_HTL_vperdevice.setText(_translate("MainWindow", "70"))
        self.date_input_HTL.setText(_translate("MainWindow", "20200101"))
        self.note_input_HTL.setText(_translate("MainWindow", "ABC"))
        self.label_67.setText(_translate("MainWindow", "Date"))
        self.solutiontype_input_HTL.setText(_translate("MainWindow", "BL"))
        self.savebutton_send_HTL.setText(_translate("MainWindow", "Save"))
        self.label_68.setText(_translate("MainWindow", "Note"))
        self.label_69.setText(_translate("MainWindow", "Type"))
        self.label_34.setText(_translate("MainWindow", "V Solution"))
        self.label_35.setText(_translate("MainWindow", "Grams of Spiro"))
        self.label_36.setText(_translate("MainWindow", "V/Device"))
        self.label_9.setText(_translate("MainWindow", "# Devices"))
        self.label_37.setText(_translate("MainWindow", "V Required"))
        self.input_Spiro_weight.setText(_translate("MainWindow", "0.11"))
        self.label_38.setText(_translate("MainWindow", "CB V"))
        self.label_70.setText(_translate("MainWindow", "LiTFSI V"))
        self.label_71.setText(_translate("MainWindow", "TBP V"))
        self.label_72.setText(_translate("MainWindow", "Iterate on mass of Spiro until V Solution > V Required"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Spiro"))
        self.input_PbI2_nomd.setText(_translate("MainWindow", "1.44"))
        self.input_PbI2_nomM.setText(_translate("MainWindow", "1.5"))
        self.input_FAI_nomM.setText(_translate("MainWindow", "1.22"))
        self.input_PbI2_ratio.setText(_translate("MainWindow", "1.09"))
        self.input_FAI_ratio.setText(_translate("MainWindow", "1"))
        self.input_PbBr2_nomd.setText(_translate("MainWindow", "1.42"))
        self.input_MABr_nomM.setText(_translate("MainWindow", "1.22"))
        self.input_MABr_ratio.setText(_translate("MainWindow", "1"))
        self.input_PbBr2_nomM.setText(_translate("MainWindow", "1.5"))
        self.input_PbBr2_ratio.setText(_translate("MainWindow", "1.09"))
        self.label_11.setText(_translate("MainWindow", "PbI2_nomd"))
        self.label_12.setText(_translate("MainWindow", "PbI2_nomM"))
        self.label_13.setText(_translate("MainWindow", "FAI_nomM"))
        self.label_14.setText(_translate("MainWindow", "PbI2_ratio"))
        self.label_31.setText(_translate("MainWindow", "FAI_ratio"))
        self.label_32.setText(_translate("MainWindow", "PbBr2_ratio"))
        self.label_33.setText(_translate("MainWindow", "MABr_nomM"))
        self.label_88.setText(_translate("MainWindow", "PbBr2_nomM"))
        self.label_85.setText(_translate("MainWindow", "PbBr2_nomd"))
        self.label_86.setText(_translate("MainWindow", "MABr_ratio"))
        self.label_87.setText(_translate("MainWindow", "Don\'t change these, unless you know what youre doing!"))
        self.label_89.setText(_translate("MainWindow", "FAPI_MAPBr_ratio"))
        self.input_FAPI_MAPI_ratio.setText(_translate("MainWindow", "5"))
        self.input_Final_M.setText(_translate("MainWindow", "1.5"))
        self.label_90.setText(_translate("MainWindow", "Intended Soln M"))
        self.label_91.setText(_translate("MainWindow", "DMF_DMSO_Ratio"))
        self.input_solvent_ratio.setText(_translate("MainWindow", "9"))
        self.label_92.setText(_translate("MainWindow", "I3 to Br3 ratio"))
        self.input_I_Br_ratio.setText(_translate("MainWindow", "5"))
        self.label_73.setText(_translate("MainWindow", "CsI_nomM"))
        self.input_CsI_nomM.setText(_translate("MainWindow", "1.5"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Advanced Settings"))


############################
# GUI Functionality 
############################


############################
# Initial Constants
############################

######### Constants to preload, not sure if float is necessary 

######### PSK
        #Density g/mL constants
        # self.DMFDMSO_d = float(0.9596)
        self.DMF_d = float(0.944)
        self.DMSO_d = float(1.1)
        self.PbI2_d = float(6.16)                
        self.PbBr2_d = float(6.6)

        #Moleular weight constants
        self.DMF_mw = float(73.09)
        self.DMSO_mw = float(78.13)
        self.PbI2_mw = float(461.01)
        self.MABr_mw = float(111.97)
        self.CsI_mw = float(259.81)
        self.FAI_mw = float(171.97)
        self.PbBr2_mw = float(367.01)

        #Preload a date display
        self.now = str(QDate.currentDate()) 
        self.datevalue.setText(str(self.now))

############################
# Triggers
############################

######### Triggers section: Runs a defined function when signal is fired (button clicked)

####### Hybrid_PSK
        #iterate button
        self.run_send.clicked.connect(self.function_0)
        self.run_send.clicked.connect(self.function_1)
        self.run_send.clicked.connect(self.function_2)
        self.run_send.clicked.connect(self.function_3)
        self.run_send.clicked.connect(self.function_4)
        self.run_send.clicked.connect(self.function_5)
        self.run_send.clicked.connect(self.function_6)
        #save button
        self.savebutton_send.clicked.connect(self.function_7)

###### Inorganic_PSK
        #iterate button
        self.run_send_2.clicked.connect(self.function_0)
        self.run_send_2.clicked.connect(self.function_12)
        self.run_send_2.clicked.connect(self.function_13)
        self.run_send_2.clicked.connect(self.function_14)
        self.run_send_2.clicked.connect(self.function_15)



####### HTL 
        #iterate button
        self.run_send_HTL.clicked.connect(self.function_8)
        self.run_send_HTL.clicked.connect(self.function_9)
        self.run_send_HTL.clicked.connect(self.function_10)
        #save button
        self.savebutton_send_HTL.clicked.connect(self.function_11)

############################
# Functions
############################

######### PSK
    def function_0(self): #Initialize nominals & ratios
            #FAPI solution constants
            self.ratio = float(self.input_FAPI_MAPI_ratio.text())
            self.IBr_ratio = float(self.input_I_Br_ratio.text())

            self.PbI2_nomd = float(self.input_PbI2_nomd.text())
            self.PbI2_nomM = float(self.input_PbI2_nomM.text())
            self.FAI_nomM = float(self.input_FAI_nomM.text())
            self.PbI2_ratio = float(self.input_PbI2_ratio.text())
            self.FAI_ratio = float(self.input_FAI_ratio.text())

            #MAPBr solution constants
            self.PbBr2_nomd = float(self.input_PbBr2_nomd.text())
            self.PbBr2_nomM = float(self.input_PbBr2_nomM.text())
            self.MABr_nomM = float(self.input_MABr_nomM.text())
            self.PbBr2_ratio = float(self.input_PbBr2_ratio.text())
            self.MABr_ratio = float(self.input_MABr_ratio.text())
            self.Solvent_ratio = float(self.input_solvent_ratio.text())

            self.CsI_nomM = float(self.input_CsI_nomM.text())

            

    def function_1(self): #Initial volume calculation
            self.Count = float(self.DeviceCount.text())
            self.V_cell = float(self.Volumeperdevice.text())
            self.V_batch = self.Count * self.V_cell
            self.FAPI_final = self.V_batch * (5/6)
            self.MAPBr_final = self.V_batch * (1/6)
            self.V_Cs=(0.05/0.95)*self.V_batch
            #calculate target solvent density

            self.DMFDMSO_d = (self.Solvent_ratio/(self.Solvent_ratio+1))*self.DMF_d + (1)/(self.Solvent_ratio+1)*self.DMSO_d
            #send calculated values to these fields 
            self.totalvolumeoutput.setText(str(self.V_batch))
            self.totalvolumeoutput_2.setText(str(self.V_batch))

            self.solvent_target_output.setText(str(self.DMFDMSO_d))
            self.solvent_target_output_2.setText(str(self.DMFDMSO_d))

            # self.initialFAPI_V.setText(str(round(self.FAPI_final,2)))
            # self.initialMAPBr_V.setText(str(round(self.MAPBr_final,2)))
            # self.CsI_v_mix_2.setText(str(round(self.V_Cs,2)))


    def function_2(self): #FAPI calculation 
            #store user inputs into variables
            self.PbI2_w = float(self.PbI2weight.text())
            self.FAI_w = float(self.FAIweight.text())
            self.PbI2_d = float(self.PbI2deinsitycheck.text())
            self.Solv_d = float(self.solventdensity.text())

            #calculate value
            self.Solv_v_PbI2 = (self.PbI2_w/self.PbI2_mw)/self.PbI2_nomM*1000000
            self.Solv_w_PbI2 = (self.Solv_v_PbI2/1000)*self.Solv_d
            self.PbI2_mol = self.PbI2_w / self.PbI2_mw
            self.PbI2_soln_w = self.PbI2_w + self.Solv_w_PbI2
            self.PrecurV_PbI2_display = (self.PbI2_soln_w / self.PbI2_d)*1000
            self.PrecurV_PbI2 = (self.PbI2_soln_w / self.PbI2_d)/1000
            self.PbI2_M = self.PbI2_mol / self.PrecurV_PbI2
            self.FAI_mol = self.FAI_w/self.FAI_mw
            self.PbI2_soln_V_to_FAI = 1000000*(self.FAI_mol * self.PbI2_ratio)/self.PbI2_M
            self.Solv_addition_FAPI = ((self.FAI_mol / self.FAI_nomM) * 1000000 ) - self.PbI2_soln_V_to_FAI
            self.FAPI_vol = self.PbI2_soln_V_to_FAI + self.Solv_addition_FAPI

            #send calculated values to these fields
            self.PbI2solventvoladdition.setText(str(round(self.Solv_v_PbI2 - 50,2))) 
            self.PbI2addition.setText(str(round(self.PbI2_soln_V_to_FAI,2)))
            self.PbI2solventaddition_final.setText(str(round(self.Solv_addition_FAPI,2)))
            self.FAPI_v.setText(str(round(self.FAPI_vol,2)))

    def function_3(self): #MAPBr calculation
            self.PbBr2_w = float(self.PbBr2weight.text())
            self.MABr_w = float(self.MABrweight.text())
            self.PbBr2_d = float(self.PbBr2deinsitycheck.text()) 
            # self.Solv_d = float(self.solventdensity.text())

            #calculate value
            self.Solv_v_PbBr2 = (self.PbBr2_w/self.PbBr2_mw)/self.PbBr2_nomM*1000000
            self.Solv_w_PbBr2 = (self.Solv_v_PbBr2/1000)*self.Solv_d
            self.PbBr2_mol = self.PbBr2_w / self.PbBr2_mw
            self.PbBr2_soln_w = self.PbBr2_w + self.Solv_w_PbBr2

            self.PrecurV_PbBr2_display = (self.PbBr2_soln_w / self.PbBr2_d)*1000
            self.PrecurV_PbBr2 = (self.PbBr2_soln_w / self.PbBr2_d)/1000
            self.PbBr2_M = self.PbBr2_mol / self.PrecurV_PbBr2
            self.MABr_mol = self.MABr_w/self.MABr_mw
            self.PbBr2_soln_V_to_MABr = 1000000*(self.MABr_mol * self.PbBr2_ratio)/self.PbBr2_M
            self.Solv_addition_MAPBr = ((self.MABr_mol / self.MABr_nomM) * 1000000 ) - self.PbBr2_soln_V_to_MABr
            self.MAPBr_vol = self.PbBr2_soln_V_to_MABr + self.Solv_addition_MAPBr

            #send calculated values to these fields
            self.PbBr2solventvoladdition.setText(str(round(self.Solv_v_PbBr2 - 50,2))) 
            self.PbBr2addition.setText(str(round(self.PbBr2_soln_V_to_MABr,2)))
            self.PbBr2solventaddition_final.setText(str(round(self.Solv_addition_MAPBr,2)))
            self.MAPBr_v.setText(str(round(self.MAPBr_vol,2)))

    def function_4(self): #Total solvent calculation
            #user input
            self.solv_density = float(self.solventdensity.text())

            #calculate a value
            self.totalsolv_vol = self.Solv_addition_FAPI + self.Solv_v_PbI2 + self.Solv_addition_MAPBr + self.Solv_v_PbBr2

            #send calculated value to these fields
            self.solventtotalvolume.setText(str(round(self.totalsolv_vol,2)))

    def function_5(self): #Solution optimizer
            if self.MAPBr_vol * self.ratio < self.FAPI_vol:
                self.maxFAPI_vol = self.MAPBr_vol * self.ratio
                self.maxMAPBr_vol = self.MAPBr_vol
            
            if self.MAPBr_vol * self.ratio > self.FAPI_vol:
                self.maxFAPI_vol = self.FAPI_vol
                self.maxMAPBr_vol = self.maxFAPI_vol / self.ratio


            self.FAPI_v_mix.setText(str(round(self.maxFAPI_vol,2)))
            self.MAPBr_v_mix.setText(str(round(self.maxMAPBr_vol,2)))
            self.V_Cs_mix=(0.05/0.95) * (self.maxFAPI_vol + self.maxMAPBr_vol)
            self.CsI_v_mix.setText(str(round(self.V_Cs_mix,2)))
            self.PSK_total_vol = self.V_Cs_mix + self.maxMAPBr_vol + self.maxFAPI_vol
            self.DeviceCnt_final = self.PSK_total_vol / self.V_cell
            self.DeviceCount_final.setText(str(round(self.DeviceCnt_final,2)))

    def function_6(self, fineName): #Store variables to dataframe
        #variables in data frame format
        self.storage = {'Date':[self.now],
                        'Count':[self.Count], 
                        'V_cell uL':[self.V_cell],
                        'Solv_d g/mL':[self.Solv_d],
                        'totalsolv_vol':[self.totalsolv_vol],
                                #user inputs FAPI
                        'PbI2_w g':[self.PbI2_w], 
                        'FAI_w':[self.FAI_w],
                        'PbI2_d':[self.PbI2_d],
                                #calculated variables FAPI
                        'Solv_v_PbI2':[self.Solv_v_PbI2],
                        'Solv_w_PbI2':[self.Solv_w_PbI2],
                        'PbI2_mol':[self.PbI2_mol],
                        'PbI2_soln_w':[self.PbI2_soln_w],
                        'PrecurV_PbI2_display':[self.PrecurV_PbI2_display],
                        'PrecurV_PbI2':[self.PrecurV_PbI2],
                        'PbI2_M':[self.PbI2_M],
                        'FAI_mol':[self.FAI_mol],
                        'PbI2_soln_V_to_FAI':[self.PbI2_soln_V_to_FAI],
                        'Solv_addition_FAPI':[self.Solv_addition_FAPI],
                        'FAPI_vol':[self.FAPI_vol],
                                
                                #user inputs MAPBr
                        'PbBr2_w':[self.PbBr2_w], 
                        'MABr_w':[self.MABr_w],
                        'PbBr2_d':[self.PbBr2_d],
                        #calculated variables MAPBr
                        'Solv_v_PbBr2':[self.Solv_v_PbBr2],
                        'Solv_w_PbBr2':[self.Solv_w_PbBr2],
                        'PbBr2_mol':[self.PbBr2_mol],
                        'PbBr2_soln_w':[self.PbBr2_soln_w], 
                        'PrecurV_PbBr2_display':[self.PrecurV_PbBr2_display],
                        'PrecurV_PbBr2':[self.PrecurV_PbBr2],
                        'PbBr2_M':[self.PbBr2_M],
                        'MABr_mol':[self.MABr_mol],
                        'PbBr2_soln_V_to_MABr':[self.PbBr2_soln_V_to_MABr],
                        'Solv_addition_MAPBr':[self.Solv_addition_MAPBr],
                        'MAPBr_vol':[self.MAPBr_vol],

                        #solution optimizer values
                        'maxFAPI_vol':[self.maxFAPI_vol],
                        'maxMAPBr_vol':[self.maxMAPBr_vol],
                        'V_Cs_mix':[self.V_Cs_mix],
                        'DeviceCnt_final':[self.DeviceCnt_final],
                        # constants
                        #Density g/mL constants
                        'DMFDMSO_d':[self.DMFDMSO_d],
                        'DMF_d':[self.DMF_d],
                        'DMSO_d':[self.DMSO_d],
                        'PbI2_d':[self.PbI2_d],
                        'PbBr2_d':[self.PbBr2_d],

                        #Moleular weight constants
                        'DMF_mw':[self.DMF_mw],
                        'DMSO_mw':[self.DMSO_mw],
                        'PbI2_mw':[self.PbI2_mw],
                        'MABr_mw':[self.MABr_mw],
                        'CsI_mw':[self.CsI_mw],
                        'FAI_mw':[self.FAI_mw],
                        'PbBr2_mw':[self.PbBr2_mw],

                        #FAPI solution constants
                        'PbI2_nomd':[self.PbI2_nomd],
                        'PbI2_nomM':[self.PbI2_nomM],
                        'FAI_nomM':[self.FAI_nomM],
                        'PbI2_ratio':[self.PbI2_ratio],
                        'FAI_ratio':[self.FAI_ratio],

                        #MAPBr solution constants
                        'PbBr2_nomd':[self.PbBr2_nomd],
                        'PbBr2_nomM':[self.PbBr2_nomM],
                        'MABr_nomM':[self.MABr_nomM],
                        'PbBr2_ratio':[self.PbBr2_ratio],
                        'MABr_ratio':[self.MABr_ratio],
                        'FAPI_MAPI_ratio':[self.ratio]}

        self.storageframe = pd.DataFrame(self.storage)
        # self.arrayconfirm.setText('Array Built!')

        # print(self.storage)
        # print(self.storageframe)

    def function_7(self): #Saving data to csv
        newdata = self.storageframe
        #if the file doenst exist yet include headers, if not exdlude
        with open('PSK_MV_Calc_Data.csv', 'a') as f:

            if f.tell() == 0:
                newdata.to_csv(f, header=True)

            else:
                newdata.to_csv(f, header=False)

        #for troubleshooting: this counts the number of rows in csv
        with open('PSK_MV_Calc_Data.csv', 'r') as f:
            row_count = sum(1 for row in f) - 1       


        date = self.date_input.text() 
        solutiontype = self.solutiontype_input.text()
        usernote = self.note_input.text()
        filename = '{0}_{1}_{2}.csv'.format(date, solutiontype, usernote)

        with open(filename, 'a') as f:
            if f.tell() == 0:
                newdata.to_csv(f, header=True)

            else:
                newdata.to_csv(f, header=False)


        self.savepath.setText(str(row_count) + ' Entries in document!')

######### Inorganic_PSK
    def function_12(self): #Initial volume calculation
            self.DMFDMSO_d = (self.Solvent_ratio/(self.Solvent_ratio+1))*self.DMF_d + (1)/(self.Solvent_ratio+1)*self.DMSO_d
            self.Count = float(self.DeviceCount_2.text())
            self.V_cell = float(self.Volumeperdevice_2.text())
            self.V_batch = self.Count * self.V_cell

            #send calculated values to these fields 
            self.totalvolumeoutput_2.setText(str(self.V_batch))
            self.solvent_target_output_2.setText(str(self.DMFDMSO_d))    

    def function_13(self): # PbI2 solvent calculation
            #store user inputs into variables
            self.PbI2_w = float(self.PbI2weight_2.text())
            self.CsI_w = float(self.CsIweight_2.text()) 
            self.PbI2_d = float(self.PbI2deinsitycheck_2.text())
            self.Solv_d = float(self.solventdensity_2.text())


            #calculate value
            self.CsI_mol = self.CsI_w/self.CsI_mw
            self.PbI2_mol = self.PbI2_w / self.PbI2_mw
            self.Solv_v_PbI2_variable = (self.PbI2_mol)/self.PbI2_nomM  # solvent V add to PbI2 in Liter
            self.Solv_v_PbI2_display = (self.PbI2_mol)/self.PbI2_nomM*1000000 # solvent V add to PbI2 in µL
            self.Solv_w_PbI2 = self.Solv_d*1000 * self.Solv_v_PbI2_variable #weight of the solvent in gram
            self.PbI2_soln_w = self.PbI2_w + self.Solv_w_PbI2 # weight of solvent + weight of powder
            self.PrecurV_PbI2 = (self.PbI2_soln_w / self.PbI2_d)/1000 # Solution volume in L
            self.PbI2_expanded_M =  self.PbI2_mol   / self.PrecurV_PbI2 # new concentration will be lower in mol/L
            self.PbI2_soln_V_to_CsI = 1000000*(self.CsI_mol * self.PbI2_ratio)/self.PbI2_expanded_M #in µL

            # I dont understand purpose of this line:
            # self.Solv_addition_CsI = ((self.CsI_mol / self.CsI_nomM) * 1000000 ) - self.PbI2_soln_V_to_CsI
            # self.PbI2solventaddition_final_2.setText(str(round(self.Solv_addition_CsI,2)))

            self.CsI_M = self.CsI_mol/self.PbI2_soln_V_to_CsI*1000000
            self.CsPbI_vol = self.PbI2_soln_V_to_CsI #+ self.Solv_addition_CsI

            #send calculated values to these fields
            self.PbI2solventvoladdition_2.setText(str(round(self.Solv_v_PbI2_display,2)))
            self.PbI2addition_2.setText(str(round(self.PbI2_soln_V_to_CsI,2)))
            self.CsI_v_2.setText(str(round(self.CsPbI_vol,2)))

            print('Real Molarity of PbI2= '+ str(round(self.PbI2_expanded_M,2)))
            print('nominal CsI_M= '+ str(round(self.CsI_M,2)))
            print('final volume in µL= '+ str(round(self.PrecurV_PbI2*1e6,2)))
            

    def function_14(self): # PbBr2 solvent calculation ( need to update mirror func_13)
            #store user inputs into variables
            self.PbBr2_w = float(self.PbBr2weight_2.text())
            self.CsI_w_2 = float(self.CsIweight_3.text()) 
            self.PbBr2_d = float(self.PbBr2deinsitycheck_2.text())
            self.Solv_d = float(self.solventdensity_2.text())


            #calculate value
            self.CsI_mol_2 = self.CsI_w_2/self.CsI_mw
            self.PbBr2_mol = self.PbBr2_w / self.PbBr2_mw
            self.Solv_v_PbBr2_variable = (self.PbBr2_mol)/self.PbBr2_nomM  # solvent V add to PbBr2 in Liter
            self.Solv_v_PbBr2_display = (self.PbBr2_mol)/self.PbBr2_nomM*1000000 # solvent V add to PbBr2 in µL
            self.Solv_w_PbBr2 = self.Solv_d*1000 * self.Solv_v_PbBr2_variable #weight of the solvent in gram
            self.PbBr2_soln_w = self.PbBr2_w + self.Solv_w_PbBr2 # weight of solvent + weight of powder
            self.PrecurV_PbBr2 = (self.PbBr2_soln_w / self.PbBr2_d)/1000 # Solution volume in L
            self.PbBr2_expanded_M =  self.PbBr2_mol   / self.PrecurV_PbBr2 # new concentration will be lower in mol/L
            self.PbBr2_soln_V_to_CsI = 1000000*(self.CsI_mol_2 * self.PbBr2_ratio)/self.PbBr2_expanded_M #in µL

            # Br dont understand purpose of this line:
            # self.Solv_addition_CsBr = ((self.CsBr_mol / self.CsBr_nomM) * 1000000 ) - self.PbBr2_soln_V_to_CsBr
            # self.PbBr2solventaddition_final_2.setText(str(round(self.Solv_addition_CsBr,2)))

            self.CsI_M_2 = self.CsI_mol_2/self.PbBr2_soln_V_to_CsI*1000000
            self.CsPbBr_vol = self.PbBr2_soln_V_to_CsI #+ self.Solv_addition_CsBr

            #send calculated values to these fields
            self.PbBr2solventvoladdition_2.setText(str(round(self.Solv_v_PbBr2_display,2)))
            self.PbBr2addition_2.setText(str(round(self.PbBr2_soln_V_to_CsI,2)))
            self.CsI_v_3.setText(str(round(self.CsPbBr_vol,2)))

            print('Real Molarity of PbBr2= '+ str(round(self.PbBr2_expanded_M,2)))
            print('nominal CsBr_M= '+ str(round(self.CsI_M_2,2)))
            print('final volume in µL= '+ str(round(self.PrecurV_PbBr2*1e6,2)))


    def function_15(self): #Solution optimizer
            if self.CsPbBr_vol * self.IBr_ratio < self.CsPbI_vol:
                self.maxCsPbI_vol = self.CsPbBr_vol * self.IBr_ratio
                self.maxCsPbBr_vol = self.CsPbBr_vol
            
            if self.CsPbBr_vol * self.IBr_ratio > self.CsPbI_vol:
                self.maxCsPbI_vol = self.CsPbI_vol
                self.maxCsPbBr_vol = self.maxCsPbI_vol / self.IBr_ratio


            self.CsPbI_v_mix_2.setText(str(round(self.maxCsPbI_vol,2)))
            self.CsPbBr_v_mix_2.setText(str(round(self.maxCsPbBr_vol,2)))

            # keep for adding MACl Later on
            # self.V_Cs_mix=(0.05/0.95) * (self.maxFAPI_vol + self.maxMAPBr_vol)
            # self.CsI_v_mix.setText(str(round(self.V_Cs_mix,2)))

            self.PSK_total_vol_2 = self.maxCsPbBr_vol + self.maxCsPbI_vol
            self.DeviceCnt_final_2 = self.PSK_total_vol_2 / self.V_cell
            self.DeviceCount_final_2.setText(str(round(self.DeviceCnt_final_2,2)))


    def function_16(self, fineName): #Store variables to dataframe
        #variables in data frame format
        self.storage = {'Date':[self.now],
                        'Count':[self.Count], 
                        'V_cell uL':[self.V_cell],
                        'Solv_d g/mL':[self.Solv_d],
                        'totalsolv_vol':[self.totalsolv_vol],

                                #user inputs FAPI
                        'PbI2_w g':[self.PbI2_w], 
                        'FAI_w':[self.FAI_w],
                        'PbI2_d':[self.PbI2_d],

                                #calculated variables FAPI
                        'Solv_v_PbI2':[self.Solv_v_PbI2],
                        'Solv_w_PbI2':[self.Solv_w_PbI2],
                        'PbI2_mol':[self.PbI2_mol],
                        'PbI2_soln_w':[self.PbI2_soln_w],
                        'PrecurV_PbI2_display':[self.PrecurV_PbI2_display],
                        'PrecurV_PbI2':[self.PrecurV_PbI2],
                        'PbI2_M':[self.PbI2_M],
                        'FAI_mol':[self.FAI_mol],
                        'PbI2_soln_V_to_FAI':[self.PbI2_soln_V_to_FAI],
                        'Solv_addition_FAPI':[self.Solv_addition_FAPI],
                        'FAPI_vol':[self.FAPI_vol],
                                
                                #user inputs MAPBr
                        'PbBr2_w':[self.PbBr2_w], 
                        'MABr_w':[self.MABr_w],
                        'PbBr2_d':[self.PbBr2_d],

                        #calculated variables MAPBr
                        'Solv_v_PbBr2':[self.Solv_v_PbBr2],
                        'Solv_w_PbBr2':[self.Solv_w_PbBr2],
                        'PbBr2_mol':[self.PbBr2_mol],
                        'PbBr2_soln_w':[self.PbBr2_soln_w], 
                        'PrecurV_PbBr2_display':[self.PrecurV_PbBr2_display],
                        'PrecurV_PbBr2':[self.PrecurV_PbBr2],
                        'PbBr2_M':[self.PbBr2_M],
                        'MABr_mol':[self.MABr_mol],
                        'PbBr2_soln_V_to_MABr':[self.PbBr2_soln_V_to_MABr],
                        'Solv_addition_MAPBr':[self.Solv_addition_MAPBr],
                        'MAPBr_vol':[self.MAPBr_vol],

                        #solution optimizer values
                        'maxFAPI_vol':[self.maxFAPI_vol],
                        'maxMAPBr_vol':[self.maxMAPBr_vol],
                        'V_Cs_mix':[self.V_Cs_mix],
                        'DeviceCnt_final':[self.DeviceCnt_final],
                        # constants
                        #Density g/mL constants
                        'DMFDMSO_d':[self.DMFDMSO_d],
                        'DMF_d':[self.DMF_d],
                        'DMSO_d':[self.DMSO_d],
                        'PbI2_d':[self.PbI2_d],
                        'PbBr2_d':[self.PbBr2_d],

                        #Moleular weight constants
                        'DMF_mw':[self.DMF_mw],
                        'DMSO_mw':[self.DMSO_mw],
                        'PbI2_mw':[self.PbI2_mw],
                        'MABr_mw':[self.MABr_mw],
                        'CsI_mw':[self.CsI_mw],
                        'FAI_mw':[self.FAI_mw],
                        'PbBr2_mw':[self.PbBr2_mw],

                        #FAPI solution constants
                        'PbI2_nomd':[self.PbI2_nomd],
                        'PbI2_nomM':[self.PbI2_nomM],
                        'FAI_nomM':[self.FAI_nomM],
                        'PbI2_ratio':[self.PbI2_ratio],
                        'FAI_ratio':[self.FAI_ratio],

                        #MAPBr solution constants
                        'PbBr2_nomd':[self.PbBr2_nomd],
                        'PbBr2_nomM':[self.PbBr2_nomM],
                        'MABr_nomM':[self.MABr_nomM],
                        'PbBr2_ratio':[self.PbBr2_ratio],
                        'MABr_ratio':[self.MABr_ratio],
                        'FAPI_MAPI_ratio':[self.ratio]}

        self.storageframe = pd.DataFrame(self.storage)

    def function_17(self): #Saving data to csv
        newdata = self.storageframe
        #if the file doenst exist yet include headers, if not exdlude
        with open('PSK_MV_Calc_Data.csv', 'a') as f:

            if f.tell() == 0:
                newdata.to_csv(f, header=True)

            else:
                newdata.to_csv(f, header=False)

        #for troubleshooting: this counts the number of rows in csv
        with open('PSK_MV_Calc_Data.csv', 'r') as f:
            row_count = sum(1 for row in f) - 1       


        date = self.date_input_2.text() 
        solutiontype = self.solutiontype_input_2.text()
        usernote = self.note_input_2.text()
        filename = '{0}_{1}_{2}.csv'.format(date, solutiontype, usernote)

        with open(filename, 'a') as f:
            if f.tell() == 0:
                newdata.to_csv(f, header=True)

            else:
                newdata.to_csv(f, header=False)


        self.savepath.setText(str(row_count) + ' Entries in document!')
    

######### HTL

    def function_8(self): #HTL Volume required
            # input batch detail
            self.var_HTL_Count = float(self.input_HTL_Device_Count.text())
            self.var_HTL_vperdevice = float(self.input_HTL_vperdevice.text())

            # calculate volume required
            self.var_HTL_V_batch = self.var_HTL_Count * self.var_HTL_vperdevice

            #send to display
            self.display_HT_V_required.setText(str(round(self.var_HTL_V_batch,2)))

    def function_9(self): #HTL Volume of solution
            #recipe to scale off of
            self.var_Spiro_weight_scaler = 0.08
            self.var_CB_v_scaler = 1000
            self.var_LiTFSI_scaler = 17.7
            self.var_TBP_scaler = 24.4

            self.var_Spiro_weight = float(self.input_Spiro_weight.text())
            self.var_CB_v_scaled = (self.var_Spiro_weight / self.var_Spiro_weight_scaler) * self.var_CB_v_scaler
            self.var_LiTFSI_scaled = (self.var_Spiro_weight / self.var_Spiro_weight_scaler) * self.var_LiTFSI_scaler
            self.var_TBP_scaled = (self.var_Spiro_weight / self.var_Spiro_weight_scaler) * self.var_TBP_scaler

            self.var_HTL_soln_final = self.var_CB_v_scaled + self.var_LiTFSI_scaler + self.var_TBP_scaled 

            # sending calculated values to display fields
            self.display_HTL_CB_V.setText(str(round(self.var_CB_v_scaled,2)))
            self.display_HTL_LiTFSI_V.setText(str(round(self.var_LiTFSI_scaled,2)))
            self.display_HTL_TBP_V.setText(str(round(self.var_TBP_scaled,2)))
            self.display_HTL_soln_final.setText(str(round(self.var_HTL_soln_final,2)))

    def function_10(self, fineName): #Store variables to dataframe
        #variables in data frame format
        self.HTL_storage = {'Date':[self.now],
                        'Count':[self.var_HTL_Count], 
                        'V/Device':[self.var_HTL_vperdevice], 
                        'var_HTL_V_batch':[self.var_HTL_V_batch], 
                        'var_Spiro_weight_scaler':[self.var_Spiro_weight_scaler], 
                        'var_CB_v_scaler':[self.var_CB_v_scaler], 
                        'var_LiTFSI_scaler':[self.var_LiTFSI_scaler], 
                        'var_TBP_scaler':[self.var_TBP_scaler], 
                        'var_Spiro_weight':[self.var_Spiro_weight], 
                        'var_CB_v_scaled':[self.var_CB_v_scaled], 
                        'var_LiTFSI_scaled':[self.var_LiTFSI_scaled], 
                        'var_TBP_scaled':[self.var_TBP_scaled],
                        'var_HTL_soln_final':[self.var_HTL_soln_final]}

        self.HTL_storageframe = pd.DataFrame(self.HTL_storage)
        # self.arrayconfirm_HTL.setText('Array Built!')

        # print(self.storage)
        # print(self.HTL_storageframe)

    def function_11(self): #Save stored variables to CSV
        HTL_newdata = self.HTL_storageframe
        #if the file doenst exist yet include headers, if not exdlude
        with open('HTL_MV_Calc_Data.csv', 'a') as f:

            if f.tell() == 0:
                HTL_newdata.to_csv(f, header=True)

            else:
                HTL_newdata.to_csv(f, header=False)

        #for troubleshooting: this counts the number of rows in csv
        with open('HTL_MV_Calc_Data.csv', 'r') as f:
            row_count = sum(1 for row in f) - 1       


        date = self.date_input_HTL.text() 
        solutiontype = self.solutiontype_input_HTL.text()
        usernote = self.note_input_HTL.text()
        filename = '{0}_{1}_{2}.csv'.format(date, solutiontype, usernote)

        with open(filename, 'a') as f:
            if f.tell() == 0:
                HTL_newdata.to_csv(f, header=True)

            else:
                HTL_newdata.to_csv(f, header=False)


        self.savepath_HTL.setText(str(row_count) + ' Entries in document!')


######### GUI exiting protocol, (to prevent system error on close)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())