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
👉 [[https://www.youtube.com/watch?v=xL0ESUYa0ug](https://www.youtube.com/watch?v=xL0ESUYa0ug)]

---

## 🛠 Proje Açıklaması

Bu projede, **Run-Length Encoding (RLE)** yöntemi ile bir metin sıkıştırılır ve tekrar eski haline getirilir.

**Örnek:**

```
Girdi  : AAAAABBBCCDAA
Çıktı  : 5:A3:B2:C1:D2:A
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
📦BLM101_24360859921_DenizBASAT
├── main.py                   # The main file...
├── README.md                 
├── RLE-Sonum.pdf             # Guid-Book about Project and "RLE" 
└── src
    ├── modules               # Modules of project with option to add other modules not only RLE
    |   └──rle                # RLE modules for working 
    |      ├── encode.py
    │      ├── decode.py
    │      └── percent.py
    |
    └── config                # Config file for customize any info
        └── config.py
```
