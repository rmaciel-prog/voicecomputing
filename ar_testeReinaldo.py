import speech_recognition as sr
import pyaudio

###função que ouve e reconhece a fala

def ouvir_microfone():
    #habilita o microfone
    frase = ''
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        #efetua a redução de ruído
        microfone.adjust_for_ambient_noise(source)
        
        print('Diga alguma coisa:')
        ##guarda a informação em uma variável
        audio = microfone.listen(source)
        
    try:
        ##detecta os padrões do speech_recognition
        
        frase = microfone.recognize_google(audio, language='pt-BR')
        
        print("Você disse: "+frase)
        
    except sr.UnknownValueError:
        print('Texto não reconhecido')
        
    return frase

ouvir_microfone()