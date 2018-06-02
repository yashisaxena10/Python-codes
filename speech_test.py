import speech_recognition as sr

r=sr.Recognizer()

mic=sr.Microphone()

with mic as source:
    print("Say something: ")
    r.adjust_for_ambient_noise(source)
    audio=r.listen(source)


try:
    output=r.recognize_google(audio)
except sr.UnknownValueError:
    print("Sorry I could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Speech Recognition service; {0}".format(e))

print("I thinks you said ",output)



