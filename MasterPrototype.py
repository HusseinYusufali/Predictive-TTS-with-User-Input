from re import I
from gtts import gTTS #Import Google Text to Speech
from happytransformer import HappyWordPrediction
from happytransformer import HappyGeneration
import pandas as pd 
import numpy as np
from playsound import playsound as play
from autocorrect import Speller

predict_max = int(20)
exitcommand = 50
prediction_model = "ROBERTA"
model_name = "roberta-base"
model_path = "/Users/husseinyusufali/Desktop/PhD/Main PhD Folder/PhD - Year 2/Technical System Implementation/Predictive TransformerTTS/Transformer Models/modelroberta_AACHPC"

spell = Speller()
happy_wp_roberta_aac = HappyWordPrediction(prediction_model, model_name, model_path)
text = input('Please enter text string: ')
stext = spell.autocorrect_sentence(text) + '[MASK]' + ' '
while True:
  result = happy_wp_roberta_aac.predict_mask(stext, top_k = predict_max)
  index = [i for i in range(predict_max)]
  df = pd.DataFrame(result, index=index)
  word_df = df[df["token"].str.contains("[!#$%&\'()*+,-./\:;<=>?@[\\]^_`{|}~»Â�…॥।1234567890]") == False]
  print(word_df['token'])
  integer_num = (int(input(f'Please input integer of the word in the prediction list above' '\n' f'{predict_max + 1} to exit the prediction' '\n' f'{exitcommand} to enter own string:')))
  a = integer_num
  if a == (predict_max + 1):
    print('You have exited the prediction program.', t.replace('[MASK]',''))
    tts = gTTS((t.replace('[MASK]','')))
    tts.save('1.wav')
    play('1.wav')
    break
  if a == (exitcommand):
    print(stext.replace('[MASK]',''))
    new_text = input('You may enter your own text string: ', )
    final_user_text = stext.replace('[MASK]','') + new_text
    print(final_user_text)
    tts = gTTS(final_user_text)
    tts.save('1.wav')
    play('1.wav')  
    exit() 
  selection = (df.iat[a,0])  
  t = (stext.replace('[MASK]','')) + selection
  print(t)
  tts = gTTS((stext.replace('[MASK]','')) + selection)
  tts.save('1.wav')
  play('1.wav')   
  stext = (t + '[MASK]' + ' ')