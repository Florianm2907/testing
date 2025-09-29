from pydub import AudioSegment

print("(Unterstützte Dateitypen: .mp3, .wav, .ogg, .aac, .flac, .mp2)")
while True:
    endung = ""
    song=input("Gib hier den Pfad zu deiner Audiodatei an: ")
    endungen = [".ogg", ".mp3", ".wav", ".aac", ".flac", ".mp2", ".opus"]
    for i in range(len(endungen)):
        if endungen[i] in song:
            endung = endungen[i]
        else: print("Bitte eine passende Datei angeben!")
    song = AudioSegment.from_file(song)
    neu = song + input("Bitte angeben, um wie viel das Audio verstärkt werden soll: ")
    neu.export(input("Bitte angeben, wohin die Datei exportiert werden soll: ")+endung, format=endung)