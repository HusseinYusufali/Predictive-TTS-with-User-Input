import sys
#from curses.ascii import isdigit
from gtts import gTTS #Import Google Text to Speech
from happytransformer import HappyWordPrediction
import pandas as pd 
from playsound import playsound as play
from autocorrect import Speller
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtCore import pyqtSlot
import pyttsx3 as t2s

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
        tts = gTTS((self.stext.replace('[MASK]','')))
        tts.save('1.wav')
        play('1.wav')


<<<<<<< Updated upstream:GUI Implementations/GUI.py
#Class for the UI layout
=======
class ttsHandler():
    t2s_engine = None
    rate = 0
    voices = None
    volume = 0
    
    def __init__(self):
        self.t2s_engine = t2s.init()
        
        self.rate = self.t2s_engine.getProperty('rate')
        self.t2s_engine.setProperty('rate', self.rate)
         
        self.volume = self.t2s_engine.getProperty('volume')
        self.t2s_engine.setProperty('volume ', self.volume )
        
        print('Current volume is '+str(self.volume ))
         
        self.voices = self.t2s_engine.getProperty('voices')    
        print('Available voices: ')
        print(str(self.voices))
        
        self.t2s_engine.setProperty('voice', self.voices[0].id)
        
    def speak(self,text):
        self.t2s_engine.say(text)
        self.t2s_engine.runAndWait()
        


>>>>>>> Stashed changes:GUI.py
class Ui_Dialog(object):    
    
    pred = predictor()     # instance of predictor class
    tts = ttsHandler()     # instance of tts class
    text = ''              # so far inputted text
    iLastButtonPressed = 0 
    reopen = True
    
    def setupUi(self, Dialog):
        self.reopen = False
        self.dialog = Dialog;
        Dialog.setObjectName("Dialog")
        Dialog.resize(512, 377)
        Dialog.setMouseTracking(True)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 10, 461, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.returnPressed.connect(self.lineEdit_returnPressed)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 210, 461, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        # self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        # self.lineEdit_3.setGeometry(QtCore.QRect(20, 210, 461, 41))
        # self.lineEdit_3.setObjectName("lineEdit_3")


        
        self.buttons = [];
        iNo = 0
        for i in range(30, 460, 110):
            button_column = []
            for j in range(60, 200, 30):
                button = QtWidgets.QPushButton(Dialog)
                button.setGeometry(QtCore.QRect(i, j, 113, 32))
                button.setMaximumSize(QtCore.QSize(113, 16777215))
                button.setDefault(False)
                button.setText(str(iNo))
                button.setAutoDefault(False)
                button.clicked.connect(self.call_predictNext)
                button.clicked.connect(lambda ch, button=button: self.choiceButtonClicked(button))
                button_column.append(button)
                iNo += 1
            self.buttons.append(button_column)

            for i in self.buttons:
                for j in i:
                    j.setText('')
                    j.setDefault(False)
                    j.setAutoDefault(False)

        self.retranslateUi(Dialog)
        #self.lineEdit.clicked.connect(self.lineEdit_returnPressed)
    
    def call_predictNext(self):
        self.pred.predictNext(self.text)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Predictive TTS with User Input"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Enter your text string here: "))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Text String: "))
        #self.lineEdit_3.setPlaceholderText(_translate("Dialog", "Enter Q to refresh"))
        
    def lineEdit_returnPressed(self):
        print(self.lineEdit.text())
        if self.lineEdit.text() == "Q":
          self.reopen = True
          self.dialog.close();
          return;
        # add the new piece of text to class variable storing all (previous) text
        self.text += ' ' + self.lineEdit.text()
        # show text in lower line
        self.lineEdit_2.setText(self.text)
        self.pred.set_stext(self.lineEdit.text());
        self.pred.play();
        # clean upper edit field for next input
        self.lineEdit.setText('')
        
        # send to TTS
        self.tts.speak(self.text)
        
        # do prediction
        result = self.pred.predictNext(self.text)
        #print('text =', self.text)
        
        index = [i for i in range(1, (self.pred.predict_max + 1), 1)]
        df = pd.DataFrame(result, index=index)
        word_df = df[df["token"].str.contains("[!#$%&\'()*+,-./\:;<=>?@[\\]^_`{|}~»Â�…॥।1234567890]") == False]
        word_df = word_df.dropna().reset_index(drop=True)
        word_df = pd.DataFrame(word_df)
        df = word_df
        
        print('\n predictions: \n')
        print(word_df['token'])
        
        #put the text predictions to the buttons
        iNoButton=int(0)
        for i in self.buttons:
            for j in i:
                if iNoButton < word_df['token'].count():
                    j.setText(str(word_df['token'].iloc[iNoButton]))
                    j.setEnabled(True)
                else:
                    j.setText("")
                    j.setEnabled(False)
                iNoButton +=1

    def pushButton_clicked(self):
        self.test_class.set_var(self.lineEdit.text());
        
    def pushButton_2_clicked(self):
        self.test_class.print_var();
        
    def pushButton_3_clicked(self):
        _translate = QtCore.QCoreApplication.translate

    def choiceButtonClicked(self, button):
        #print('Button no. ' + str(button) + ' was pressed...')
        print('Button pressed')
        print(button)
        print('This is the button in line')
        
        # add the new piece of text to class variable storing all (previous) text
        self.text += '' + button.text()
        # show text in lower line
        self.lineEdit_2.setText(self.text)
        # clean upper edit field for next input
        self.lineEdit.setText('')
        # send to TTS
        self.tts.speak(button.text())
        # do prediction
        result = self.pred.predictNext(self.text)
        # Play audio via TTS
        self.pred.set_stext(button.text());
        self.pred.play();
        
        index = [i for i in range(1, (self.pred.predict_max + 1), 1)]
        df = pd.DataFrame(result, index=index)
        word_df = df[df["token"].str.contains("[!#$%&\'()*+,-./\:;<=>?@[\\]^_`{|}~»Â�…॥।1234567890]") == False]
        word_df = word_df.dropna().reset_index(drop=True)
        word_df = pd.DataFrame(word_df)
        df = word_df
        
        print('\n predictions: \n')
        print(word_df['token'])

        iNoButton=int(0)
        for i in self.buttons:
            for j in i:
                if iNoButton < word_df['token'].count():
                    j.setText(str(word_df['token'].iloc[iNoButton]))
                    j.setEnabled(True)
                else:
                    j.setText("")
                    j.setEnabled(False)
                iNoButton +=1

    def getReopen(self):
        return self.reopen;

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    while ui.getReopen():
        ui.setupUi(Dialog)
        Dialog.show()
        app.exec()
    #sys.exit(app.exec_()) # pyQT5
    sys.exit()   # pyQT6
