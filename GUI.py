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

while True:

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
            
            #Function for TTS
            def play(self):
                tts = gTTS((self.stext.replace('[MASK]','')))
                tts.save('1.wav')
                play('1.wav')


        #Class for the UI layout
        class Ui_Dialog(object):    
            
            pred = predictor()     # instance of predictor class
            text = ''              # so far inputted text
            iLastButtonPressed = 0 
            
            def setupUi(self, Dialog):
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
                
            def lineEdit_returnPressed(self):
                print(self.lineEdit.text())
                
                # add the new piece of text to class variable storing all (previous) text
                self.text += ' ' + self.lineEdit.text()
                # show text in lower line
                self.lineEdit_2.setText(self.text)
                # clean upper edit field for next input
                self.lineEdit.setText('')
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
                print('*******adding new button texts********')
                for i in self.buttons:
                    for j in i:
                        j.setText(str(word_df['token'].iloc[iNoButton]))
                        iNoButton +=1
                        #print('iNoButton =',iNoButton)
                        #print(str(word_df['token'].iloc[iNoButton]))
                    
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
                # do prediction
                result = self.pred.predictNext(self.text)
                
                index = [i for i in range(1, (self.pred.predict_max + 1), 1)]
                df = pd.DataFrame(result, index=index)
                word_df = df[df["token"].str.contains("[!#$%&\'()*+,-./\:;<=>?@[\\]^_`{|}~»Â�…॥।1234567890]") == False]
                word_df = word_df.dropna().reset_index(drop=True)
                word_df = pd.DataFrame(word_df)
                df = word_df
                
                print('\n predictions: \n')
                print(word_df['token'])

                # put text to the buttons
                iNoButton=int(0)
                for i in self.buttons:
                    for j in i:
                        j.setText(str(word_df['token'].iloc[iNoButton]))
                        iNoButton +=1

                #play(str(self.text))

        if __name__ == "__main__":
            import sys
            app = QtWidgets.QApplication(sys.argv)
            Dialog = QtWidgets.QDialog()
            ui = Ui_Dialog()
            ui.setupUi(Dialog)
            Dialog.show()
            #sys.exit(app.exec_()) # pyQT5
            sys.exit(app.exec())   # pyQT6