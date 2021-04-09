import requests
from gtts import gTTS
import os

active_cases=requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=39MIBO73EC2CREV3")
death_cases=requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=R8Q8FVW3WT70UOED")
vaccination_cases=requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=3G4JT7G9LR2SALZV")

print("Active Count     :",active_cases.text.strip())
print("Death Count      :",death_cases.text.strip())
print("Vaccination Count:",vaccination_cases.text.strip())

mytext = "covid पोर्टल में आपका स्वागत है|"
language = 'hi'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("active_cases.mp3")
os.system("mpg321 active_cases.mp3")

mytext = "सक्रिय covid संख्या:"+active_cases.text
mytext2="मृत्यु संख्या:"+death_cases.text
mytext3="टीकाकरण संख्या:"+vaccination_cases.text
mytext4="दवाई भी ,और कड़ाई भी!, भारत सरकार द्वारा जनहित में जारी"
language = 'hi'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj1 = gTTS(text=mytext2, lang=language, slow=False)
myobj2 = gTTS(text=mytext3, lang=language, slow=False)
myobj3 = gTTS(text=mytext4, lang=language, slow=False)
myobj.save("active_cases.mp3")
myobj1.save("death_cases.mp3")
myobj2.save("vaccination_cases.mp3")
myobj3.save("greet.mp3")
os.system("mpg321 active_cases.mp3")
os.system("mpg321 death_cases.mp3")
os.system("mpg321 vaccination_cases.mp3")
os.system("mpg321 greet.mp3")