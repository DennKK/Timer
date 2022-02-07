import time
import pyglet
import win10toast
from threading import Thread

hour = int(input("How many hours?"))
minute = int(input("How many minutes?"))
second = int(input("How many seconds?"))
timer = (hour * 3600 + minute * 60 + second)


def play_sound():
    sound = pyglet.media.load('music/TimerSound1.mp3')
    sound.play()
    pyglet.app.run()


def popup_notification():
    toast = win10toast.ToastNotifier()
    toast.show_toast(title="WAKE UP!", msg="Time is up", duration=10)


def main():
    time.sleep(timer)
    Thread(target=play_sound).start()
    Thread(target=popup_notification).start()


if __name__ == "__main__":
    main()