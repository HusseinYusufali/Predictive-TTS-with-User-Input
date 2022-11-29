import sys
#from curses.ascii import isdigit
#from gtts import gTTS #Import Google Text to Speech
from happytransformer import HappyWordPrediction
import pandas as pd 
#from playsound import playsound as play
from autocorrect import Speller
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtCore import pyqtSlot
import pyttsx3 

#Prediction class, with the model parameters and path     
class predictor():
    spell = None
    predict_max = 30
    exitcommand = 'Q'
    stext = ''
    happy_wp_roberta_aac = None
    
    #Model path and parameters
    def __init__(self):
        self.prediction_model = "ROBERTA"
        self.model_name = "roberta-base"
        self.model_path = "/Users/husseinyusufali/Desktop/PhD/Main PhD Folder/PhD - Year 2/Technical System Implementation/Predictive TransformerTTS/Transformer Models/modelroberta_AACHPC_2"
        self.spell = Speller()
        self.happy_wp_roberta_aac = HappyWordPrediction(self.prediction_model, self.model_name, self.model_path)
        
    #Function to predict the predictions according to the string    
    def predictNext(self,currentString):
        self.stext = self.spell.autocorrect_sentence(currentString) + '' + '[MASK]' + ''
        result = self.happy_wp_roberta_aac.predict_mask(self.stext, top_k = self.predict_max)
        return result

    def set_stext(self, currentString):
        self.stext = currentString

    #Function for TTS
    def play(self):
        engine = pyttsx3.init()
        engine.startLoop(False)
        engine.say(self.stext.replace('[MASK]',''))
        engine.iterate()

