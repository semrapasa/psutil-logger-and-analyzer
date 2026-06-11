import psutil
import asyncio
from fastapi import FastAPI, BackgroundTasks

sistem_app = FastAPI(title="SISTEM MONITORU API")
izleme_aktif = False
canli_veri = {
    "cpu": "Olcum baslatin",
    "ram": "Olcum baslatin"
}


async def system_monitor(bars=50):
    global izleme_aktif, canli_veri
    while izleme_aktif:
        cpu_yuzde = psutil.cpu_percent(interval=0.1)
        ram_yuzde = psutil.virtual_memory().percent
        cpu_oran = cpu_yuzde / 100.0
        cpu_bar = "█" * int(cpu_oran * bars) + "░" * \
            (bars - int(cpu_oran * bars))
        ram_oran = ram_yuzde / 100.0
        ram_bar = "█" * int(ram_oran * bars) + "░" * \
            (bars - int(ram_oran * bars))
        canli_veri = {
            "cpu": f"|{cpu_bar}| %{cpu_yuzde:.2f}",
            "ram": f"|{ram_bar}| %{ram_yuzde:.2f}"
        }
        await asyncio.sleep(0.6)


@sistem_app.get("/")
def ana_menu():
    return {
        "mesaj": "Programi calistirmak icin sistem_monitor_baslat ardından ana_menu kısmını tekrar tekrar execute edebilirsiniz",
        "sistem_durumu": canli_veri}


@sistem_app.get("/sistem_monitor_durdur")
def system_monitor_stop():
    global izleme_aktif
    izleme_aktif = False
    return {"mesaj": "Durduruldu"}


@sistem_app.get("/sistem_monitor_baslat")
async def system_monitor_start(background_tasks: BackgroundTasks):
    global izleme_aktif
    if not izleme_aktif:
        izleme_aktif = True

    background_tasks.add_task(system_monitor)
    return {"mesaj": "Baslatildi"}
