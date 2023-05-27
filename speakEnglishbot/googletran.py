from googletrans import Translator
translator = Translator()

message = 'text'

res = translator.detect(message).lang

print(translator.translate(text='Hello world', dest='uz'))
