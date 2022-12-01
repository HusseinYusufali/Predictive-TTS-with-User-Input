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
        #self.model_path = "./../Transformer-Models/modelroberta_AACHPC_2"
        self.spell = Speller()
        self.happy_wp_roberta_aac = HappyWordPrediction(self.prediction_model, self.model_name, self.model_path)
        
    #Function to predict the predictions according to the string    
    def predictNext(self,currentString):
        self.stext = self.spell.autocorrect_sentence(currentString) + '' + '[MASK]' + ''
        result = self.happy_wp_roberta_aac.predict_mask(self.stext, top_k = self.predict_max)
        return result

    #Function for TTS
    def play(self):                  ################################## MOVE THIS TO TTS CLASS
        engine = pyttsx3.init()
        engine.startLoop(False)
        engine.say(self.stext.replace('[MASK]',''))
        engine.iterate()

    def set_stext(self, currentString):
        self.stext = currentString

class Ui_Tab3(object):

    pred = predictor()     # instance of predictor class
    text1 = ''              # so far inputted text
    text2 = ''              # so far inputted text
    text3 = ''              # so far inputted text
    text4 = ''              # so far inputted text on tab 4
    iLastButtonPressed = 0 
    reopen = True

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
        
        self.pushButtons1 = []
        self.pushButtons2 = []
        self.pushButtons3 = []
        self.pushButtons4 = []
        
        ################################################################# FIRST TAB ##################################################################################################################
        # FIRST TAB
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("Tab_1")

        self.lineEdit_1_1 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_1_1.setGeometry(QtCore.QRect(90, 10, 751, 41))
        self.lineEdit_1_1.setObjectName("lineEdit_1_1")
        self.lineEdit_1_1.returnPressed.connect(self.lineEdit_returnPressed1)

        self.lineEdit_1_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_1_2.setGeometry(QtCore.QRect(100, 280, 751, 41))
        self.lineEdit_1_2.setObjectName("lineEdit_1_2")
        self.lineEdit_1_2.returnPressed.connect(self.lineEdit_returnPressed1)

        self.pushButton_1_1 = QtWidgets.QPushButton(self.tab)
        self.pushButton_1_1.setGeometry(QtCore.QRect(180, 80, 113, 32))
        self.pushButton_1_1.setObjectName("pushButton_1_1")
        self.pushButton_1_1.clicked.connect(lambda ch, button=self.pushButton_1_1: self.choiceButtonClicked1(button))
        self.pushButtons1.append(self.pushButton_1_1)

        self.pushButton_1_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_1_2.setGeometry(QtCore.QRect(180, 110, 113, 32))
        self.pushButton_1_2.setObjectName("pushButton_1_2")
        self.pushButton_1_2.clicked.connect(lambda ch, button=self.pushButton_1_2: self.choiceButtonClicked1(button))
        self.pushButtons1.append(self.pushButton_1_2)

        self.pushButton_1_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_1_3.setGeometry(QtCore.QRect(180, 140, 113, 32))
        self.pushButton_1_3.setObjectName("pushButton_1_3")
        self.pushButton_1_3.clicked.connect(lambda ch, button=self.pushButton_1_3: self.choiceButtonClicked1(button))
        self.pushButtons1.append(self.pushButton_1_3)

        self.pushButton_1_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_1_4.setGeometry(QtCore.QRect(180, 170, 113, 32))
        self.pushButton_1_4.setObjectName("pushButton_1_4")
        self.pushButton_1_4.clicked.connect(lambda ch, button=self.pushButton_1_4: self.choiceButtonClicked1(button))
        self.pushButtons1.append(self.pushButton_1_4)

        self.pushButton_1_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_1_5.setGeometry(QtCore.QRect(180, 200, 113, 32))
        self.pushButton_1_5.setObjectName("pushButton_1_5")
        self.pushButton_1_5.clicked.connect(lambda ch, button=self.pushButton_1_5: self.choiceButtonClicked1(button))
        self.pushButtons1.append(self.pushButton_1_5)

        self.pushButton_1_6 = QtWidgets.QPushButton(self.tab)
        self.pushButton_1_6.setGeometry(QtCore.QRect(300, 140, 113, 32))
        self.pushButton_1_6.setObjectName("pushButton_1_6")
        self.pushButton_1_6.clicked.connect(lambda ch, button=self.pushButton_1_6: self.choiceButtonClicked1(button))
        self.pushButtons1.append(self.pushButton_1_6)

        self.pushButton_1_7 = QtWidgets.QPushButton(self.tab)
        self.pushButton_1_7.setGeometry(QtCore.QRect(300, 200, 113, 32))
        self.pushButton_1_7.setObjectName("pushButton_1_7")
        self.pushButton_1_7.clicked.connect(lambda ch, button=self.pushButton_1_7: self.choiceButtonClicked1(button))
        self.pushButtons1.append(self.pushButton_1_7)

        self.pushButton_1_8 = QtWidgets.QPushButton(self.tab)
        self.pushButton_1_8.setGeometry(QtCore.QRect(300, 170, 113, 32))
        self.pushButton_1_8.setObjectName("pushButton_1_8")
        self.pushButton_1_8.clicked.connect(lambda ch, button=self.pushButton_1_8: self.choiceButtonClicked1(button))
        self.pushButtons1.append(self.pushButton_1_8)

        self.pushButton_1_9 = QtWidgets.QPushButton(self.tab)
        self.pushButton_1_9.setGeometry(QtCore.QRect(300, 110, 113, 32))
        self.pushButton_1_9.setObjectName("pushButton_1_9")
        self.pushButton_1_9.clicked.connect(lambda ch, button=self.pushButton_1_9: self.choiceButtonClicked1(button))
        self.pushButtons1.append(self.pushButton_1_9)

        self.pushButton_1_10 = QtWidgets.QPushButton(self.tab)
        self.pushButton_1_10.setGeometry(QtCore.QRect(300, 80, 113, 32))
        self.pushButton_1_10.setObjectName("pushButton_1_10")
        self.pushButton_1_10.clicked.connect(lambda ch, button=self.pushButton_1_10: self.choiceButtonClicked1(button))
        self.pushButtons1.append(self.pushButton_1_10)

        self.pushButton_1_11 = QtWidgets.QPushButton(self.tab)
        self.pushButton_1_11.setGeometry(QtCore.QRect(420, 140, 113, 32))
        self.pushButton_1_11.setObjectName("pushButton_1_11")
        self.pushButton_1_11.clicked.connect(lambda ch, button=self.pushButton_1_11: self.choiceButtonClicked1(button))
        self.pushButtons1.append(self.pushButton_1_11)

        self.pushButton_1_12 = QtWidgets.QPushButton(self.tab)
        self.pushButton_1_12.setGeometry(QtCore.QRect(420, 200, 113, 32))
        self.pushButton_1_12.setObjectName("pushButton_1_12")
        self.pushButton_1_12.clicked.connect(lambda ch, button=self.pushButton_1_12: self.choiceButtonClicked1(button))
        self.pushButtons1.append(self.pushButton_1_12)

        self.pushButton_1_13 = QtWidgets.QPushButton(self.tab)
        self.pushButton_1_13.setGeometry(QtCore.QRect(420, 170, 113, 32))
        self.pushButton_1_13.setObjectName("pushButton_1_13")
        self.pushButton_1_13.clicked.connect(lambda ch, button=self.pushButton_1_13: self.choiceButtonClicked1(button))
        self.pushButtons1.append(self.pushButton_1_13)

        self.pushButton_1_14 = QtWidgets.QPushButton(self.tab)
        self.pushButton_1_14.setGeometry(QtCore.QRect(420, 110, 113, 32))
        self.pushButton_1_14.setObjectName("pushButton_1_14")
        self.pushButton_1_14.clicked.connect(lambda ch, button=self.pushButton_1_14: self.choiceButtonClicked1(button))
        self.pushButtons1.append(self.pushButton_1_14)

        self.pushButton_1_15 = QtWidgets.QPushButton(self.tab)
        self.pushButton_1_15.setGeometry(QtCore.QRect(420, 80, 113, 32))
        self.pushButton_1_15.setObjectName("pushButton_1_15")
        self.pushButton_1_15.clicked.connect(lambda ch, button=self.pushButton_1_15: self.choiceButtonClicked1(button))
        self.pushButtons1.append(self.pushButton_1_15)

        self.pushButton_1_16 = QtWidgets.QPushButton(self.tab)
        self.pushButton_1_16.setGeometry(QtCore.QRect(540, 140, 113, 32))
        self.pushButton_1_16.setObjectName("pushButton_1_16")
        self.pushButton_1_16.clicked.connect(lambda ch, button=self.pushButton_1_16: self.choiceButtonClicked1(button))
        self.pushButtons1.append(self.pushButton_1_16)

        self.pushButton_1_17 = QtWidgets.QPushButton(self.tab)
        self.pushButton_1_17.setGeometry(QtCore.QRect(540, 200, 113, 32))
        self.pushButton_1_17.setObjectName("pushButton_1_17")
        self.pushButton_1_17.clicked.connect(lambda ch, button=self.pushButton_1_17: self.choiceButtonClicked1(button))
        self.pushButtons1.append(self.pushButton_1_17)

        self.pushButton_1_18 = QtWidgets.QPushButton(self.tab)
        self.pushButton_1_18.setGeometry(QtCore.QRect(540, 170, 113, 32))
        self.pushButton_1_18.setObjectName("pushButton_1_18")
        self.pushButton_1_18.clicked.connect(lambda ch, button=self.pushButton_1_18: self.choiceButtonClicked1(button))
        self.pushButtons1.append(self.pushButton_1_18)

        self.pushButton_1_19 = QtWidgets.QPushButton(self.tab)
        self.pushButton_1_19.setGeometry(QtCore.QRect(540, 110, 113, 32))
        self.pushButton_1_19.setObjectName("pushButton_1_19")
        self.pushButton_1_19.clicked.connect(lambda ch, button=self.pushButton_1_19: self.choiceButtonClicked1(button))
        self.pushButtons1.append(self.pushButton_1_19)

        self.pushButton_1_20 = QtWidgets.QPushButton(self.tab)
        self.pushButton_1_20.setGeometry(QtCore.QRect(540, 80, 113, 32))
        self.pushButton_1_20.setObjectName("pushButton_1_20")
        self.pushButton_1_20.clicked.connect(lambda ch, button=self.pushButton_1_20: self.choiceButtonClicked1(button))
        self.pushButtons1.append(self.pushButton_1_20)

        self.pushButton_1_21 = QtWidgets.QPushButton(self.tab)
        self.pushButton_1_21.setGeometry(QtCore.QRect(660, 140, 113, 32))
        self.pushButton_1_21.setObjectName("pushButton_1_21")
        self.pushButton_1_21.clicked.connect(lambda ch, button=self.pushButton_1_21: self.choiceButtonClicked1(button))
        self.pushButtons1.append(self.pushButton_1_21)

        self.pushButton_1_22 = QtWidgets.QPushButton(self.tab)
        self.pushButton_1_22.setGeometry(QtCore.QRect(660, 200, 113, 32))
        self.pushButton_1_22.setObjectName("pushButton_1_22")
        self.pushButton_1_22.clicked.connect(lambda ch, button=self.pushButton_1_22: self.choiceButtonClicked1(button))
        self.pushButtons1.append(self.pushButton_1_22)

        self.pushButton_1_23 = QtWidgets.QPushButton(self.tab)
        self.pushButton_1_23.setGeometry(QtCore.QRect(660, 170, 113, 32))
        self.pushButton_1_23.setObjectName("pushButton_1_23")
        self.pushButton_1_23.clicked.connect(lambda ch, button=self.pushButton_1_23: self.choiceButtonClicked1(button))
        self.pushButtons1.append(self.pushButton_1_23)

        self.pushButton_1_24 = QtWidgets.QPushButton(self.tab)
        self.pushButton_1_24.setGeometry(QtCore.QRect(660, 110, 113, 32))
        self.pushButton_1_24.setObjectName("pushButton_1_24")
        self.pushButton_1_24.clicked.connect(lambda ch, button=self.pushButton_1_24: self.choiceButtonClicked1(button))
        self.pushButtons1.append(self.pushButton_1_24)

        self.pushButton_1_25 = QtWidgets.QPushButton(self.tab)
        self.pushButton_1_25.setGeometry(QtCore.QRect(660, 80, 113, 32))
        self.pushButton_1_25.setObjectName("pushButton_46")
        self.pushButton_1_25.clicked.connect(lambda ch, button=self.pushButton_1_25: self.choiceButtonClicked1(button))
        self.pushButtons1.append(self.pushButton_1_25)

         ################################################################# SECOND TAB ##################################################################################################################
        # SECOND TAB
        Tab3.addTab(self.tab, "")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("Tab_2")

        self.lineEdit_2_1 = QtWidgets.QLineEdit(self.tab1)
        self.lineEdit_2_1.setGeometry(QtCore.QRect(90, 10, 751, 41))
        self.lineEdit_2_1.setObjectName("lineEdit_2_1")
        self.lineEdit_2_1.returnPressed.connect(self.lineEdit_returnPressed2)

        self.lineEdit_2_2 = QtWidgets.QLineEdit(self.tab1)
        self.lineEdit_2_2.setGeometry(QtCore.QRect(110, 280, 751, 41))
        self.lineEdit_2_2.setObjectName("lineEdit_2_2")
        self.lineEdit_2_2.returnPressed.connect(self.lineEdit_returnPressed2)

        self.pushButton_2_1 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_2_1.setGeometry(QtCore.QRect(410, 60, 113, 32))
        self.pushButton_2_1.setObjectName("pushButton")
        self.pushButton_2_1.clicked.connect(lambda ch, button=self.pushButton_2_1: self.choiceButtonClicked2(button))
        self.pushButtons2.append(self.pushButton_2_1)

        self.pushButton_2_2 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_2_2.setGeometry(QtCore.QRect(300, 90, 113, 32))
        self.pushButton_2_2.setObjectName("pushButton_2")
        self.pushButton_2_2.clicked.connect(lambda ch, button=self.pushButton_2_2: self.choiceButtonClicked2(button))
        self.pushButtons2.append(self.pushButton_2_2)

        self.pushButton_2_3 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_2_3.setGeometry(QtCore.QRect(410, 90, 113, 32))
        self.pushButton_2_3.setObjectName("pushButton_2_3")
        self.pushButton_2_3.clicked.connect(lambda ch, button=self.pushButton_2_3: self.choiceButtonClicked2(button))
        self.pushButtons2.append(self.pushButton_2_3)

        self.pushButton_2_4 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_2_4.setGeometry(QtCore.QRect(520, 90, 113, 32))
        self.pushButton_2_4.setObjectName("pushButton_2_4")
        self.pushButton_2_4.clicked.connect(lambda ch, button=self.pushButton_2_4: self.choiceButtonClicked2(button))
        self.pushButtons2.append(self.pushButton_2_4)

        self.pushButton_2_5 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_2_5.setGeometry(QtCore.QRect(240, 120, 113, 32))
        self.pushButton_2_5.setObjectName("pushButton_2_5")
        self.pushButton_2_5.clicked.connect(lambda ch, button=self.pushButton_2_5: self.choiceButtonClicked2(button))
        self.pushButtons2.append(self.pushButton_2_5)

        self.pushButton_2_6 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_2_6.setGeometry(QtCore.QRect(350, 120, 113, 32))
        self.pushButton_2_6.setObjectName("pushButton_2_6")
        self.pushButton_2_6.clicked.connect(lambda ch, button=self.pushButton_2_6: self.choiceButtonClicked2(button))
        self.pushButtons2.append(self.pushButton_2_6)

        self.pushButton_2_7 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_2_7.setGeometry(QtCore.QRect(460, 120, 113, 32))
        self.pushButton_2_7.setObjectName("pushButton_2_7")
        self.pushButton_2_7.clicked.connect(lambda ch, button=self.pushButton_2_7: self.choiceButtonClicked2(button))
        self.pushButtons2.append(self.pushButton_2_7)

        self.pushButton_2_8 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_2_8.setGeometry(QtCore.QRect(570, 120, 113, 32))
        self.pushButton_2_8.setObjectName("pushButton_2_8")
        self.pushButton_2_8.clicked.connect(lambda ch, button=self.pushButton_2_8: self.choiceButtonClicked2(button))
        self.pushButtons2.append(self.pushButton_2_8)

        self.pushButton_2_9 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_2_9.setGeometry(QtCore.QRect(400, 150, 113, 32))
        self.pushButton_2_9.setObjectName("pushButton_2_9")
        self.pushButton_2_9.clicked.connect(lambda ch, button=self.pushButton_2_9: self.choiceButtonClicked2(button))
        self.pushButtons2.append(self.pushButton_2_9)

        self.pushButton_2_10 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_2_10.setGeometry(QtCore.QRect(180, 150, 113, 32))
        self.pushButton_2_10.setObjectName("pushButton_2_10")
        self.pushButton_2_10.clicked.connect(lambda ch, button=self.pushButton_2_10: self.choiceButtonClicked2(button))
        self.pushButtons2.append(self.pushButton_2_10)

        self.pushButton_2_11 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_2_11.setGeometry(QtCore.QRect(510, 150, 113, 32))
        self.pushButton_2_11.setObjectName("pushButton_2_11")
        self.pushButton_2_11.clicked.connect(lambda ch, button=self.pushButton_2_11: self.choiceButtonClicked2(button))
        self.pushButtons2.append(self.pushButton_2_11)

        self.pushButton_2_12 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_2_12.setGeometry(QtCore.QRect(290, 150, 113, 32))
        self.pushButton_2_12.setObjectName("pushButton_2_12")
        self.pushButton_2_12.clicked.connect(lambda ch, button=self.pushButton_2_12: self.choiceButtonClicked2(button))
        self.pushButtons2.append(self.pushButton_2_12)

        self.pushButton_2_14 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_2_14.setGeometry(QtCore.QRect(620, 150, 113, 32))
        self.pushButton_2_14.setObjectName("pushButton_2_14")
        self.pushButton_2_14.clicked.connect(lambda ch, button=self.pushButton_2_14: self.choiceButtonClicked2(button))
        self.pushButtons2.append(self.pushButton_2_14)

        self.pushButton_2_13 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_2_13.setGeometry(QtCore.QRect(460, 180, 113, 32))
        self.pushButton_2_13.setObjectName("pushButton_2_13")
        self.pushButton_2_13.clicked.connect(lambda ch, button=self.pushButton_2_13: self.choiceButtonClicked2(button))
        self.pushButtons2.append(self.pushButton_2_13)

        self.pushButton_2_15 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_2_15.setGeometry(QtCore.QRect(240, 180, 113, 32))
        self.pushButton_2_15.setObjectName("pushButton_2_15")
        self.pushButton_2_15.clicked.connect(lambda ch, button=self.pushButton_2_15: self.choiceButtonClicked2(button))
        self.pushButtons2.append(self.pushButton_2_15)

        self.pushButton_2_16 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_2_16.setGeometry(QtCore.QRect(570, 180, 113, 32))
        self.pushButton_2_16.setObjectName("pushButton_2_16")
        self.pushButton_2_16.clicked.connect(lambda ch, button=self.pushButton_2_16: self.choiceButtonClicked2(button))
        self.pushButtons2.append(self.pushButton_2_16)

        self.pushButton_2_17 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_2_17.setGeometry(QtCore.QRect(350, 180, 113, 32))
        self.pushButton_2_17.setObjectName("pushButton_2_17")
        self.pushButton_2_17.clicked.connect(lambda ch, button=self.pushButton_2_17: self.choiceButtonClicked2(button))
        self.pushButtons2.append(self.pushButton_2_17)

        self.pushButton_2_18 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_2_18.setGeometry(QtCore.QRect(520, 210, 113, 32))
        self.pushButton_2_18.setObjectName("pushButton_2_18")
        self.pushButton_2_18.clicked.connect(lambda ch, button=self.pushButton_2_18: self.choiceButtonClicked2(button))
        self.pushButtons2.append(self.pushButton_2_18)

        self.pushButton_2_19 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_2_19.setGeometry(QtCore.QRect(300, 210, 113, 32))
        self.pushButton_2_19.setObjectName("pushButton_2_19")
        self.pushButton_2_19.clicked.connect(lambda ch, button=self.pushButton_2_19: self.choiceButtonClicked2(button))
        self.pushButtons2.append(self.pushButton_2_19)

        self.pushButton_2_20 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_2_20.setGeometry(QtCore.QRect(410, 210, 113, 32))
        self.pushButton_2_20.setObjectName("pushButton_2_20")
        self.pushButton_2_20.clicked.connect(lambda ch, button=self.pushButton_2_20: self.choiceButtonClicked2(button))
        self.pushButtons2.append(self.pushButton_2_20)

        self.pushButton_2_21 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_2_21.setGeometry(QtCore.QRect(410, 240, 113, 32))
        self.pushButton_2_21.setObjectName("pushButton_2_21")
        self.pushButton_2_21.clicked.connect(lambda ch, button=self.pushButton_2_21: self.choiceButtonClicked2(button))
        self.pushButtons2.append(self.pushButton_2_21)

        ################################################################# THIRD TAB ##################################################################################################################
        # THIRD TAB
        Tab3.addTab(self.tab1, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        
        self.lineEdit_3_1 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_3_1.setGeometry(QtCore.QRect(360, 10, 221, 41))
        self.lineEdit_3_1.setObjectName("lineEdit_3_2")
        self.lineEdit_3_1.returnPressed.connect(self.lineEdit_returnPressed3)

        self.lineEdit_3_2 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_3_2.setGeometry(QtCore.QRect(360, 370, 241, 41))
        self.lineEdit_3_2.setObjectName("lineEdit_3_1")
        self.lineEdit_3_2.returnPressed.connect(self.lineEdit_returnPressed3)

        self.pushButton_3_1 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3_1.setGeometry(QtCore.QRect(420, 60, 113, 32))
        self.pushButton_3_1.setObjectName("pushButton_3_1")
        self.pushButton_3_1.clicked.connect(lambda ch, button=self.pushButton_3_1: self.choiceButtonClicked3(button))
        self.pushButtons3.append(self.pushButton_3_1)

        self.pushButton_3_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3_2.setGeometry(QtCore.QRect(420, 90, 113, 32))
        self.pushButton_3_2.setObjectName("pushButton_3_2")
        self.pushButton_3_2.clicked.connect(lambda ch, button=self.pushButton_3_2: self.choiceButtonClicked3(button))
        self.pushButtons3.append(self.pushButton_3_2)

        self.pushButton_3_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3_3.setGeometry(QtCore.QRect(420, 120, 113, 32))
        self.pushButton_3_3.setObjectName("pushButton_3_3")
        self.pushButton_3_3.clicked.connect(lambda ch, button=self.pushButton_3_3: self.choiceButtonClicked3(button))
        self.pushButtons3.append(self.pushButton_3_3)

        self.pushButton_3_4 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3_4.setGeometry(QtCore.QRect(420, 150, 113, 32))
        self.pushButton_3_4.setObjectName("pushButton_3_4")
        self.pushButton_3_4.clicked.connect(lambda ch, button=self.pushButton_3_4: self.choiceButtonClicked3(button))
        self.pushButtons3.append(self.pushButton_3_4)

        self.pushButton_3_5 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3_5.setGeometry(QtCore.QRect(420, 180, 113, 32))
        self.pushButton_3_5.setObjectName("pushButton_51")
        self.pushButton_3_5.clicked.connect(lambda ch, button=self.pushButton_3_5: self.choiceButtonClicked3(button))
        self.pushButtons3.append(self.pushButton_3_5)

        self.pushButton_3_6 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3_6.setGeometry(QtCore.QRect(420, 210, 113, 32))
        self.pushButton_3_6.setObjectName("pushButton_52")
        self.pushButton_3_6.clicked.connect(lambda ch, button=self.pushButton_3_6: self.choiceButtonClicked3(button))
        self.pushButtons3.append(self.pushButton_3_6)

        self.pushButton_3_7 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3_7.setGeometry(QtCore.QRect(420, 240, 113, 32))
        self.pushButton_3_7.setObjectName("pushButton_3_7")
        self.pushButton_3_7.clicked.connect(lambda ch, button=self.pushButton_3_7: self.choiceButtonClicked3(button))
        self.pushButtons3.append(self.pushButton_3_7)

        self.pushButton_3_8 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3_8.setGeometry(QtCore.QRect(420, 270, 113, 32))
        self.pushButton_3_8.setObjectName("pushButton_3_8")
        self.pushButton_3_8.clicked.connect(lambda ch, button=self.pushButton_3_8: self.choiceButtonClicked3(button))
        self.pushButtons3.append(self.pushButton_3_8)

        self.pushButton_3_9 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3_9.setGeometry(QtCore.QRect(420, 300, 113, 32))
        self.pushButton_3_9.setObjectName("pushButton_3_9")
        self.pushButton_3_9.clicked.connect(lambda ch, button=self.pushButton_3_9: self.choiceButtonClicked3(button))
        self.pushButtons3.append(self.pushButton_3_9)

        self.pushButton_3_10 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3_10.setGeometry(QtCore.QRect(420, 330, 113, 32))
        self.pushButton_3_10.setObjectName("pushButton_3_10")
        self.pushButton_3_10.clicked.connect(lambda ch, button=self.pushButton_3_10: self.choiceButtonClicked3(button))
        self.pushButtons3.append(self.pushButton_3_10)
        
        Tab3.addTab(self.tab_3, "")

        ################################################################# FOURTH TAB ##################################################################################################################
        # FOURTH TAB (4th tab)

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        
        self.lineEdit_4_1 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4_1.setGeometry(QtCore.QRect(100, 30, 301, 231))
        self.lineEdit_4_1.setObjectName("lineEdit_4_1")
        self.lineEdit_4_1.returnPressed.connect(self.lineEdit_returnPressed4)
        
        self.lineEdit_4_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4_2.setGeometry(QtCore.QRect(530, 320, 281, 301))
        self.lineEdit_4_2.setObjectName("lineEdit_4_2")
        self.lineEdit_4_2.returnPressed.connect(self.lineEdit_returnPressed4)
        
        self.pushButton_4_1 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4_1.setGeometry(QtCore.QRect(410, 60, 113, 32))
        self.pushButton_4_1.setObjectName("pushButton_4_1")
        self.pushButton_4_1.clicked.connect(lambda ch, button=self.pushButton_4_1: self.choiceButtonClicked4(button))
        self.pushButtons4.append(self.pushButton_4_1)

        self.pushButton_4_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4_2.setGeometry(QtCore.QRect(410, 30, 113, 32))
        self.pushButton_4_2.setObjectName("pushButton_4_2")
        self.pushButton_4_2.clicked.connect(lambda ch, button=self.pushButton_4_2: self.choiceButtonClicked4(button))
        self.pushButtons4.append(self.pushButton_4_2)

        self.pushButton_4_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4_3.setGeometry(QtCore.QRect(410, 120, 113, 32))
        self.pushButton_4_3.setObjectName("pushButton_4_3")
        self.pushButton_4_3.clicked.connect(lambda ch, button=self.pushButton_4_3: self.choiceButtonClicked4(button))
        self.pushButtons4.append(self.pushButton_4_3)

        self.pushButton_4_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4_4.setGeometry(QtCore.QRect(410, 150, 113, 32))
        self.pushButton_4_4.setObjectName("pushButton_4_4")
        self.pushButton_4_4.clicked.connect(lambda ch, button=self.pushButton_4_4: self.choiceButtonClicked4(button))
        self.pushButtons4.append(self.pushButton_4_4)

        self.pushButton_4_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4_5.setGeometry(QtCore.QRect(410, 210, 113, 32))
        self.pushButton_4_5.setObjectName("pushButton_4_5")
        self.pushButton_4_5.clicked.connect(lambda ch, button=self.pushButton_4_5: self.choiceButtonClicked4(button))
        self.pushButtons4.append(self.pushButton_4_5)

        self.pushButton_4_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4_6.setGeometry(QtCore.QRect(410, 180, 113, 32))
        self.pushButton_4_6.setObjectName("pushButton_4_6")
        self.pushButton_4_6.clicked.connect(lambda ch, button=self.pushButton_4_6: self.choiceButtonClicked4(button))
        self.pushButtons4.append(self.pushButton_4_6)

        self.pushButton_4_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4_7.setGeometry(QtCore.QRect(410, 270, 113, 32))
        self.pushButton_4_7.setObjectName("pushButton_4_7")
        self.pushButton_4_7.clicked.connect(lambda ch, button=self.pushButton_4_7: self.choiceButtonClicked4(button))
        self.pushButtons4.append(self.pushButton_4_7)

        self.pushButton_4_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4_8.setGeometry(QtCore.QRect(410, 240, 113, 32))
        self.pushButton_4_8.setObjectName("pushButton_4_8")
        self.pushButton_4_8.clicked.connect(lambda ch, button=self.pushButton_4_8: self.choiceButtonClicked4(button))
        self.pushButtons4.append(self.pushButton_4_8)

        self.pushButton_4_9 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4_9.setGeometry(QtCore.QRect(410, 90, 113, 32))
        self.pushButton_4_9.setObjectName("pushButton_4_9")
        self.pushButton_4_9.clicked.connect(lambda ch, button=self.pushButton_4_9: self.choiceButtonClicked4(button))
        self.pushButtons4.append(self.pushButton_4_9)

        self.pushButton_4_10 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4_10.setGeometry(QtCore.QRect(410, 300, 113, 32))
        self.pushButton_4_10.setObjectName("pushButton_4_10")
        self.pushButton_4_10.clicked.connect(lambda ch, button=self.pushButton_4_10: self.choiceButtonClicked4(button))
        self.pushButtons4.append(self.pushButton_4_10)

        self.pushButton_4_11 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4_11.setGeometry(QtCore.QRect(410, 450, 113, 32))
        self.pushButton_4_11.setObjectName("pushButton_4_11")
        self.pushButton_4_11.clicked.connect(lambda ch, button=self.pushButton_4_11: self.choiceButtonClicked4(button))
        self.pushButtons4.append(self.pushButton_4_11)

        self.pushButton_4_12 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4_12.setGeometry(QtCore.QRect(410, 360, 113, 32))
        self.pushButton_4_12.setObjectName("pushButton_4_12")
        self.pushButton_4_12.clicked.connect(lambda ch, button=self.pushButton_4_12: self.choiceButtonClicked4(button))
        self.pushButtons4.append(self.pushButton_4_12)

        self.pushButton_4_13 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4_13.setGeometry(QtCore.QRect(410, 420, 113, 32))
        self.pushButton_4_13.setObjectName("pushButton_4_13")
        self.pushButton_4_13.clicked.connect(lambda ch, button=self.pushButton_4_13: self.choiceButtonClicked4(button))
        self.pushButtons4.append(self.pushButton_4_13)

        self.pushButton_4_14 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4_14.setGeometry(QtCore.QRect(410, 540, 113, 32))
        self.pushButton_4_14.setObjectName("pushButton_4_14")
        self.pushButton_4_14.clicked.connect(lambda ch, button=self.pushButton_4_14: self.choiceButtonClicked4(button))
        self.pushButtons4.append(self.pushButton_4_14)

        self.pushButton_4_15 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4_15.setGeometry(QtCore.QRect(410, 390, 113, 32))
        self.pushButton_4_15.setObjectName("pushButton_4_15")
        self.pushButton_4_15.clicked.connect(lambda ch, button=self.pushButton_4_15: self.choiceButtonClicked4(button))
        self.pushButtons4.append(self.pushButton_4_15)

        self.pushButton_4_16 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4_16.setGeometry(QtCore.QRect(410, 330, 113, 32))
        self.pushButton_4_16.setObjectName("pushButton_4_16")
        self.pushButton_4_16.clicked.connect(lambda ch, button=self.pushButton_4_16: self.choiceButtonClicked4(button))
        self.pushButtons4.append(self.pushButton_4_16)

        self.pushButton_4_17 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4_17.setGeometry(QtCore.QRect(410, 600, 113, 32))
        self.pushButton_4_17.setObjectName("pushButton_4_18")
        self.pushButton_4_17.clicked.connect(lambda ch, button=self.pushButton_4_17: self.choiceButtonClicked4(button))
        self.pushButtons4.append(self.pushButton_4_17)

        self.pushButton_4_18 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4_18.setGeometry(QtCore.QRect(410, 510, 113, 32))
        self.pushButton_4_18.setObjectName("pushButton_4_19")
        self.pushButton_4_18.clicked.connect(lambda ch, button=self.pushButton_4_18: self.choiceButtonClicked4(button))
        self.pushButtons4.append(self.pushButton_4_18)

        self.pushButton_4_19 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4_19.setGeometry(QtCore.QRect(410, 480, 113, 32))
        self.pushButton_4_19.setObjectName("pushButton_4_20")
        self.pushButton_4_19.clicked.connect(lambda ch, button=self.pushButton_4_19: self.choiceButtonClicked4(button))
        self.pushButtons4.append(self.pushButton_4_19)

        self.pushButton_4_20 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4_20.setGeometry(QtCore.QRect(410, 570, 113, 32))
        self.pushButton_4_20.setObjectName("pushButton_76")
        self.pushButton_4_20.clicked.connect(lambda ch, button=self.pushButton_4_20: self.choiceButtonClicked4(button))
        self.pushButtons4.append(self.pushButton_4_20)

        Tab3.addTab(self.tab_2, "")

################################################################## END OF TAB PUSH BUTTONS #########################################################################################################

        self.retranslateUi(Tab3)
        Tab3.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Tab3)

    def retranslateUi(self, Tab3):
        _translate = QtCore.QCoreApplication.translate
        Tab3.setWindowTitle(_translate("Tab3", "Predictive TTS with User Input"))
        Tab3.setToolTip(_translate("Tab3", "<html><head/><body><p>Tab3</p><p><br/></p></body></html>"))
        Tab3.setTabText(Tab3.indexOf(self.tab), _translate("Tab3", "Tab 1"))
        Tab3.setTabText(Tab3.indexOf(self.tab1), _translate("Tab3", "Tab 2"))
        Tab3.setTabText(Tab3.indexOf(self.tab_3), _translate("Tab3", "Tab 3"))
        Tab3.setTabText(Tab3.indexOf(self.tab_2), _translate("Tab3", "Tab 4"))
        self.lineEdit_1_2.setPlaceholderText(_translate("Dialog", "Enter your text string here: "))
        self.lineEdit_1_1.setPlaceholderText(_translate("Dialog", "Text String: "))
        self.lineEdit_2_2.setPlaceholderText(_translate("Dialog", "Enter your text string here: "))
        self.lineEdit_2_1.setPlaceholderText(_translate("Dialog", "Text String: "))
        self.lineEdit_3_2.setPlaceholderText(_translate("Dialog", "Enter your text string here: "))
        self.lineEdit_3_1.setPlaceholderText(_translate("Dialog", "Text String: "))
        self.lineEdit_4_1.setPlaceholderText(_translate("Dialog", "Enter your text string here: "))
        self.lineEdit_4_2.setPlaceholderText(_translate("Dialog", "Text String: "))

