# 👾 RLE (Run-Length Encoding) Sıkıştırma Projesi

## 👨‍🎓 Öğrenci Bilgileri

* **Ad:** Deniz
* **Soyad:** BAŞAT
* **Öğrencı No:** 24360859921

---

## 📌 Proje Konusu

**2. Grup – Veri Depolama ve Sıkıştırma Algoritmaları**

> 📍 RLE (Run-Length Encoding) Sıkıştırıcı

---

## ▶ YouTube Linki

🎥 **Sunum Videosu:**
👉 [https://www.youtube.com/watch?v=abcdef12345](https://www.youtube.com/watch?v=abcdef12345)

---

## 🛠 Proje Açıklaması

Bu projede, **Run-Length Encoding (RLE)** yöntemi ile bir metin sıkıştırılır ve tekrar eski haline getirilir.

**Örnek:**

```
Girdi  : AAAAABBBCCDAA
Çıktı  : 5A3B2C1D2A
```

Program ayrıca **sıkıştırma oranını (%)** hesaplar.

---

## ▶ Nasıl Çalıştırılır?

Terminal (veya CMD) açılır ve aşağıdaki komut çalıştırılır:

```
python main.py
```

Ardından kullanıcıdan bir metin girilmesi istenir.

---

## 🌐 Ağ (Network) Gereksinimi

* İnternet gerekir mi? ❌ Hayır
* Ek ayar var mı? ❌ Hayır

---

## 🧠 Çalışma Mantığı (Özet)

1. Kullanıcıdan metin alınır ✍️
2. `encode.py` ile sıkıştırılır ⚙️
3. `decode.py` ile tekrar açılır 🔁
4. `percent.py` ile sıkıştırma oranı hesaplanır 📊
5. Sonuçlar ekrana yazdırılır ✅

---

## 📂 Proje Yapısı

```
📦 BLM101_202312345_AhmetYilmaz
├── main.py                   # MAin 
├── README.md
├── Sunum.pdf
└── src
    ├── modules 
    |   └──rle
    |      ├── encode.py
    │      ├── decode.py
    │      └── percent.py
    |
    └── config
        └── config.py
```
