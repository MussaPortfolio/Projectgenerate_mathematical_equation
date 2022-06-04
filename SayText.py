import pyttsx3


def say_text(text):
    '''Функция озыучивает переданный в нее текст'''
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()