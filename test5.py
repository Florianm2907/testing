import winsound
import time

winsound.PlaySound(r'H:\test1\ad-blocking\wartemusik.wav', winsound.SND_ASYNC)
time.sleep(10)
winsound.PlaySound(None, winsound.SND_ASYNC)
