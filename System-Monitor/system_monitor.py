import psutil
import time
from pynput import keyboard


dur = False


def system_monitor(cpu_yuzde, ram_yuzde, bars=30):
    cpu_oran = cpu_yuzde / 100.0
    cpu_bar = "█" * int(cpu_oran * bars) + "-" * \
        (bars - int(cpu_oran * bars))
    ram_oran = ram_yuzde / 100.0
    ram_bar = "█" * int(ram_oran * bars) + "-" * \
        (bars - int(ram_oran * bars))
    print(f"\r CPU Kullanımı:|{cpu_bar}| %{cpu_yuzde:.2f}  ", end="")
    print(f"RAM Kullanımı:|{ram_bar}| %{ram_yuzde:.2f}  ", end="\r")


def on_press(key):  # Hazır kod olarak aldım. Monitörün istenildiğinde durması lazım
    global dur
    try:
        if key.char == 'q':
            dur = True
    except AttributeError:
        pass


def tus_kontrol():
    return dur


listener = keyboard.Listener(on_press=on_press)
listener.start()

print("Sistem izleme monitörüne hoş geldiniz. Programı durdurmak q tuşuna basabilirsiniz")
while True:
    system_monitor(psutil.cpu_percent(), psutil.virtual_memory().percent)
    if tus_kontrol():
        print("\n\nSistem İzleme Sona Erdi.")
        break
    time.sleep(1)
listener.stop()
