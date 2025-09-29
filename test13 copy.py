from pydub import AudioSegment

song = r"./explode1.ogg"
song = AudioSegment.from_ogg(song)
neu = song + input("Bitte angeben, um wie viel das Audio verstärkt werden soll: ")
neu.export("./explode1.ogg", format='ogg')