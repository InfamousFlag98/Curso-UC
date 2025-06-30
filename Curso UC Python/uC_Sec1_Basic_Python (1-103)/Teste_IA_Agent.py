import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import pause

texto_fala = pyttsx3.init()

def falar(audio):
    rate = texto_fala.getProperty('rate')
    texto_fala.setProperty('rate', 250)
    voices = texto_fala.getProperty('voices')
    texto_fala.setProperty('voice', voices[0].id)
    texto_fala.say(audio)
    texto_fala.runAndWait()

def tempo():
    agora = datetime.datetime.now().strftime("%H:%M")
    falar("Agora são: " + agora)
def data():
    ano = datetime.datetime.now().year
    mes = datetime.datetime.now().month
    dia = datetime.datetime.now().day
    falar("Hoje é: " + str(dia) + " do " + str(mes) + " de " + str(ano))
def bem_vindo():
    falar("Olá, bem vindo de volta!")
    hora = datetime.datetime.now().hour
    if hora < 12:
        falar("Bom dia!")
    elif hora < 18:
        falar("Boa tarde!")
    else:
        falar("Boa noite!")
    falar("Estou a sua disposição. O que você deseja fazer?")
def microfone():
    # Cria um reconhecedor
    r = sr.Recognizer()

    # Usa o microfone como fonte de entrada
    with sr.Microphone() as source:
        r.pause_threshold = 1
        print("Ouvindo...")
        # Ajusta o ruído ambiente
        r.adjust_for_ambient_noise(source)
        # Captura o áudio
        audio = r.listen(source)
        print("Reconhecendo...")
        try:
            # Reconhece o áudio e converte em texto
            frase = r.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {frase}")
            falar(f"Você disse: {frase}")
            return frase
        except sr.UnknownValueError:
            falar("Não consegui entender o que você disse. Repita, por favor.")
            return None
        except sr.RequestError:
            falar("Erro ao conectar ao serviço de reconhecimento de fala.")
            return None

if __name__ == "__main__":
    # Executa as funções
    falar("Iniciando o assistente de voz.")
    bem_vindo()

    while True:
        print("Ouvindo...")
        frase = microfone().lower()
        if frase is not None:
            if "sair" in frase or "parar" in frase or "encerrar" in frase or "fechar" in frase or "desligar" in frase or "isso é tudo" in frase:
                falar("Espero ter ajudado. Até logo!")
                falar("Encerrando o assistente.")
                break
            elif "hora" in frase or "horas" in frase:
                tempo()
            elif "data" in frase or "dia" in frase:
                data()
            elif "bem vindo" in frase:
                bem_vindo()
            elif "como você está" in frase:
                falar("Estou bem, obrigado por perguntar!")
                falar("O que posso fazer por você?")
            elif "abrir o spotify" in frase or "abrir spotify" in frase:
                url = 'https://open.spotify.com/'
                falar("Abrindo o navegador.")
                webbrowser.open(url)
            elif "abrir youtube" in frase or "abrir o youtube" in frase:
                url = 'https://www.youtube.com/'
                falar("Abrindo o navegador.")
                webbrowser.open(url)
            elif "abrir google" in frase or "abrir o google" in frase:
                url = 'https://www.google.com/'
                falar("Abrindo o navegador.")
                webbrowser.open(url)
            
            


            elif "pare de escutar" in frase or "parar de escutar" in frase or "não escute mais" in frase:
                falar("por quanto tempo você quer que eu pare de escutar?")
                tempo_espera = microfone()
                falar("Desligando o microfone por " + tempo_espera + "minutos.")
                tempo_espera = int(tempo_espera)
                pause.minutes(tempo_espera)
                falar("Estou de volta! O que você deseja fazer?")
        else:
                falar("Desculpe, não entendi o que você disse.")
        # Adicione mais comandos conforme necessário
