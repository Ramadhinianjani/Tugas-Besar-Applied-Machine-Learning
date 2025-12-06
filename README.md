# Tugas-Besar-Applied-Machine-Learning
**Prediksi Jumlah Siswa Berdasarkan Data Pendidikan Indonesia**

---

**NAMA: RAMAADHINI ANJANI HAMID**

**NIM: 105841119823**

**KELAS: 5AI-B**

---

Repository ini berisi project machine learning yang bertujuan untuk memprediksi jumlah siswa berdasarkan data statistik pendidikan Indonesia. Proyek ini dibuat sebagai pemenuhan **Tugas Besar Mata Kuliah Applied Machine Learning**.

---

## 📊 Dataset  
Dataset bersumber dari:
**https://data.kemendikdasmen.go.id/dataset/p/peserta-didik/jumlah-siswa-menurut-tingkat-tiap-propinsi-indonesia-sd-2024**

Dataset yang digunakan:  
**"Jumlah Siswa Menurut Jenis Kelamin dan Status Sekolah Tiap Kabupaten/Kota"**

Sumber: *Kementerian Pendidikan dan Kebudayaan (Kemendikbud)*  
Format: `.csv`  
Isi utama:
- Kabupaten/Kota  
- Jenis Kelamin  
- Status Sekolah (Negeri/Swasta)  
- Jumlah Siswa  

---

## 🛠️ Tahapan Proyek Machine Learning  
Proyek ini mengikuti tahapan standar ML:

1. **Load data**  
2. **Cleaning & preprocessing**  
3. **Exploratory Data Analysis (EDA)**  
4. **Feature selection & engineering**  
5. **Split data (train–test)**  
6. **Training model**  
7. **Evaluasi model**  
8. **Saving model (pickle)**  
9. **Deployment menggunakan Gradio**

---
## 💻 File dalam Repository  
- `LK PERANCANGAN`
- `LAPORAN` — Penjelasan dan hasil tiap tahapan
- `datasiswa.ipynb` — Notebook utama proses ML  
- `jumlah-siswa-menurut-jenis-kelamin...csv` — Dataset  
- `model_siswa.pkl` — Model yang sudah dilatih  
- `app.py` — Script aplikasi Gradio untuk prediksi  
- `README.md` — Dokumentasi proyek  

---

## 🚀 Cara Menjalankan Aplikasi (Local)
1. Install library:
```bash
pip install pandas numpy scikit-learn gradio...
```
2. jalankan aplikasi
```bash
python app.py...
```

---

## 📈 Hasil Model  
Model menghasilkan metrik evaluasi:

- **MAE**
- **MSE**
- **RMSE**