################################################################## END OF RETRANSLATE #########################################################################################################

    def call_predictNext(self):
        self.pred.predictNext(self.text)

####################### LINE EDIT TAB1 ##################################################
    def lineEdit_returnPressed1(self):
        print(self.lineEdit_1_1.text())
        if self.lineEdit_1_1.text() == "Q":
          self.lineEdit_1_2.setText('')
          self.text1 = ''
          self.reopen = True
          self.dialog.close();
          return;

        print('Line Edit 1 return pressed')
        # add the new piece of text to class variable storing all (previous) text
        self.text1 += ' ' + self.lineEdit_1_1.text()
        # show text in lower line
        self.lineEdit_1_2.setText(self.text1)
        self.pred.set_stext(self.lineEdit_1_1.text())
        self.pred.play()
        # clean upper edit field for next input
        self.lineEdit_1_1.setText('')
        # do prediction
        result = self.pred.predictNext(self.text1)
        #print('text =', self.text)
        
        index = [i for i in range(1, (self.pred.predict_max + 1), 1)]
        df = pd.DataFrame(result, index=index)
        word_df = df[df["token"].str.contains("[!#$%&\'()*+,-./\:;<=>?@[\\]^_`{|}~»Â�…॥।1234567890]") == False]
        word_df = word_df.dropna().reset_index(drop=True)
        word_df = pd.DataFrame(word_df)
        word_df = word_df.sort_values(by=['token'], ascending=True, key=lambda col: col.str.lower())
        df = word_df
        
        print('\n predictions: \n')
        print(word_df['token'])
        
        #put the text predictions to the buttons
        iNoButton=int(0)
        for i in self.pushButtons1:
            if iNoButton < word_df['token'].count():
                i.setText(str(word_df['token'].iloc[iNoButton]))
                i.setEnabled(True)
            else:
                i.setText("")
                i.setEnabled(False)
            iNoButton +=1

    def getReopen(self):
        return self.reopen;
    
