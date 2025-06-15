# 1. Kütüphane İçe Aktarımları
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import csv
import threading
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# 2. Log Mesajı Fonksiyonu
def log_message(msg):
    log_text.config(state='normal')
    log_text.insert(tk.END, msg + '\n')
    log_text.see(tk.END)
    log_text.config(state='disabled')

# 3. UPOS'tan Tag Üretme Fonksiyonu
def upos_to_tag(upos):
    # UPOS değerini küçük harfe çevirip kısaltma üretir
    mapping = {
        "VERB": "vrb",
        "NOUN": "nn",
        "ADJ": "adj",
        "ADV": "advrb",
        "PRON": "prn",
        "PROPN": "prpn",
        "ADP": "adp",
        "AUX": "aux",
        "CCONJ": "cconj",
        "DET": "det",
        "INTJ": "intj",
        "NUM": "num",
        "PART": "part",
        "SCONJ": "sconj",
        "PUNCT": "punct",
        "SYM": "sym",
        "X": "x"
    }
    return mapping.get(upos.upper(), upos.lower())

# 4. CoNLL-U Dosyasını Okuma ve Dönüştürme Fonksiyonu

def parse_conllu(file_path):
    data = []
    sentence_id = 1
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('#'):
                continue
            if not line.strip():
                sentence_id += 1
                continue
            fields = line.strip().split('\t')
            if len(fields) == 10:
                token_id = fields[0]
                token = fields[1]      # FORM
                meaning = fields[3]    # UPOS
                tag = upos_to_tag(meaning)
                data.append([
                    sentence_id,   # Sentence
                    token_id,      # ID
                    token,         # Token
                    meaning,       # Meaning
                    tag            # Tag
                ])
    return data

# 5. CSV Kaydetme Fonksiyonu
def save_csv(data, out_path):
    with open(out_path, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow([
            "Sentence", "ID", "Token", "Meaning", "Tag"
        ])
        writer.writerows(data)

# 6. Dosya Seçme Fonksiyonu (GUI)

def select_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("CoNLL-U dosyası", "*.conllu")],
        title="İşlemek istediğiniz veri dosyasını seçin"
    )
    if file_path:
        entry_file.delete(0, tk.END)
        entry_file.insert(0, file_path)
        label_status.config(text="Dosya yüklendi. Dönüştürmek için 'Dönüştür' butonuna basın.", fg="#2e7d32")
        log_message(f"Dosya seçildi: {file_path}")

# 7. Dönüştürme İşlemini Başlatan Fonksiyon (GUI)

def convert():
    file_path = entry_file.get()
    if not file_path or not file_path.endswith('.conllu'):
        messagebox.showerror("Hata", "Lütfen bir .conllu uzantılı veri dosyası seçin!")
        log_message("Hatalı dosya seçimi! .conllu uzantılı dosya bekleniyor.")
        return
    label_status.config(text="Dosya işleniyor...", fg="#1565c0")
    log_message("Dönüştürme işlemi başlatıldı.")
    root.update_idletasks()
    threading.Thread(target=process_conversion, args=(file_path,)).start()

# 8. Dönüştürme ve Kaydetme İşlemini Gerçekleştiren Fonksiyon (GUI)

def process_conversion(file_path):
    try:
        log_message("Veri okunuyor...")
        data = parse_conllu(file_path)
        if not data:
            label_status.config(text="Uygun veri bulunamadı.", fg="#c62828")
            log_message("Uygun veri bulunamadı.")
            return
        out_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV dosyası", "*.csv")],
            title="Çıktı dosyasını kaydedin"
        )
        if out_path:
            label_status.config(text="Çıktı kaydediliyor...", fg="#1565c0")
            log_message(f"CSV dosyası kaydediliyor: {out_path}")
            save_csv(data, out_path)
            label_status.config(text=f"Başarılı! CSV dosyası kaydedildi.", fg="#2e7d32")
            log_message("Dönüştürme işlemi tamamlandı.")
        else:
            log_message("Kullanıcı çıktı dosyası seçimini iptal etti.")
    except Exception as e:
        label_status.config(text="Bir hata oluştu.", fg="#c62828")
        log_message(f"Hata: {str(e)}")
        messagebox.showerror("Hata", f"Bir hata oluştu:\n{str(e)}")

# 9. Tkinter Arayüzü Oluşturma

root = tk.Tk()
root.title("POS Tagging (Sözcük Türü Etiketleme) Uygulaması ")
root.geometry("480x420")
root.resizable(False, False)

frame = tk.Frame(root, padx=20, pady=10)
frame.pack(expand=False)

label_title = tk.Label(frame, text="Kelime Etiketleyiciye Hoş Geldiniz", font=("Segoe UI", 13, "bold"))
label_title.pack(pady=(0, 5))

label_info = tk.Label(frame, text="İşlemek istediğiniz veri dosyasını (.conllu) yükleyin.", font=("Segoe UI", 10))
label_info.pack()

entry_file = tk.Entry(frame, width=32, font=("Segoe UI", 10))
entry_file.pack(pady=8, side=tk.LEFT, fill=tk.X, expand=True)

btn_browse = tk.Button(frame, text="Gözat", command=select_file, font=("Segoe UI", 10))
btn_browse.pack(pady=8, side=tk.LEFT, padx=(5,0))

frame2 = tk.Frame(root)
frame2.pack(pady=(10,0))

btn_convert = tk.Button(frame2, text="Dönüştür", command=convert, width=20, font=("Segoe UI", 11, "bold"), bg="#4CAF50", fg="white")
btn_convert.pack()

label_hint = tk.Label(root, text="* Girdi dosyası: .conllu\n* Çıktı dosyası: .csv (içerik değişmez)", font=("Segoe UI", 9), fg="#555")
label_hint.pack(pady=(10,0))

label_status = tk.Label(root, text="", font=("Segoe UI", 10, "italic"), fg="#1565c0")
label_status.pack(pady=(8,0))

log_frame = tk.LabelFrame(root, text="İşlem Logu", font=("Segoe UI", 10, "bold"))
log_frame.pack(fill="both", expand=True, padx=20, pady=(10, 15))

log_text = scrolledtext.ScrolledText(log_frame, height=8, state='disabled', font=("Consolas", 9))
log_text.pack(fill="both", expand=True, padx=5, pady=5)


# 10. Tkinter Ana Döngüsü
root.mainloop()