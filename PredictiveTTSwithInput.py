from gtts import gTTS #Import Google Text to Speech
from happytransformer import HappyWordPrediction
import pandas as pd 
from playsound import playsound as play
from autocorrect import Speller

predict_max = 20
exitcommand = 50
counter = 0
prediction_model = "ROBERTA"
model_name = "roberta-base"
model_path = "/Users/husseinyusufali/Desktop/PhD/Main PhD Folder/PhD - Year 2/Technical System Implementation/Predictive TransformerTTS/Transformer Models/modelroberta_aac"

spell = Speller()
happy_wp_roberta_aac = HappyWordPrediction(prediction_model, model_name, model_path)
text = input('Please enter text string: ')
stext = spell.autocorrect_sentence(text) + '' + '[MASK]' + ' '

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
    print(stext.replace('[MASK]','') + '' + new_text + '')
    user_text = stext.replace('[MASK]','')+ ' ' + new_text + ' '
    tts = gTTS((user_text))
    tts.save('1.wav')
    play('1.wav')
    user_text = stext.replace('[MASK]','') + '' + new_text + '' + '[MASK]' + ''

    while True:
      result_1 = happy_wp_roberta_aac.predict_mask(user_text, top_k = predict_max)
      index_1 = [i for i in range(predict_max)]
      df1 = pd.DataFrame(result_1, index=index_1)
      word_df_1 = df1[df1["token"].str.contains("[!#$%&\'()*+,-./\:;<=>?@[\\]^_`{|}~»Â�…॥।1234567890]") == False]
      print(word_df_1['token'])

      integer_num_1 = (int(input(f'Please input integer of the word in the prediction list above' '\n' f'{predict_max + 1} to exit the prediction' '\n' f'{exitcommand} to enter own string:')))
      b = integer_num_1

      if b == (predict_max + 1):
        print('You have exited the prediction program.', user_text.replace('[MASK]',''))
        tts = gTTS((user_text.replace('[MASK]','')))
        tts.save('1.wav')
        play('1.wav')
        exit()
    
      while b == exitcommand:
        new_text = ' ' + input('You may enter your own text string: ',) + ''
        print(user_text.replace('[MASK]','') + ' ' + new_text + ' ')
        tts = gTTS((user_text.replace('[MASK]','') + new_text))
        tts.save('1.wav')
        play('1.wav')
        user_text = user_text.replace('[MASK]','') + '' + new_text + '' + '[MASK]' + ''
        
        result_1 = happy_wp_roberta_aac.predict_mask(user_text, top_k = predict_max)
        index_1 = [i for i in range(predict_max)]
        df1 = pd.DataFrame(result_1, index=index_1)
        word_df_1 = df1[df1["token"].str.contains("[!#$%&\'()*+,-./\:;<=>?@[\\]^_`{|}~»Â�…॥।1234567890]") == False]
        print(word_df_1['token'])

        integer_num_1 = (int(input(f'Please input integer of the word in the prediction list above' '\n' f'{predict_max + 1} to exit the prediction' '\n' f'{exitcommand} to enter own string:')))
        b = integer_num_1

        if b == (predict_max + 1):
            print('You have exited the prediction program.' '\n', user_text.replace('[MASK]',''))
            tts = gTTS((user_text.replace('[MASK]','')))
            tts.save('1.wav')
            play('1.wav')
            exit()

      selection_1 = (df1.iat[b,0])
      user_text = ('' + user_text.replace('[MASK]','')) + ' ' + selection_1 + '[MASK]' + ''
      print('' + user_text.replace('[MASK]','') + ' ')
      tts = gTTS(user_text.replace('[MASK]',''))
      tts.save('1.wav')
      play('1.wav')

  selection = (df.iat[a,0])  
  t = (stext.replace('[MASK]','')) + selection + ''
  print(t)
  tts = gTTS((stext.replace('[MASK]','')) + selection)
  tts.save('1.wav')
  play('1.wav')
  stext = (t + '[MASK]' + ' ')