####################### LINE EDIT TAB2 ##################################################
    def lineEdit_returnPressed2(self):
        print(self.lineEdit_2_1.text())
        if self.lineEdit_2_1.text() == "Q":
          self.lineEdit_2_2.setText('')
          self.text2 = ''
          self.reopen = True
          self.dialog.close();
          return;

        print('Line Edit 2 return pressed')
        # add the new piece of text to class variable storing all (previous) text
        self.text2 += ' ' + self.lineEdit_2_1.text()
        # show text in lower line
        self.lineEdit_2_2.setText(self.text2)
        self.pred.set_stext(self.lineEdit_2_1.text());
        self.pred.play();
        # clean upper edit field for next input
        self.lineEdit_2_1.setText('')
        # do prediction
        result = self.pred.predictNext(self.text2)
        #print('text =', self.text)
        
        index = [i for i in range(1, (self.pred.predict_max + 1), 1)]
        df = pd.DataFrame(result, index=index)
        word_df = df[df["token"].str.contains("[!#$%&\'()*+,-./\:;<=>?@[\\]^_`{|}~»Â�…॥।1234567890]") == False]
        word_df = word_df.dropna().reset_index(drop=True)
        word_df = pd.DataFrame(word_df)
        word_df = word_df.sort_values(by=['token'], ascending=True, key=lambda col: col.str.lower())
        df = word_df
        
        print('\n predictions: \n')
        print(word_df['token'])
        
        #put the text predictions to the buttons
        iNoButton=int(0)
        for i in self.pushButtons2:
            if iNoButton < word_df['token'].count():
                i.setText(str(word_df['token'].iloc[iNoButton]))
                i.setEnabled(True)
            else:
                i.setText("")
                i.setEnabled(False)
            iNoButton +=1

    def getReopen(self):
        return self.reopen;

