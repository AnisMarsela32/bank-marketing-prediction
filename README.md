# Prediksi Nasabah yang Berlangganan Deposito Bank

Proyek ini bertujuan membantu sebuah bank di Portugal dalam menyusun strategi pemasaran telepon yang lebih efisien dengan memprediksi apakah seorang nasabah akan setuju membuka **deposito berjangka** atau tidak. Model dibangun menggunakan data historis kampanye pemasaran sebelumnya.

---

## Latar Belakang Masalah

Sebuah bank menjalankan kampanye pemasaran melalui telepon untuk menawarkan produk deposito. Namun, tidak semua nasabah tertarik, sehingga banyak waktu dan tenaga terbuang sia-sia.

Dengan memanfaatkan data historis, kita dapat membangun model yang memprediksi siapa saja nasabah yang **berpotensi membuka deposito**, sehingga kampanye jadi **lebih tepat sasaran dan hemat biaya**.

---

## Tujuan Proyek

- Membersihkan dan menyiapkan data historis dari kampanye pemasaran bank.
- Memahami pola karakteristik nasabah yang tertarik pada produk deposito.
- Menemukan fitur penting yang mempengaruhi keputusan nasabah.
- Membangun model klasifikasi untuk memprediksi apakah nasabah akan mengatakan `yes` atau `no`.
- Fokus utama adalah **recall**, untuk menjangkau sebanyak mungkin calon nasabah potensial.
- Menyediakan visualisasi hasil dalam bentuk **dashboard Streamlit**.

---

## Deskripsi Dataset

- **Sumber:** UCI & Kaggle
- **Jumlah data:** 45.211 baris (versi penuh), 4.521 baris (versi kecil)
- **Fitur:** 16 fitur input + 1 target (`y`)
- **Target:** Apakah nasabah membuka deposito berjangka? (`yes` / `no`)
- **Jenis data:** Kombinasi numerik & kategorikal (umur, pekerjaan, status pernikahan, dll.)
- Tidak terdapat nilai kosong

---

## Proses Pengolahan Data

Langkah-langkah utama dalam preprocessing:

- **Imputasi** untuk menangani nilai kosong (jika ada)
- **Encoding** untuk fitur kategorikal
- **Normalisasi** untuk menyamakan skala fitur numerik
- **Penanganan Outlier** menggunakan Winsorizer
- **SMOTE** untuk mengatasi ketidakseimbangan kelas (kelas `yes` jauh lebih sedikit)
- Semua tahap dikemas dalam **pipeline otomatis** agar proses konsisten dan terulang

---

## Metodologi

Proyek menggunakan pendekatan supervised learning untuk klasifikasi biner (`yes` / `no`). Model yang dicoba:

- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Decision Tree
- Random Forest
- **Gradient Boosting** (model terbaik)

Ketidakseimbangan data ditangani menggunakan **SMOTE**. Evaluasi dilakukan menggunakan **cross-validation** dan **GridSearchCV** untuk tuning hyperparameter.

Metode evaluasi utama adalah **recall untuk kelas `yes`**, agar tidak ada calon nasabah yang terlewatkan.

---

## Model Terbaik: Gradient Boosting

Model Gradient Boosting dipilih karena:

- **Recall tinggi** (0.81) untuk kelas `yes`
- F1-score seimbang
- Konsisten pada cross-validation
- Mampu mendeteksi lebih banyak nasabah potensial

---

## Deployment

Model telah disiapkan untuk **deployment** menggunakan **Hugging Face Spaces** atau **Streamlit**.

🔗 [Link ke Hugging Face / Streamlit](https://huggingface.co/spaces/anismarsela32/bank-marketing-prediction)

---

## Teknologi yang Digunakan

- **Bahasa:** Python 
- **Library:** pandas, numpy, scikit-learn, imbalanced-learn, seaborn, matplotlib, streamlit, joblib
- **Tools:** Jupyter Notebook, VSCode, Git, Streamlit

---

## Kontak

- **Nama:** Anis Marsela  
- **Email:** anismarsela36854@gmail.com
- **LinkedIn:** [linkedin.com/in/anis-marsela](https://www.linkedin.com/in/anis-marsela-348727301/)

---

## 📚 Referensi

- [UCI Machine Learning Repository - Bank Marketing](https://archive.ics.uci.edu/ml/datasets/bank+marketing)
- [Dokumentasi Scikit-learn](https://scikit-learn.org/stable/)
- [Dokumentasi Imbalanced-learn](https://imbalanced-learn.org/)
