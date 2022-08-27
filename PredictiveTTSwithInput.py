from gtts import gTTS #Import Google Text to Speech
from happytransformer import HappyWordPrediction
from happytransformer import HappyGeneration
import pandas as pd 
import numpy as np
from playsound import playsound as play
from autocorrect import Speller

predict_max = 10
exitcommand = 50

spell = Speller()
happy_wp = HappyWordPrediction("ROBERTA","roberta-large",load_path="model/")
text = input('Please enter text string: ')
stext = spell.autocorrect_sentence(text) + '[MASK]' + ' '
while True:
  result = happy_wp.predict_mask(stext, top_k = predict_max)
  index = [i for i in range(10)]
  df = pd.DataFrame(result, index=index)
  word_df = df[df["token"].str.contains("[!#$%&\'()*+,-./\:;<=>?@[\\]^_`{|}~Â1234567890]") == False]
  print(word_df['token'])
  integer_num =int(input(f'Please input integer of the word in the prediction list above' '\n' f'{predict_max + 1} to exit the prediction' '\n' f'{exitcommand} to enter own string:'))
  a = integer_num
  if a == (predict_max + 1):
    print('You have exited the prediction program.', t.replace('[MASK]',''))
    break
  if a == (exitcommand):
    print(stext.replace('[MASK]',''));
    new_text = input('You may enter your own text string: ', )
    final_user_text = stext.replace('[MASK]','') + new_text
    print(final_user_text)
    tts = gTTS(final_user_text)
    tts.save('1.wav')
    play('1.wav')  
    exit() 
  t = (stext.replace('[MASK]','')) + (df.iat[a,0]);
  stext = (t + '[MASK]' + ' ')
  print('Text string: ' + t)

final_text = (stext.replace('[MASK]',''))
tts = gTTS(final_text)
tts.save('1.wav')
play('1.wav')  