####################### LINE EDIT TAB3 ##################################################
    def lineEdit_returnPressed3(self):
        print(self.lineEdit_3_1.text())
        if self.lineEdit_3_1.text() == "Q":
          self.lineEdit_3_2.setText('')
          self.text3 = ''
          self.reopen = True
          self.dialog.close();
          return;

        print('Line Edit 3 return pressed')
        # add the new piece of text to class variable storing all (previous) text
        self.text3 += ' ' + self.lineEdit_3_1.text()
        # show text in lower line
        self.lineEdit_3_2.setText(self.text3)
        self.pred.set_stext(self.lineEdit_3_1.text());
        self.pred.play();
        # clean upper edit field for next input
        self.lineEdit_3_1.setText('')
        # do prediction
        result = self.pred.predictNext(self.text3)
        #print('text =', self.text)
        
        index = [i for i in range(1, (self.pred.predict_max + 1), 1)]
        df = pd.DataFrame(result, index=index)
        word_df = df[df["token"].str.contains("[!#$%&\'()*+,-./\:;<=>?@[\\]^_`{|}~»Â�…॥।1234567890]") == False]
        word_df = word_df.dropna().reset_index(drop=True)
        word_df = pd.DataFrame(word_df)
        word_df = word_df.sort_values(by=['token'], ascending=True, key=lambda col: col.str.lower())
        df = word_df
        
        print('\n predictions: \n')
        print(word_df['token'])
        
        #put the text predictions to the buttons
        iNoButton=int(0)
        for i in self.pushButtons3:
            if iNoButton < word_df['token'].count():
                i.setText(str(word_df['token'].iloc[iNoButton]))
                i.setEnabled(True)
            else:
                i.setText("")
                i.setEnabled(False)
            iNoButton +=1
    
    def getReopen(self):
        return self.reopen;

