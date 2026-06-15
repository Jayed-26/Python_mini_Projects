# This is a auto jokes generator and reader. it will read it out loud for you.

import pyjokes
joke = pyjokes.get_joke()
print(joke)

import pyttsx3
engine = pyttsx3.init()
engine.say(joke + " Ha ha ha!, hope you liked it!")
engine.runAndWait()