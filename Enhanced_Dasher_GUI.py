import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from happytransformer import HappyWordPrediction
import pandas as pd
from autocorrect import Speller
import pyttsx3
import time
import pandas as pd
from pathlib import Path
import logging

class HoverPushButton(QtWidgets.QPushButton):
    def __init__(self, arg):
        super().__init__(arg)
        # Without enabling tracking, mouse is only tracked when a button is pressed
        self.setMouseTracking(True)
        # This will be a handle to the method to forward mouse movement events to
        self.interactionHandler = None;
        # Disable the button by default as it started with no word
        self.setEnabled(False);

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        # Only handle button if it's enabled (e.g. it has a word)
        if self.isEnabled():
            if event.type() == QtCore.QEvent.Type.MouseMove:
                if not self.interactionHandler is None:
                    self.interactionHandler(self);

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
        self.model_path = "/Users/husseinyusufali/Desktop/PhD/Main PhD Folder/PhD - Year 2/Technical System Implementation/Predictive TransformerTTS/Transformer Models/modelroberta_aac"
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
    logging.basicConfig(filename='Participant_1_RoBERTa_AAC_Alphabetical_GUI_2_log-file2_MouseHover.log',
                        filemode='a',
                        format='%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s',
                        level=logging.INFO)
    logging.info('########################### Start Program Participant 1 ###########################')
    pred = predictor()     # instance of predictor class
    text1 = ''              # so far inputted text
    iLastButtonPressed = 0 
    reopen = True

    start_time = None
    stop_time = None