class Ui_Tab3(object):

    pred = predictor()     # instance of predictor class
    text = ''              # so far inputted text
    iLastButtonPressed = 0 
    reopen = True
    global iNo

    def setupUi(self, Dialog):
        self.reopen = False
        self.dialog = Dialog;
        Tab3.setObjectName("Dialog")
        Tab3.resize(927, 680)
        Tab3.setMouseTracking(False)
        Tab3.setAcceptDrops(False)
        Tab3.setAutoFillBackground(True)
        Tab3.setUsesScrollButtons(False)
        Tab3.setDocumentMode(False)
        Tab3.setTabsClosable(True)
        Tab3.setMovable(True)
        Tab3.setTabBarAutoHide(False)
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 280, 751, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.returnPressed.connect(self.lineEdit_returnPressed)
        
        iNo = 0
        
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(90, 10, 751, 41))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.returnPressed.connect(self.lineEdit_returnPressed)

        self.pushButtons = []

        self.pushButton_22 = QtWidgets.QPushButton(self.tab)
        self.pushButton_22.setGeometry(QtCore.QRect(180, 80, 113, 32))
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_22.clicked.connect(lambda ch, button=self.pushButton_22: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_22)
        iNo += 1

        self.pushButton_23 = QtWidgets.QPushButton(self.tab)
        self.pushButton_23.setGeometry(QtCore.QRect(180, 110, 113, 32))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_23.clicked.connect(lambda ch, button=self.pushButton_23: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_23)
        iNo += 1

        self.pushButton_24 = QtWidgets.QPushButton(self.tab)
        self.pushButton_24.setGeometry(QtCore.QRect(180, 140, 113, 32))
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_24.clicked.connect(lambda ch, button=self.pushButton_24: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_24)
        iNo += 1

        self.pushButton_25 = QtWidgets.QPushButton(self.tab)
        self.pushButton_25.setGeometry(QtCore.QRect(180, 170, 113, 32))
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_25.clicked.connect(lambda ch, button=self.pushButton_25: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_25)
        iNo += 1


        self.pushButton_26 = QtWidgets.QPushButton(self.tab)
        self.pushButton_26.setGeometry(QtCore.QRect(180, 200, 113, 32))
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_26.clicked.connect(lambda ch, button=self.pushButton_26: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_26)
        iNo += 1

        self.pushButton_27 = QtWidgets.QPushButton(self.tab)
        self.pushButton_27.setGeometry(QtCore.QRect(300, 140, 113, 32))
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_27.clicked.connect(lambda ch, button=self.pushButton_27: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_27)
        iNo += 1

        self.pushButton_28 = QtWidgets.QPushButton(self.tab)
        self.pushButton_28.setGeometry(QtCore.QRect(300, 200, 113, 32))
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_28.clicked.connect(lambda ch, button=self.pushButton_28: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_28)
        iNo += 1

        self.pushButton_29 = QtWidgets.QPushButton(self.tab)
        self.pushButton_29.setGeometry(QtCore.QRect(300, 170, 113, 32))
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_29.clicked.connect(lambda ch, button=self.pushButton_29: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_29)
        iNo += 1

        self.pushButton_30 = QtWidgets.QPushButton(self.tab)
        self.pushButton_30.setGeometry(QtCore.QRect(300, 110, 113, 32))
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_30.clicked.connect(lambda ch, button=self.pushButton_30: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_30)
        iNo += 1

        self.pushButton_31 = QtWidgets.QPushButton(self.tab)
        self.pushButton_31.setGeometry(QtCore.QRect(300, 80, 113, 32))
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_31.clicked.connect(lambda ch, button=self.pushButton_31: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_31)
        iNo += 1

        self.pushButton_32 = QtWidgets.QPushButton(self.tab)
        self.pushButton_32.setGeometry(QtCore.QRect(420, 140, 113, 32))
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_32.clicked.connect(lambda ch, button=self.pushButton_32: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_32)
        iNo += 1

        self.pushButton_33 = QtWidgets.QPushButton(self.tab)
        self.pushButton_33.setGeometry(QtCore.QRect(420, 200, 113, 32))
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_33.clicked.connect(lambda ch, button=self.pushButton_33: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_33)
        iNo += 1

        self.pushButton_34 = QtWidgets.QPushButton(self.tab)
        self.pushButton_34.setGeometry(QtCore.QRect(420, 170, 113, 32))
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_34.clicked.connect(lambda ch, button=self.pushButton_34: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_34)
        iNo += 1

        self.pushButton_35 = QtWidgets.QPushButton(self.tab)
        self.pushButton_35.setGeometry(QtCore.QRect(420, 110, 113, 32))
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_35.clicked.connect(lambda ch, button=self.pushButton_35: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_35)
        iNo += 1

        self.pushButton_36 = QtWidgets.QPushButton(self.tab)
        self.pushButton_36.setGeometry(QtCore.QRect(420, 80, 113, 32))
        self.pushButton_36.setObjectName("pushButton_36")
        self.pushButton_36.clicked.connect(lambda ch, button=self.pushButton_36: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_36)
        iNo += 1

        self.pushButton_37 = QtWidgets.QPushButton(self.tab)
        self.pushButton_37.setGeometry(QtCore.QRect(540, 140, 113, 32))
        self.pushButton_37.setObjectName("pushButton_37")
        self.pushButton_37.clicked.connect(lambda ch, button=self.pushButton_37: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_37)
        iNo += 1

        self.pushButton_38 = QtWidgets.QPushButton(self.tab)
        self.pushButton_38.setGeometry(QtCore.QRect(540, 200, 113, 32))
        self.pushButton_38.setObjectName("pushButton_38")
        self.pushButton_38.clicked.connect(lambda ch, button=self.pushButton_38: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_38)
        iNo += 1

        self.pushButton_39 = QtWidgets.QPushButton(self.tab)
        self.pushButton_39.setGeometry(QtCore.QRect(540, 170, 113, 32))
        self.pushButton_39.setObjectName("pushButton_39")
        self.pushButton_39.clicked.connect(lambda ch, button=self.pushButton_39: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_39)
        iNo += 1

        self.pushButton_40 = QtWidgets.QPushButton(self.tab)
        self.pushButton_40.setGeometry(QtCore.QRect(540, 110, 113, 32))
        self.pushButton_40.setObjectName("pushButton_40")
        self.pushButton_40.clicked.connect(lambda ch, button=self.pushButton_40: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_40)
        iNo += 1

        self.pushButton_41 = QtWidgets.QPushButton(self.tab)
        self.pushButton_41.setGeometry(QtCore.QRect(540, 80, 113, 32))
        self.pushButton_41.setObjectName("pushButton_41")
        self.pushButton_41.clicked.connect(lambda ch, button=self.pushButton_41: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_41)
        iNo += 1

        self.pushButton_42 = QtWidgets.QPushButton(self.tab)
        self.pushButton_42.setGeometry(QtCore.QRect(660, 140, 113, 32))
        self.pushButton_42.setObjectName("pushButton_42")
        self.pushButton_42.clicked.connect(lambda ch, button=self.pushButton_42: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_42)
        iNo += 1

        self.pushButton_43 = QtWidgets.QPushButton(self.tab)
        self.pushButton_43.setGeometry(QtCore.QRect(660, 200, 113, 32))
        self.pushButton_43.setObjectName("pushButton_43")
        self.pushButton_43.clicked.connect(lambda ch, button=self.pushButton_43: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_43)
        iNo += 1

        self.pushButton_44 = QtWidgets.QPushButton(self.tab)
        self.pushButton_44.setGeometry(QtCore.QRect(660, 170, 113, 32))
        self.pushButton_44.setObjectName("pushButton_44")
        self.pushButton_44.clicked.connect(lambda ch, button=self.pushButton_44: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_44)
        iNo += 1

        self.pushButton_45 = QtWidgets.QPushButton(self.tab)
        self.pushButton_45.setGeometry(QtCore.QRect(660, 110, 113, 32))
        self.pushButton_45.setObjectName("pushButton_45")
        self.pushButton_45.clicked.connect(lambda ch, button=self.pushButton_45: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_45)
        iNo += 1

        self.pushButton_46 = QtWidgets.QPushButton(self.tab)
        self.pushButton_46.setGeometry(QtCore.QRect(660, 80, 113, 32))
        self.pushButton_46.setObjectName("pushButton_46")
        self.pushButton_46.clicked.connect(lambda ch, button=self.pushButton_46: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_46)
        iNo += 1

        Tab3.addTab(self.tab, "")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")


        self.pushButton = QtWidgets.QPushButton(self.tab1)
        self.pushButton.setGeometry(QtCore.QRect(410, 60, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda ch, button=self.pushButton: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton)
        iNo += 1
        
        self.pushButton_2 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 90, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda ch, button=self.pushButton_2: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_2)
        iNo += 1

        self.pushButton_3 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 90, 113, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda ch, button=self.pushButton_3: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_3)
        iNo += 1

        self.pushButton_4 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_4.setGeometry(QtCore.QRect(520, 90, 113, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda ch, button=self.pushButton_4: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_4)
        iNo += 1

        self.pushButton_5 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_5.setGeometry(QtCore.QRect(240, 120, 113, 32))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(lambda ch, button=self.pushButton_5: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_5)
        iNo += 1

        self.pushButton_6 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_6.setGeometry(QtCore.QRect(350, 120, 113, 32))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(lambda ch, button=self.pushButton_6: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_6)
        iNo += 1

        self.pushButton_7 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_7.setGeometry(QtCore.QRect(460, 120, 113, 32))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(lambda ch, button=self.pushButton_7: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_7)
        iNo += 1

        self.pushButton_8 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_8.setGeometry(QtCore.QRect(570, 120, 113, 32))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(lambda ch, button=self.pushButton_8: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_8)
        iNo += 1

        self.pushButton_9 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_9.setGeometry(QtCore.QRect(400, 150, 113, 32))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(lambda ch, button=self.pushButton_9: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_9)
        iNo += 1

        self.pushButton_10 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_10.setGeometry(QtCore.QRect(180, 150, 113, 32))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(lambda ch, button=self.pushButton_10: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_10)
        iNo += 1

        self.pushButton_11 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_11.setGeometry(QtCore.QRect(510, 150, 113, 32))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(lambda ch, button=self.pushButton_11: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_11)
        iNo += 1

        self.pushButton_12 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_12.setGeometry(QtCore.QRect(290, 150, 113, 32))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(lambda ch, button=self.pushButton_12: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_12)
        iNo += 1

        self.pushButton_14 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_14.setGeometry(QtCore.QRect(620, 150, 113, 32))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.clicked.connect(lambda ch, button=self.pushButton_14: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_14)
        iNo += 1

        self.pushButton_13 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_13.setGeometry(QtCore.QRect(460, 180, 113, 32))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(lambda ch, button=self.pushButton_13: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_13)
        iNo += 1

        self.pushButton_15 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_15.setGeometry(QtCore.QRect(240, 180, 113, 32))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.clicked.connect(lambda ch, button=self.pushButton_15: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_15)
        iNo += 1

        self.pushButton_16 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_16.setGeometry(QtCore.QRect(570, 180, 113, 32))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_16.clicked.connect(lambda ch, button=self.pushButton_16: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_16)
        iNo += 1

        self.pushButton_17 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_17.setGeometry(QtCore.QRect(350, 180, 113, 32))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_17.clicked.connect(lambda ch, button=self.pushButton_17: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_17)
        iNo += 1

        self.pushButton_18 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_18.setGeometry(QtCore.QRect(520, 210, 113, 32))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_18.clicked.connect(lambda ch, button=self.pushButton_18: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_18)
        iNo += 1

        self.pushButton_19 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_19.setGeometry(QtCore.QRect(300, 210, 113, 32))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_19.clicked.connect(lambda ch, button=self.pushButton_19: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_19)
        iNo += 1

        self.pushButton_20 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_20.setGeometry(QtCore.QRect(410, 210, 113, 32))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_20.clicked.connect(lambda ch, button=self.pushButton_20: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_20)
        iNo += 1

        self.pushButton_21 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_21.setGeometry(QtCore.QRect(410, 240, 113, 32))
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_21.clicked.connect(lambda ch, button=self.pushButton_21: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_21)
        iNo += 1

        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab1)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 280, 751, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.returnPressed.connect(self.lineEdit_returnPressed)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab1)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 10, 751, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.returnPressed.connect(self.lineEdit_returnPressed)

        Tab3.addTab(self.tab1, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(360, 370, 241, 41))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.returnPressed.connect(self.lineEdit_returnPressed)

        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(360, 10, 221, 41))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.returnPressed.connect(self.lineEdit_returnPressed)


        self.pushButton_47 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_47.setGeometry(QtCore.QRect(420, 60, 113, 32))
        self.pushButton_47.setObjectName("pushButton_47")
        self.pushButton_47.clicked.connect(lambda ch, button=self.pushButton_47: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_47)
        iNo += 1


        self.pushButton_48 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_48.setGeometry(QtCore.QRect(420, 90, 113, 32))
        self.pushButton_48.setObjectName("pushButton_48")
        self.pushButton_48.clicked.connect(lambda ch, button=self.pushButton_48: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_48)
        iNo += 1

        self.pushButton_49 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_49.setGeometry(QtCore.QRect(420, 120, 113, 32))
        self.pushButton_49.setObjectName("pushButton_49")
        self.pushButton_49.clicked.connect(lambda ch, button=self.pushButton_49: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_49)
        iNo += 1

        self.pushButton_50 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_50.setGeometry(QtCore.QRect(420, 150, 113, 32))
        self.pushButton_50.setObjectName("pushButton_50")
        self.pushButton_50.clicked.connect(lambda ch, button=self.pushButton_50: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_50)
        iNo += 1

        self.pushButton_51 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_51.setGeometry(QtCore.QRect(420, 180, 113, 32))
        self.pushButton_51.setObjectName("pushButton_51")
        self.pushButton_51.clicked.connect(lambda ch, button=self.pushButton_51: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_51)
        iNo += 1


        self.pushButton_52 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_52.setGeometry(QtCore.QRect(420, 210, 113, 32))
        self.pushButton_52.setObjectName("pushButton_52")
        self.pushButton_52.clicked.connect(lambda ch, button=self.pushButton_52: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_52)
        iNo += 1

        self.pushButton_53 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_53.setGeometry(QtCore.QRect(420, 240, 113, 32))
        self.pushButton_53.setObjectName("pushButton_53")
        self.pushButton_53.clicked.connect(lambda ch, button=self.pushButton_53: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_53)
        iNo += 1

        self.pushButton_54 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_54.setGeometry(QtCore.QRect(420, 270, 113, 32))
        self.pushButton_54.setObjectName("pushButton_54")
        self.pushButton_54.clicked.connect(lambda ch, button=self.pushButton_54: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_54)
        iNo += 1

        self.pushButton_55 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_55.setGeometry(QtCore.QRect(420, 300, 113, 32))
        self.pushButton_55.setObjectName("pushButton_55")
        self.pushButton_55.clicked.connect(lambda ch, button=self.pushButton_55: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_55)
        iNo += 1

        self.pushButton_56 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_56.setGeometry(QtCore.QRect(420, 330, 113, 32))
        self.pushButton_56.setObjectName("pushButton_56")
        self.pushButton_56.clicked.connect(lambda ch, button=self.pushButton_56: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_56)
        iNo += 1

        Tab3.addTab(self.tab_3, "")


        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_57 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_57.setGeometry(QtCore.QRect(410, 60, 113, 32))
        self.pushButton_57.setObjectName("pushButton_57")
        self.pushButton_57.clicked.connect(lambda ch, button=self.pushButton_57: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_57)
        iNo += 1

        self.pushButton_58 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_58.setGeometry(QtCore.QRect(410, 30, 113, 32))
        self.pushButton_58.setObjectName("pushButton_58")
        self.pushButton_58.clicked.connect(lambda ch, button=self.pushButton_58: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_58)
        iNo += 1

        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(100, 30, 301, 231))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.returnPressed.connect(self.lineEdit_returnPressed)


        self.pushButton_59 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_59.setGeometry(QtCore.QRect(410, 120, 113, 32))
        self.pushButton_59.setObjectName("pushButton_59")
        self.pushButton_59.clicked.connect(lambda ch, button=self.pushButton_59: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_59)
        iNo += 1

        self.pushButton_60 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_60.setGeometry(QtCore.QRect(410, 150, 113, 32))
        self.pushButton_60.setObjectName("pushButton_60")
        self.pushButton_60.clicked.connect(lambda ch, button=self.pushButton_60: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_60)
        iNo += 1


        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(530, 320, 281, 301))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_9.returnPressed.connect(self.lineEdit_returnPressed)

        self.pushButton_61 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_61.setGeometry(QtCore.QRect(410, 210, 113, 32))
        self.pushButton_61.setObjectName("pushButton_61")
        self.pushButton_61.clicked.connect(lambda ch, button=self.pushButton_61: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_61)
        iNo += 1

        self.pushButton_62 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_62.setGeometry(QtCore.QRect(410, 180, 113, 32))
        self.pushButton_62.setObjectName("pushButton_62")
        self.pushButton_62.clicked.connect(lambda ch, button=self.pushButton_62: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_62)
        iNo += 1

        self.pushButton_63 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_63.setGeometry(QtCore.QRect(410, 270, 113, 32))
        self.pushButton_63.setObjectName("pushButton_63")
        self.pushButton_63.clicked.connect(lambda ch, button=self.pushButton_22: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_63)
        iNo += 1

        self.pushButton_64 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_64.setGeometry(QtCore.QRect(410, 240, 113, 32))
        self.pushButton_64.setObjectName("pushButton_64")
        self.pushButton_64.clicked.connect(lambda ch, button=self.pushButton_64: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_64)
        iNo += 1

        self.pushButton_65 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_65.setGeometry(QtCore.QRect(410, 90, 113, 32))
        self.pushButton_65.setObjectName("pushButton_65")
        self.pushButton_65.clicked.connect(lambda ch, button=self.pushButton_65: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_65)
        iNo += 1

        self.pushButton_66 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_66.setGeometry(QtCore.QRect(410, 300, 113, 32))
        self.pushButton_66.setObjectName("pushButton_66")
        self.pushButton_66.clicked.connect(lambda ch, button=self.pushButton_66: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_66)
        iNo += 1

        self.pushButton_67 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_67.setGeometry(QtCore.QRect(410, 450, 113, 32))
        self.pushButton_67.setObjectName("pushButton_67")
        self.pushButton_67.clicked.connect(lambda ch, button=self.pushButton_67: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_67)
        iNo += 1

        self.pushButton_68 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_68.setGeometry(QtCore.QRect(410, 360, 113, 32))
        self.pushButton_68.setObjectName("pushButton_68")
        self.pushButton_68.clicked.connect(lambda ch, button=self.pushButton_68: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_68)
        iNo += 1

        self.pushButton_69 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_69.setGeometry(QtCore.QRect(410, 420, 113, 32))
        self.pushButton_69.setObjectName("pushButton_69")
        self.pushButton_69.clicked.connect(lambda ch, button=self.pushButton_69: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_69)
        iNo += 1

        self.pushButton_70 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_70.setGeometry(QtCore.QRect(410, 540, 113, 32))
        self.pushButton_70.setObjectName("pushButton_70")
        self.pushButton_70.clicked.connect(lambda ch, button=self.pushButton_70: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_70)
        iNo += 1

        self.pushButton_71 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_71.setGeometry(QtCore.QRect(410, 390, 113, 32))
        self.pushButton_71.setObjectName("pushButton_71")
        self.pushButton_71.clicked.connect(lambda ch, button=self.pushButton_71: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_71)
        iNo += 1

        self.pushButton_72 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_72.setGeometry(QtCore.QRect(410, 330, 113, 32))
        self.pushButton_72.setObjectName("pushButton_72")
        self.pushButton_72.clicked.connect(lambda ch, button=self.pushButton_72: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_72)
        iNo += 1

        self.pushButton_73 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_73.setGeometry(QtCore.QRect(410, 600, 113, 32))
        self.pushButton_73.setObjectName("pushButton_73")
        self.pushButton_73.clicked.connect(lambda ch, button=self.pushButton_73: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_73)
        iNo += 1

        self.pushButton_74 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_74.setGeometry(QtCore.QRect(410, 510, 113, 32))
        self.pushButton_74.setObjectName("pushButton_74")
        self.pushButton_74.clicked.connect(lambda ch, button=self.pushButton_74: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_74)
        iNo += 1

        self.pushButton_75 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_75.setGeometry(QtCore.QRect(410, 480, 113, 32))
        self.pushButton_75.setObjectName("pushButton_75")
        self.pushButton_75.clicked.connect(lambda ch, button=self.pushButton_75: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_75)
        iNo += 1

        self.pushButton_76 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_76.setGeometry(QtCore.QRect(410, 570, 113, 32))
        self.pushButton_76.setObjectName("pushButton_76")
        self.pushButton_76.clicked.connect(lambda ch, button=self.pushButton_76: self.choiceButtonClicked(button))
        self.pushButtons.append(self.pushButton_76)
        iNo += 1

        #self.pushButtons = list(enumerate(self.pushButtons, 1))
        #self.pushButtons.split(',')
        print("**********", (self.pushButtons))

        print('TYPE')
        print(type(self.pushButtons))

        for i in self.pushButtons:
             for j in i:
                print(j)
                #j.setText('')

        Tab3.addTab(self.tab_2, "")

        self.retranslateUi(Tab3)
        Tab3.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Tab3)

    def retranslateUi(self, Tab3):
        _translate = QtCore.QCoreApplication.translate
        Tab3.setWindowTitle(_translate("Tab3", "TabWidget"))
        Tab3.setToolTip(_translate("Tab3", "<html><head/><body><p>Tab3</p><p><br/></p></body></html>"))
        self.pushButton_22.setText(_translate("Tab3", "PushButton"))
        self.pushButton_23.setText(_translate("Tab3", "PushButton"))
        self.pushButton_24.setText(_translate("Tab3", "PushButton"))
        self.pushButton_25.setText(_translate("Tab3", "PushButton"))
        self.pushButton_26.setText(_translate("Tab3", "PushButton"))
        self.pushButton_27.setText(_translate("Tab3", "PushButton"))
        self.pushButton_28.setText(_translate("Tab3", "PushButton"))
        self.pushButton_29.setText(_translate("Tab3", "PushButton"))
        self.pushButton_30.setText(_translate("Tab3", "PushButton"))
        self.pushButton_31.setText(_translate("Tab3", "PushButton"))
        self.pushButton_32.setText(_translate("Tab3", "PushButton"))
        self.pushButton_33.setText(_translate("Tab3", "PushButton"))
        self.pushButton_34.setText(_translate("Tab3", "PushButton"))
        self.pushButton_35.setText(_translate("Tab3", "PushButton"))
        self.pushButton_36.setText(_translate("Tab3", "PushButton"))
        self.pushButton_37.setText(_translate("Tab3", "PushButton"))
        self.pushButton_38.setText(_translate("Tab3", "PushButton"))
        self.pushButton_39.setText(_translate("Tab3", "PushButton"))
        self.pushButton_40.setText(_translate("Tab3", "PushButton"))
        self.pushButton_41.setText(_translate("Tab3", "PushButton"))
        self.pushButton_42.setText(_translate("Tab3", "PushButton"))
        self.pushButton_43.setText(_translate("Tab3", "PushButton"))
        self.pushButton_44.setText(_translate("Tab3", "PushButton"))
        self.pushButton_45.setText(_translate("Tab3", "PushButton"))
        self.pushButton_46.setText(_translate("Tab3", "PushButton"))
        Tab3.setTabText(Tab3.indexOf(self.tab), _translate("Tab3", "Tab 1"))
        self.pushButton.setText(_translate("Tab3", "PushButton"))
        self.pushButton_2.setText(_translate("Tab3", "PushButton"))
        self.pushButton_3.setText(_translate("Tab3", "PushButton"))
        self.pushButton_4.setText(_translate("Tab3", "PushButton"))
        self.pushButton_5.setText(_translate("Tab3", "PushButton"))
        self.pushButton_6.setText(_translate("Tab3", "PushButton"))
        self.pushButton_7.setText(_translate("Tab3", "PushButton"))
        self.pushButton_8.setText(_translate("Tab3", "PushButton"))
        self.pushButton_9.setText(_translate("Tab3", "PushButton"))
        self.pushButton_10.setText(_translate("Tab3", "PushButton"))
        self.pushButton_11.setText(_translate("Tab3", "PushButton"))
        self.pushButton_12.setText(_translate("Tab3", "PushButton"))
        self.pushButton_14.setText(_translate("Tab3", "PushButton"))
        self.pushButton_13.setText(_translate("Tab3", "PushButton"))
        self.pushButton_15.setText(_translate("Tab3", "PushButton"))
        self.pushButton_16.setText(_translate("Tab3", "PushButton"))
        self.pushButton_17.setText(_translate("Tab3", "PushButton"))
        self.pushButton_18.setText(_translate("Tab3", "PushButton"))
        self.pushButton_19.setText(_translate("Tab3", "PushButton"))
        self.pushButton_20.setText(_translate("Tab3", "PushButton"))
        self.pushButton_21.setText(_translate("Tab3", "PushButton"))
        Tab3.setTabText(Tab3.indexOf(self.tab1), _translate("Tab3", "Tab 2"))
        self.pushButton_47.setText(_translate("Tab3", "PushButton"))
        self.pushButton_48.setText(_translate("Tab3", "PushButton"))
        self.pushButton_49.setText(_translate("Tab3", "PushButton"))
        self.pushButton_50.setText(_translate("Tab3", "PushButton"))
        self.pushButton_51.setText(_translate("Tab3", "PushButton"))
        self.pushButton_52.setText(_translate("Tab3", "PushButton"))
        self.pushButton_53.setText(_translate("Tab3", "PushButton"))
        self.pushButton_54.setText(_translate("Tab3", "PushButton"))
        self.pushButton_55.setText(_translate("Tab3", "PushButton"))
        self.pushButton_56.setText(_translate("Tab3", "PushButton"))
        Tab3.setTabText(Tab3.indexOf(self.tab_3), _translate("Tab3", "Tab 3"))
        self.pushButton_57.setText(_translate("Tab3", "PushButton"))
        self.pushButton_58.setText(_translate("Tab3", "PushButton"))
        self.pushButton_59.setText(_translate("Tab3", "PushButton"))
        self.pushButton_60.setText(_translate("Tab3", "PushButton"))
        self.pushButton_61.setText(_translate("Tab3", "PushButton"))
        self.pushButton_62.setText(_translate("Tab3", "PushButton"))
        self.pushButton_63.setText(_translate("Tab3", "PushButton"))
        self.pushButton_64.setText(_translate("Tab3", "PushButton"))
        self.pushButton_65.setText(_translate("Tab3", "PushButton"))
        self.pushButton_66.setText(_translate("Tab3", "PushButton"))
        self.pushButton_67.setText(_translate("Tab3", "PushButton"))
        self.pushButton_68.setText(_translate("Tab3", "PushButton"))
        self.pushButton_69.setText(_translate("Tab3", "PushButton"))
        self.pushButton_70.setText(_translate("Tab3", "PushButton"))
        self.pushButton_71.setText(_translate("Tab3", "PushButton"))
        self.pushButton_72.setText(_translate("Tab3", "PushButton"))
        self.pushButton_73.setText(_translate("Tab3", "PushButton"))
        self.pushButton_74.setText(_translate("Tab3", "PushButton"))
        self.pushButton_75.setText(_translate("Tab3", "PushButton"))
        self.pushButton_76.setText(_translate("Tab3", "PushButton"))
        Tab3.setTabText(Tab3.indexOf(self.tab_2), _translate("Tab3", "Tab 4"))

    def choiceButtonClicked(self, buttonText):
        #print('Button no. ' + str(button) + ' was pressed...')
        print('Button pressed')
        print(buttonText)
        print('This is the button in line')

    def lineEdit_returnPressed(self):
        print(self.lineEdit.text())
        if self.lineEdit.text() == "Q":
          self.lineEdit_2.setText('')
          self.text = ''
          self.reopen = True
          self.dialog.close();
          return;
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tab3 = QtWidgets.QTabWidget()
    ui = Ui_Tab3()
    ui.setupUi(Tab3)
    Tab3.show()
    sys.exit(app.exec())