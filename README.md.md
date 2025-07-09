# Analisis dan Prediksi Data Nasabah Bank

## Repository Outline
```
1. README.md - Penjelasan umum project
2. notebook.ipynb - Proses utama: eksplorasi, preprocessing, dan modeling
3. P1M2_anis_marsela.ipynb - Notebook utama sesuai format project
4. P1M2_anis_marsela_inf.ipynb - Notebook untuk proses prediksi/inference
5. P1M2_anis_marsela_conceptual.ipynb - Penjelasan konsep secara teori
6. bank-marketing-prediction/
   ├── eda.py - Script eksplorasi data
   ├── prediction.py - Script prediksi model
   ├── streamlit_app.py - Dashboard visualisasi
7. url.txt - Link penting
8. gb_model_pipeline.pkl - Model Gradient Boosting dalam format pickle
9. bank-full.csv - Dataset utama

```

---

## Problem Background

Sebuah bank di Portugal menjalankan kampanye pemasaran lewat telepon untuk menawarkan produk deposito berjangka. Namun, tidak semua nasabah tertarik, sehingga banyak waktu dan tenaga terbuang sia-sia.

Dengan bantuan data historis dari kampanye sebelumnya, kita ingin memprediksi apakah seorang nasabah akan setuju membuka deposito atau tidak. Tujuannya adalah agar kampanye lebih tepat sasaran dan efisien.

## Project Output

Output dari proyek ini adalah sebuah model machine learning berbasis Gradient Boosting yang mampu memprediksi apakah seorang nasabah akan menerima penawaran deposito. Model ini juga dikemas dalam pipeline siap pakai dan telah diuji dengan metrik evaluasi yang relevan. Selain itu, terdapat visualisasi hasil dalam bentuk dashboard Streamlit.

## Data

Dataset berasal dari UCI dan Kaggle, berisi data kampanye pemasaran telepon oleh bank di Portugal.

* Jumlah data: 45.211 baris (versi penuh), 4.521 baris (versi kecil)
* Fitur: 16 kolom input + 1 kolom target (`y`)
* Target: Apakah nasabah berlangganan deposito berjangka? (ya/tidak)
* Tipe data: kombinasi numerik dan kategorikal (usia, pekerjaan, status pernikahan, dsb.)
* Tidak ada nilai kosong (missing values)

---

## Method

Proyek ini menggunakan pendekatan supervised learning untuk klasifikasi biner (ya/tidak berlangganan deposito). Beberapa model diuji, seperti KNN, SVM, Decision Tree, dan Random Forest. Namun, Gradient Boosting dipilih sebagai model terbaik. Data imbalance diatasi dengan SMOTE dan performa model dievaluasi melalui cross-validation serta hyperparameter tuning menggunakan Grid Search. Fokus utama metrik adalah recall untuk kelas yes, agar sebanyak mungkin nasabah yang tertarik bisa terdeteksi.

---

## Stacks

* Bahasa Pemrograman: Python

* Libraries: pandas, numpy, scikit-learn, imblearn, matplotlib, seaborn, streamlit, joblib

* Tools: Jupyter Notebook, Visual Studio Code, Streamlit, Git

---

## Reference

* Dataset: [UCI Machine Learning Repository - Bank Marketing](https://archive.ics.uci.edu/ml/datasets/bank+marketing)
* [Scikit-learn documentation](https://scikit-learn.org/stable/)
* [Imbalanced-learn documentation](https://imbalanced-learn.org/)