####################### LINE EDIT TAB4 ##################################################
    def lineEdit_returnPressed4(self):
        if self.lineEdit_4_1.text() == "Q":
          self.lineEdit_4_2.setText('')
          self.text4 = ''
          self.reopen = True
          self.dialog.close();
          return;

        print('Line Edit for tab 4 return pressed')
        # add the new piece of text to class variable storing all (previous) text
        self.text4 += ' ' + self.lineEdit_4_1.text()
        # show text in lower line
        self.lineEdit_4_2.setText(self.text4)
        self.pred.set_stext(self.lineEdit_4_1.text())
        self.pred.play()
        # clean upper edit field for next input
        self.lineEdit_4_1.setText('')
        # do prediction
        result = self.pred.predictNext(self.text4)
        #print('text =', self.text)
        
        index = [i for i in range(1, (self.pred.predict_max + 1), 1)]
        df = pd.DataFrame(result, index=index)
        word_df = df[df["token"].str.contains("[!#$%&\'()*+,-./\:;<=>?@[\\]^_`{|}~»Â�…॥।1234567890]") == False]
        word_df = word_df.dropna().reset_index(drop=True)
        word_df = word_df.sort_values(by=['token'], ascending=True, key=lambda col: col.str.lower())
        word_df = pd.DataFrame(word_df)
        df = word_df
        
        print('\n predictions: \n')
        print(word_df['token'])
        
        #put the text predictions to the buttons
        iNoButton=int(0)
        for i in self.pushButtons4:
            if iNoButton < word_df['token'].count():
                i.setText(str(word_df['token'].iloc[iNoButton]))
                i.setEnabled(True)
            else:
                i.setText("")
                i.setEnabled(False)
            iNoButton +=1

    def getReopen(self):
        return self.reopen;

