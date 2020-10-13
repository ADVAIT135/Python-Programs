import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print("SPEAK.......")
    audio=r.listen(source)
print(r.reconize_google(audio))











