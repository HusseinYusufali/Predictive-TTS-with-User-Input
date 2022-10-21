from curses.ascii import isdigit
from gtts import gTTS #Import Google Text to Speech
from happytransformer import HappyWordPrediction
import pandas as pd 
from playsound import playsound as play
from autocorrect import Speller
# from PyQt5 import QtCore, QtGui, QtWidgets

predict_max = 30
exitcommand = 'Q'
prediction_model = "ROBERTA"
model_name = "roberta-base"
model_path = "/Users/husseinyusufali/Desktop/PhD/Main PhD Folder/PhD - Year 2/Technical System Implementation/Predictive TransformerTTS/Transformer Models/modelroberta_AACHPC_2"

spell = Speller()
happy_wp_roberta_aac = HappyWordPrediction(prediction_model, model_name, model_path)
text = input('Please enter text string: ')
stext = spell.autocorrect_sentence(text) + '' + '[MASK]' + ''
tts = gTTS((stext.replace('[MASK]','')))
tts.save('1.wav')
play('1.wav')

while True:
  result = happy_wp_roberta_aac.predict_mask(stext, top_k = predict_max)
  index = [i for i in range(1, (predict_max + 1), 1)]
  df = pd.DataFrame(result, index=index)
  word_df = df[df["token"].str.contains("[!#$%&\'()*+,-./\:;<=>?@[\\]^_`{|}~»Â�…॥।1234567890]") == False]
  word_df = word_df.dropna().reset_index(drop=True)
  word_df = pd.DataFrame(word_df)
  df = word_df
  print(word_df['token'])
  a = input('Please input integer of the word in the prediction list above' '\n' f'{exitcommand} to exit the prediction' '\n' 'Or enter your own string: ')
  b = a.isdigit()

  if a == str(exitcommand):
    print('You have exited the prediction program.' '\n', stext.replace('[MASK]',''))
    print(stext.replace('[MASK]',''))
    tts = gTTS((stext.replace('[MASK]','')))
    tts.save('1.wav')
    play('1.wav')
    break
  
  if b == True:
    b = int(a)
    selection = (df.iat[b,0])  
    user_text = (stext.replace('[MASK]','')) + '' + selection + ' '
    print(user_text)
    tts = gTTS(selection)
    tts.save('1.wav')
    play('1.wav')
    user_text = (user_text + '[MASK]' + '')

  else:
    user_text = stext.replace('[MASK]','')+ ' ' + str(a) + ' '
    print(user_text)
    tts = gTTS(str(a))
    tts.save('1.wav')
    play('1.wav')
    user_text = stext.replace('[MASK]','') + '' + str(a) + '' + '[MASK]' + ' '

  while True:
    result_1 = happy_wp_roberta_aac.predict_mask(user_text, top_k = predict_max)
    index_1 = [i for i in range(predict_max)]
    df1 = pd.DataFrame(result_1, index=index_1)
    word_df_1 = df1[df1["token"].str.contains("[!#$%&\'()*+,-./\:;<=>?@[\\]^_`{|}~»Â�…॥।1234567890]") == False]
    word_df_1 = word_df_1.dropna().reset_index(drop=True)
    word_df_1 = pd.DataFrame(word_df_1)
    df1 = word_df_1 
    print(word_df_1['token'])

    c = input('Please input integer of the word in the prediction list above' '\n' f'{exitcommand} to exit the prediction' '\n' 'Or enter your own string: ')
    d = c.isdigit()
    
    if c == str(exitcommand):
      print('You have exited the prediction program.' '\n', user_text.replace('[MASK]',''))
      tts = gTTS((user_text.replace('[MASK]','')))
      tts.save('1.wav')
      play('1.wav')
      break

    if d == True:
      d = int(c)
      selection_1 = (df1.iat[d,0])
      user_text = ('' + user_text.replace('[MASK]','')) + '' + selection_1 + '[MASK]' + ' '
      print(user_text.replace('[MASK]',''))
      tts = gTTS(selection_1)
      tts.save('1.wav')
      play('1.wav')

    else:
      print(user_text.replace('[MASK]','') + ' ' + str(c) + ' ')
      tts = gTTS(str(c))
      tts.save('1.wav')
      play('1.wav')
      user_text = user_text.replace('[MASK]','') + '' + str(c) + '' + '[MASK]' + ' '
      
      result_1 = happy_wp_roberta_aac.predict_mask(user_text, top_k = predict_max)
      index_2 = [i for i in range(predict_max)]
      df2 = pd.DataFrame(result_1, index=index_2)
      word_df_2 = df2[df2["token"].str.contains("[!#$%&\'()*+,-./\:;<=>?@[\\]^_`{|}~»Â�…॥।1234567890]") == False]
      word_df_2 = pd.DataFrame(word_df_2, index=index)
      word_df_2 = word_df_2.dropna().reset_index(drop=True)
      word_df_2 = pd.DataFrame(word_df_2)
      df2 = word_df_2
      print(word_df_2['token'])

      e = input('Please input integer of the word in the prediction list above' '\n' f'{exitcommand} to exit the prediction' '\n' 'Or enter your own string: ')
      f = e.isdigit()

      if e == str(exitcommand):
        print('You have exited the prediction program.' '\n', user_text.replace('[MASK]',''))
        tts = gTTS((user_text.replace('[MASK]','')))
        tts.save('1.wav')
        play('1.wav')
        break

      if f == True:
        f = int(e)
        selection_2 = (df2.iat[f,0])
        user_text = ('' + user_text.replace('[MASK]','')) + '' + selection_2 + '[MASK]' + ' '
        print('' + user_text.replace('[MASK]','') + '')
        tts = gTTS(selection_2)
        tts.save('1.wav')
        play('1.wav')

      else:
        print(user_text.replace('[MASK]','') + ' ' + str(e) + ' ')
        tts = gTTS(str(e))
        tts.save('1.wav')
        play('1.wav')
        user_text = user_text.replace('[MASK]','') + ' ' + str(e) + '' + '[MASK]' + ' '