#################################################### CHOICE BUTTON CLICKED TAB 1 ####################################
    def choiceButtonClicked1(self, button):
        #print('Button no. ' + str(button) + ' was pressed...')
        print('Button pressed')
        print(button)
        print('This is the button in line')
        
        # add the new piece of text to class variable storing all (previous) text
        self.text1 += '' + button.text()
        # show text in lower line
        self.lineEdit_1_2.setText(self.text1)
        # clean upper edit field for next input
        self.lineEdit_1_1.setText('')
        # do prediction
        result = self.pred.predictNext(self.text1)
        # Play audio via TTS
        self.pred.set_stext(button.text());
        self.pred.play();
        
        index = [i for i in range(1, (self.pred.predict_max + 1), 1)]
        df = pd.DataFrame(result, index=index)
        word_df = df[df["token"].str.contains("[!#$%&\'()*+,-./\:;<=>?@[\\]^_`{|}~»Â�…॥।1234567890]") == False]
        word_df = word_df.dropna().reset_index(drop=True)
        word_df = word_df.sort_values(by=['token'], ascending=True, key=lambda col: col.str.lower())
        df = word_df
        
        print('\n predictions: \n')
        print(word_df['token'])

        iNoButton=int(0)
        for i in self.pushButtons1:
            if iNoButton < word_df['token'].count():
                i.setText(str(word_df['token'].iloc[iNoButton]))
                i.setEnabled(True)
            else:
                i.setText("")
                i.setEnabled(False)
            iNoButton +=1

