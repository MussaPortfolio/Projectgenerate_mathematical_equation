import speech_recognition as sr
from say_text import say_text


def listen():
    '''Функция случает текст пользователя и выдает его в формате string'''
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Говорите...")
        say_text('Говорите')
        audio = r.listen(source)
    query = r.recognize_google(audio, language="ru-RU")
    return query

#Cerf