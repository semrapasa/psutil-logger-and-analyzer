<p align="center">
  <a href="https://semrapasa-system-monitor.hf.space/docs" target="_blank">🚀 semrapasa-system-monitor.hf.space/docs</a>
</p>

<p align="center">
  
  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=gradient&amp;customColorList=12,20,24&amp;height=220&amp;section=header&amp;text=SystemMonitor&amp;fontSize=56&amp;fontColor=fff&ampanimation=twinkling&ampfontAlignY=40&ampdesc=Real-time%20CPU%20%26%20RAM%20%7C%20FastAPI%20%7C%20Docker%20%7C%20HuggingFace%20Spaces&ampdescAlignY=62&ampdescSize=17" />

</p>

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/psutil-powered-success?style=for-the-badge" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/deploy-live-brightgreen?style=flat-square" />
  <img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" />
</p>

---

## 📡 Proje Nedir?

Sisteminizin CPU ve RAM kullanımını **gerçek zamanlı** izleyen bir monitör.  
İki modda çalışır: terminalden direkt kullanım ve REST API üzerinden uzaktan kontrol.
Psutil,HuggingFace,FastAPI,Docker

### 📊 Canlı API Çıktısı (Docs / Swagger UI Örneği)

API, güncel sistem yük durumunu barlar halinde JSON formatında döner:

<p align="center">
  
  <img src="https://github.com/user-attachments/assets/2290db4e-fc47-43de-bae3-e6c931d419ef" alt="Sistem Monitörü API Çıktısı" width="100%">

</p>


## 🏗️ Mimari

```
System-Monitor/
├── system_monitor.py     # Standalone terminal uygulaması
├── system_monitor_deploy.py                  # FastAPI ile deploy uygulaması
├── Dockerfile              # Container tanımı
└── requirements.txt
```

---

## ⚡ Özellikler

| Özellik | Terminal | API |
|---|---|---|
| CPU izleme | ✅ | ✅ |
| RAM izleme | ✅ | ✅ |
| Canlı güncelleme | ✅ (1s) | ✅ (0.6s) |
| Uzaktan kontrol | ❌ | ✅ |
| durdurma fonk | ✅ | ✅ |
| Swagger UI | — | ✅ `/docs` |

---

## 🖥️ Terminal Modu

```bash
pip install psutil pynput
python terminal_monitor.py
```

> Çıkmak için **q** tuşuna basın.

---


### Docker ile çalıştırma

```bash
docker build -t sistem-monitor .
docker run -p 7860:7860 sistem-monitor
```

### Endpoint'ler

| Method | Endpoint | Açıklama |
|---|---|---|
| `GET` | `/` | Durum & canlı veri |
| `GET` | `/sistem_monitör_başlat` | İzlemeyi başlat |
| `GET` | `/sistem_monitor_durdur` | İzlemeyi durdur |
| `GET` | `/docs` | Swagger UI |



## 🚀 HuggingFace Spaces Deploy

Bu proje **HuggingFace Spaces** üzerinde Docker runtime ile deploy edilmiştir.

> 🔗 **[Live Demo →]([https://semrapasa-system-monitor.hf.space/docs)](https://semrapasa-system-monitor.hf.space/docs)**

<details>
<summary><b>Deploy adımları</b></summary>

<br>

1. HuggingFace'te yeni bir Space oluşturun → SDK: **Docker**
2. Aşağıdaki `Dockerfile`'ı projenize ekleyin:

```dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7860
CMD ["uvicorn", "api:sistem_app", "--host", "0.0.0.0", "--port", "7860"]
```

3. `requirements.txt`:

```
fastapi
uvicorn
psutil
```

4. Dosyaları Space'e push edin — otomatik deploy başlar.

</details>

---

## 🛠️ Kullanılan Teknolojiler

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,fastapi,docker,linux&theme=dark" />
</p>

---

## 🗺️ Yol Haritası

- [x] Terminal monitörü
- [x] FastAPI entegrasyonu
- [x] Docker containerization
- [x] HuggingFace Spaces deploy
- [ ] CSV kaydetme...


---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=100&section=footer" />
</p>
```