##################################################### CHOICE BUTTON CLICKED TAB 2 ####################################
    def choiceButtonClicked2(self, button):
        #print('Button no. ' + str(button) + ' was pressed...')
        print('Button pressed')
        print(button)
        print('This is the button in line')
        
        # add the new piece of text to class variable storing all (previous) text
        self.text2 += '' + button.text()
        # show text in lower line
        self.lineEdit_2_2.setText(self.text2)
        # clean upper edit field for next input
        self.lineEdit_2_1.setText('')
        # do prediction
        result = self.pred.predictNext(self.text2)
        # Play audio via TTS
        self.pred.set_stext(button.text());
        self.pred.play();
        
        index = [i for i in range(1, (self.pred.predict_max + 1), 1)]
        df = pd.DataFrame(result, index=index)
        word_df = df[df["token"].str.contains("[!#$%&\'()*+,-./\:;<=>?@[\\]^_`{|}~»Â�…॥।1234567890]") == False]
        word_df = word_df.dropna().reset_index(drop=True)
        word_df = word_df.sort_values(by=['token'], ascending=True, key=lambda col: col.str.lower())
        df = word_df
        
        print('\n predictions: \n')
        print(word_df['token'])

        iNoButton=int(0)
        for i in self.pushButtons2:
            if iNoButton < word_df['token'].count():
                i.setText(str(word_df['token'].iloc[iNoButton]))
                i.setEnabled(True)
            else:
                i.setText("")
                i.setEnabled(False)
            iNoButton +=1

