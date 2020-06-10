import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('speak to the microphone:')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="en-EN")
        print('you said {}'.format(text))
    except:
        print('something wrong')