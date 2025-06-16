# 🇹🇷 Türkçe POS Tagging GUI Uygulaması

 

Bu proje, `.conllu` formatındaki Türkçe metinleri analiz ederek her kelimenin dilbilgisel türünü (Part-of-Speech / POS) etiketleyen bir masaüstü uygulamadır. Etiketlenen veriler `.csv` formatında dışa aktarılır. Uygulama Python diliyle ve `Tkinter` GUI kütüphanesiyle geliştirilmiştir.

 

---

 

## 🎯 Proje Amacı

 

POS tagging (sözcük türü etiketleme), metin içerisindeki her kelimenin fiil, isim, zarf gibi türünü belirleme işlemidir. Bu uygulama sayesinde:

 

- Türkçe `.conllu` dosyaları kolayca analiz edilir

- Arayüz üzerinden dönüştürme işlemi gerçekleştirilir

- Sonuçlar Excel uyumlu `.csv` olarak dışa aktarılır

 

---

 

## 🖼️ Arayüz Özellikleri

 

- `.conllu` formatında veri girişi

- Kullanıcı dostu Tkinter arayüzü

- Dönüştürme işlemini başlatma düğmesi

- İşlem log ekranı

- `.csv` olarak veri kaydı

 

---

 

## 📥 Girdi Formatı (CoNLL-U)

 

1​Ali​_​PROPN​

2​renkli​_​ADJ​

3​bir​_​NUM​

4​resim​_​NOUN​

5​çizdi​_​VERB​

6​.​_​PUNCT

---

 

## 📤 Çıktı Formatı (CSV)

 

| Sentence | ID | Token | Meaning | Tag   |

|----------|----|--------|---------|--------|

| 1        | 1  | Ali     | PROPN   | prpn   |

| 1        | 2  | renkli | ADJ        | adj    |

| 1        | 3  | bir      | NUM      | num    |

| 1        | 4  | resim | NOUN    | noun    |

| 1        | 5  | çizdi  | VERB      | vrb    |

| 1        | 6  | .         | PUNCT    | pnct    |

 

---

 

## ⚙️ Kullanılan Teknolojiler

 

- Python 3.10+

- Tkinter (GUI)

- CSV (veri işleme)

- Threading (arka plan işlemi)

- Pandas (CSV gösterimi için isteğe bağlı)

 

---

 

## 🧪 Kurulum ve Çalıştırma

 

```bash

# 1. Reponun klonlanması

git clone https://github.com/kullanici_adiniz/pos-tagger-tr.git

cd pos-tagger-tr

 

# 2. Gerekli kütüphaneler (opsiyonel)

pip install pandas

 

# 3. Uygulamanın başlatılması

python pos_tagger_gui_app.py

👨‍💻 Geliştirici Ekip

İsim​Görevler

Süleyman Asım Gelişgen​Arayüz geliştirme, GitHub yayını

Hasan Umut Kocatepe​Veri seti hazırlığı (.conllu dosyası)

Ahmet Sefa Ünal​Video sunumu, kaynak araştırması

Talha Korkmaz​Temel kodlama (işleme, etiketleme, CSV kayıt)

 

📚 Kaynaklar

Speech and Language Processing – Jurafsky & Martin

 

NLP with Python – NLTK Kitabı

 

Universal POS Tags

 

Python Tkinter Docs

![image](https://github.com/user-attachments/assets/3f5cf06d-da4c-4a4c-acd6-6763fccff228)
![image](https://github.com/user-attachments/assets/a1582169-d5fb-4960-9a2e-0febca03614e)