##################################################### CHOICE BUTTON CLICKED TAB 3 ####################################
    def choiceButtonClicked3(self, button):
        #print('Button no. ' + str(button) + ' was pressed...')
        print('Button pressed')
        print(button)
        print('This is the button in line')
        
        # add the new piece of text to class variable storing all (previous) text
        self.text3 += '' + button.text()
        # show text in lower line
        self.lineEdit_3_2.setText(self.text3)
        # clean upper edit field for next input
        self.lineEdit_3_1.setText('')
        # do prediction
        result = self.pred.predictNext(self.text3)
        # Play audio via TTS
        self.pred.set_stext(button.text());
        self.pred.play();
        
        index = [i for i in range(1, (self.pred.predict_max + 1), 1)]
        df = pd.DataFrame(result, index=index)
        word_df = df[df["token"].str.contains("[!#$%&\'()*+,-./\:;<=>?@[\\]^_`{|}~»Â�…॥।1234567890]") == False]
        word_df = word_df.dropna().reset_index(drop=True)
        word_df = word_df.sort_values(by=['token'], ascending=True, key=lambda col: col.str.lower())
        df = word_df
        
        print('\n predictions: \n')
        print(word_df['token'])

        iNoButton=int(0)
        for i in self.pushButtons3:
            if iNoButton < word_df['token'].count():
                i.setText(str(word_df['token'].iloc[iNoButton]))
                i.setEnabled(True)
            else:
                i.setText("")
                i.setEnabled(False)
            iNoButton +=1

##################################################### CHOICE BUTTON CLICKED TAB 4 ####################################
    def choiceButtonClicked4(self, button):
        #print('Button no. ' + str(button) + ' was pressed...')
        print('Button pressed')
        print(button)
        print('This is the button in line')
        
        # add the new piece of text to class variable storing all (previous) text
        self.text4 += '' + button.text()
        # show text in lower line
        self.lineEdit_4_2.setText(self.text4)
        # clean upper edit field for next input
        self.lineEdit_4_1.setText('')
        # do prediction
        result = self.pred.predictNext(self.text4)
        # Play audio via TTS
        self.pred.set_stext(button.text());
        self.pred.play();
        
        index = [i for i in range(1, (self.pred.predict_max + 1), 1)]
        df = pd.DataFrame(result, index=index)
        word_df = df[df["token"].str.contains("[!#$%&\'()*+,-./\:;<=>?@[\\]^_`{|}~»Â�…॥।1234567890]") == False]
        word_df = word_df.dropna().reset_index(drop=True)
        word_df = word_df.sort_values(by=['token'], ascending=True, key=lambda col: col.str.lower())
        df = word_df
        
        print('\n predictions: \n')
        print(word_df['token'])

        iNoButton=int(0)
        for i in self.pushButtons4:
            if iNoButton < word_df['token'].count():
                i.setText(str(word_df['token'].iloc[iNoButton]))
                i.setEnabled(True)
            else:
                i.setText("")
                i.setEnabled(False)
            iNoButton +=1

################### GUI LAYOUT #################################
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tab3 = QtWidgets.QTabWidget()
    ui = Ui_Tab3()
    while ui.getReopen():
        ui.setupUi(Tab3)
        Tab3.show()
        app.exec()
    sys.exit(app.exec())