class Ui_Enhanced_Dasher_GUI(object):
    def setupUi(self, Enhanced_Dasher_GUI):
        Enhanced_Dasher_GUI.setObjectName("Enhanced_Dasher_GUI")
        Enhanced_Dasher_GUI.resize(931, 548)
        self.reopen = False
        self.dialog = Enhanced_Dasher_GUI;
        self.count = 0
        Enhanced_Dasher_GUI.setMouseTracking(False)
        Enhanced_Dasher_GUI.setAcceptDrops(False)
        Enhanced_Dasher_GUI.setAutoFillBackground(True)
        Enhanced_Dasher_GUI.setUsesScrollButtons(False)
        Enhanced_Dasher_GUI.setDocumentMode(False)
        Enhanced_Dasher_GUI.setTabsClosable(True)
        Enhanced_Dasher_GUI.setMovable(True)
        Enhanced_Dasher_GUI.setTabBarAutoHide(False)

        self.pushButtons_A = []
        self.pushButtons_W = []

        self.pushButton_A_1 = QtWidgets.QPushButton(Enhanced_Dasher_GUI)
        self.pushButton_A_1.setGeometry(QtCore.QRect(120, 70, 113, 32))
        self.pushButton_A_1.setObjectName("pushButton_A_1")

        self.pushButton_A_2 = QtWidgets.QPushButton(Enhanced_Dasher_GUI)
        self.pushButton_A_2.setGeometry(QtCore.QRect(120, 100, 113, 32))
        self.pushButton_A_2.setObjectName("pushButton_A_2")

        self.pushButton_A_3 = QtWidgets.QPushButton(Enhanced_Dasher_GUI)
        self.pushButton_A_3.setGeometry(QtCore.QRect(120, 130, 113, 32))
        self.pushButton_A_3.setObjectName("pushButton_A_3")

        self.pushButton_A_4 = QtWidgets.QPushButton(Enhanced_Dasher_GUI)
        self.pushButton_A_4.setGeometry(QtCore.QRect(120, 160, 113, 32))
        self.pushButton_A_4.setObjectName("pushButton_A_4")

        self.pushButton_A_5 = QtWidgets.QPushButton(Enhanced_Dasher_GUI)
        self.pushButton_A_5.setGeometry(QtCore.QRect(120, 190, 113, 32))
        self.pushButton_A_5.setObjectName("pushButton_A_5")

        self.pushButton_A_6 = QtWidgets.QPushButton(Enhanced_Dasher_GUI)
        self.pushButton_A_6.setGeometry(QtCore.QRect(120, 220, 113, 32))
        self.pushButton_A_6.setObjectName("pushButton_A_6")

        self.pushButton_A_7 = QtWidgets.QPushButton(Enhanced_Dasher_GUI)
        self.pushButton_A_7.setGeometry(QtCore.QRect(120, 250, 113, 32))
        self.pushButton_A_7.setObjectName("pushButton_A_7")

        self.pushButton_A_8 = QtWidgets.QPushButton(Enhanced_Dasher_GUI)
        self.pushButton_A_8.setGeometry(QtCore.QRect(120, 280, 113, 32))
        self.pushButton_A_8.setObjectName("pushButton_A_8")

        self.pushButton_A_9 = QtWidgets.QPushButton(Enhanced_Dasher_GUI)
        self.pushButton_A_9.setGeometry(QtCore.QRect(120, 310, 113, 32))
        self.pushButton_A_9.setObjectName("pushButton_A_9")

        self.pushButton_A_10 = QtWidgets.QPushButton(Enhanced_Dasher_GUI)
        self.pushButton_A_10.setGeometry(QtCore.QRect(120, 340, 113, 32))
        self.pushButton_A_10.setObjectName("pushButton_A_10")

        self.pushButton_W_1 = QtWidgets.QPushButton(Enhanced_Dasher_GUI)
        self.pushButton_W_1.setGeometry(QtCore.QRect(390, 60, 113, 32))
        self.pushButton_W_1.setObjectName("pushButton_W_1")
        self.pushButton_W_1.interactionHandler = self.choiceButtonClicked1;

        self.pushButton_W_2 = QtWidgets.QPushButton(Enhanced_Dasher_GUI)
        self.pushButton_W_2.setGeometry(QtCore.QRect(500, 80, 113, 32))
        self.pushButton_W_2.setObjectName("pushButton_W_2")
        self.pushButton_W_2.interactionHandler = self.choiceButtonClicked1;

        self.pushButton_W_3 = QtWidgets.QPushButton(Enhanced_Dasher_GUI)
        self.pushButton_W_3.setGeometry(QtCore.QRect(580, 110, 113, 32))
        self.pushButton_W_3.setObjectName("pushButton_W_3")
        self.pushButton_W_3.interactionHandler = self.choiceButtonClicked1;

        self.pushButton_W_4 = QtWidgets.QPushButton(Enhanced_Dasher_GUI)
        self.pushButton_W_4.setGeometry(QtCore.QRect(640, 140, 113, 32))
        self.pushButton_W_4.setObjectName("pushButton_W_4")
        self.pushButton_W_4.interactionHandler = self.choiceButtonClicked1;

        self.pushButton_W_5 = QtWidgets.QPushButton(Enhanced_Dasher_GUI)
        self.pushButton_W_5.setGeometry(QtCore.QRect(700, 170, 113, 32))
        self.pushButton_W_5.setObjectName("pushButton_W_5")
        self.pushButton_W_5.interactionHandler = self.choiceButtonClicked1;

        self.pushButton_W_6 = QtWidgets.QPushButton(Enhanced_Dasher_GUI)
        self.pushButton_W_6.setGeometry(QtCore.QRect(700, 210, 113, 32))
        self.pushButton_W_6.setObjectName("pushButton_W_6")
        self.pushButton_W_6.interactionHandler = self.choiceButtonClicked1;

        self.pushButton_W_7 = QtWidgets.QPushButton(Enhanced_Dasher_GUI)
        self.pushButton_W_7.setGeometry(QtCore.QRect(640, 240, 113, 32))
        self.pushButton_W_7.setObjectName("pushButton_W_7")
        self.pushButton_W_7.interactionHandler = self.choiceButtonClicked1;

        self.pushButton_W_8 = QtWidgets.QPushButton(Enhanced_Dasher_GUI)
        self.pushButton_W_8.setGeometry(QtCore.QRect(570, 270, 113, 32))
        self.pushButton_W_8.setObjectName("pushButton_W_8")
        self.pushButton_W_8.interactionHandler = self.choiceButtonClicked1;

        self.pushButton_W_9 = QtWidgets.QPushButton(Enhanced_Dasher_GUI)
        self.pushButton_W_9.setGeometry(QtCore.QRect(490, 300, 113, 32))
        self.pushButton_W_9.setObjectName("pushButton_W_9")
        self.pushButton_W_9.interactionHandler = self.choiceButtonClicked1;

        self.pushButton_W_10 = QtWidgets.QPushButton(Enhanced_Dasher_GUI)
        self.pushButton_W_10.setGeometry(QtCore.QRect(390, 330, 113, 32))
        self.pushButton_W_10.setObjectName("pushButton_W_10")
        self.pushButton_W_10.interactionHandler = self.choiceButtonClicked1;

        self.lineEdit_1 = QtWidgets.QLineEdit(Enhanced_Dasher_GUI)
        self.lineEdit_1.setGeometry(QtCore.QRect(280, 180, 401, 41))
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_1.returnPressed.connect(self.lineEdit_returnPressed1)
        self.lineEdit_1.textEdited.connect(lambda ch, lineedit=self.lineEdit_1_1: self.lineEditEdited(lineedit))

        self.lineEdit_2 = QtWidgets.QLineEdit(Enhanced_Dasher_GUI)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 390, 691, 51))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.returnPressed.connect(self.lineEdit_returnPressed1)

        self.pushButtons_W.append(self.pushButton_W_1)
        self.pushButtons_W.append(self.pushButton_W_2)
        self.pushButtons_W.append(self.pushButton_W_3)
        self.pushButtons_W.append(self.pushButton_W_4)
        self.pushButtons_W.append(self.pushButton_W_5)
        self.pushButtons_W.append(self.pushButton_W_6)
        self.pushButtons_W.append(self.pushButton_W_7)
        self.pushButtons_W.append(self.pushButton_W_8)
        self.pushButtons_W.append(self.pushButton_W_9)
        self.pushButtons_W.append(self.pushButton_W_10)

        self.pushButtons_A.append(self.pushButton_A_1)
        self.pushButtons_A.append(self.pushButton_A_2)
        self.pushButtons_A.append(self.pushButton_A_3)
        self.pushButtons_A.append(self.pushButton_A_4)
        self.pushButtons_A.append(self.pushButton_A_5)
        self.pushButtons_A.append(self.pushButton_A_6)
        self.pushButtons_A.append(self.pushButton_A_7)
        self.pushButtons_A.append(self.pushButton_A_8)
        self.pushButtons_A.append(self.pushButton_A_9)
        self.pushButtons_A.append(self.pushButton_A_10)

        self.retranslateUi(Enhanced_Dasher_GUI)
        QtCore.QMetaObject.connectSlotsByName(Enhanced_Dasher_GUI)

    def retranslateUi(self, Enhanced_Dasher_GUI):
        _translate = QtCore.QCoreApplication.translate
        Enhanced_Dasher_GUI.setWindowTitle(_translate("Enhanced_Dasher_GUI", "Form"))
        self.pushButton_A_3.setText(_translate("Enhanced_Dasher_GUI", "PushButton"))
        self.pushButton_W_7.setText(_translate("Enhanced_Dasher_GUI", "PushButton"))
        self.pushButton_A_4.setText(_translate("Enhanced_Dasher_GUI", "PushButton"))
        self.pushButton_W_1.setText(_translate("Enhanced_Dasher_GUI", "PushButton"))
        self.pushButton_W_10.setText(_translate("Enhanced_Dasher_GUI", "PushButton"))
        self.pushButton_A_10.setText(_translate("Enhanced_Dasher_GUI", "PushButton"))
        self.pushButton_W_6.setText(_translate("Enhanced_Dasher_GUI", "PushButton"))
        self.pushButton_W_2.setText(_translate("Enhanced_Dasher_GUI", "PushButton"))
        self.pushButton_A_9.setText(_translate("Enhanced_Dasher_GUI", "PushButton"))
        self.pushButton_A_5.setText(_translate("Enhanced_Dasher_GUI", "PushButton"))
        self.pushButton_W_9.setText(_translate("Enhanced_Dasher_GUI", "PushButton"))
        self.pushButton_W_5.setText(_translate("Enhanced_Dasher_GUI", "PushButton"))
        self.pushButton_A_1.setText(_translate("Enhanced_Dasher_GUI", "PushButton"))
        self.pushButton_A_7.setText(_translate("Enhanced_Dasher_GUI", "PushButton"))
        self.pushButton_W_8.setText(_translate("Enhanced_Dasher_GUI", "PushButton"))
        self.pushButton_A_2.setText(_translate("Enhanced_Dasher_GUI", "PushButton"))
        self.pushButton_A_8.setText(_translate("Enhanced_Dasher_GUI", "PushButton"))
        self.pushButton_W_4.setText(_translate("Enhanced_Dasher_GUI", "PushButton"))
        self.pushButton_A_6.setText(_translate("Enhanced_Dasher_GUI", "PushButton"))
        self.pushButton_W_3.setText(_translate("Enhanced_Dasher_GUI", "PushButton"))


    def call_predictNext(self):
        self.pred.predictNext(self.text)

    def lineEdit_returnPressed1(self):
        logging.info(self.lineEdit_1.text())
        if self.lineEdit_1.text() == "Q":
            global utterance_stop
            self.stop_time = time.time()
            self.reset()
            global duration_per_utterance
            duration_per_utterance = self.stop_time - self.start_time
            self.start_time = None
        else:
            #print('Line Edit 1 return pressed')
            # add the new piece of text to class variable storing all (previous) text
            self.text1 += ' ' + self.lineEdit_1_1.text()
            # show text in lower line
            self.lineEdit_2.setText(self.text1)
            self.pred.set_stext(self.lineEdit_1.text())
            self.pred.play()
            # clean upper edit field for next input
            self.lineEdit_1.setText('')
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
            
            # print('\n predictions: \n')
            # print(word_df['token'])
            
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

    def reset(self):
        self.stop_time = time.time()
        self.text1 = ""
        self.lineEdit_1.setText("")
        self.lineEdit_2.setText("")
        i = 1
        for p in self.pushButtons_W:
            p.setText(str(i))
            p.setEnabled(False)
            i+=1
        i = 1

        global words_per_minute
        duration_per_utterance = self.stop_time - self.start_time
        words_per_minute = ((int(self.number_of_words) / duration_per_utterance)*60)
        words_per_minute = round(words_per_minute, 3)

        logging.info(f'{duration_per_utterance} Duration per utterance')
        logging.info(f'{accuracy} Accuracy')
        logging.info(f'{words_per_minute} Words Per Minute')
        logging.info('New Utterance has been initialised')

    def button_clicked_1(self):
        self.count += 1
        logging.info(self.text1)
        logging.info(f'{self.number_of_words} Number of words')
        
    choice_button_working = False;
    def choiceButtonClicked1(self, button):
        if self.choice_button_working:
            return;
        self.choice_button_working = True;    
        start_button_clicked = time.time()
        # add the new piece of text to class variable storing all (previous) text
        self.text1 += ' ' + button.text()
        # show text in lower line
        self.lineEdit_2.setText(self.text1)
        # clean upper edit field for next input
        self.lineEdit_1.setText('')
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
        
        # print('\n predictions: \n')
        # print(word_df['token'])

        global number_of_words
        word_list = self.text1.split()
        self.number_of_words = len(word_list)
        #print('NOW', self.number_of_words)
        #print('########### NUMBER OF WORDS IN UTTERANCE #########', number_of_words)

        #print('######## SELF.COUNT ########', (self.count + 1))
        logging.info(f'{self.count + 1} Button Count')

        global accuracy
        accuracy = (((self.count + 1) / self.number_of_words)*100)
        accuracy = round(accuracy, 2)

        iNoButton=int(0)
        for i in self.pushButtons1:
            if iNoButton < word_df['token'].count():
                i.setText(str(word_df['token'].iloc[iNoButton]))
                i.setEnabled(True)
            else:
                i.setText("")
                i.setEnabled(False)
            iNoButton +=1

        stop_button_clicked = time.time()
        global button_clicked_duration
        button_clicked_duration = stop_button_clicked - start_button_clicked
        logging.info(f'{button_clicked_duration} Button clicked duration')
        # Ensure buttons have repainted before we continue
        self.tab.repaint();
        self.choice_button_working = False; 

    def lineEditEdited(self, lineedit):
        if (len(lineedit.text()) == 1 and lineedit.text() !="Q"):
            if self.start_time == None:
                self.start_time = time.time()
                #print("Start Time: %d\n"%(self.start_time)); 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Enhanced_Dasher_GUI = QtWidgets.QWidget()
    ui = Ui_Enhanced_Dasher_GUI()
    ui.setupUi(Enhanced_Dasher_GUI)
    Enhanced_Dasher_GUI.show()
    sys.exit(app.exec_())