import streamlit as st
import pandas as pd
import joblib

# Load model pipeline
model_pipeline = joblib.load("./src/gb_model_pipeline.pkl")

st.title("Prediksi Pelanggan Berlangganan (Bank Marketing)")

st.markdown("Silakan masukkan informasi nasabah untuk memprediksi apakah mereka akan berlangganan produk bank.")

def run():
    with st.form(key="form-predict"):
        age = st.number_input("Umur", min_value=18, max_value=100, value=35, step=1)
        job = st.selectbox("Pekerjaan", [
            'admin.', 'technician', 'services', 'management', 'retired', 'blue-collar',
            'unemployed', 'entrepreneur', 'housemaid', 'student', 'self-employed', 'unknown'
        ])
        marital = st.selectbox("Status Pernikahan", ['single', 'married', 'divorced'])
        education = st.selectbox("Pendidikan", [
            'high.school', 'basic.9y', 'university.degree', 'professional.course',
            'basic.6y', 'basic.4y', 'illiterate', 'unknown'
        ])
        default = st.radio("Kredit Macet?", ['no', 'yes'])
        balance = st.number_input("Saldo", min_value=-2000, max_value=100000, value=3000, step=100)
        housing = st.radio("Pinjaman Rumah?", ['no', 'yes'])
        loan = st.radio("Pinjaman Pribadi?", ['no', 'yes'])
        contact = st.selectbox("Jenis Kontak", ['cellular', 'telephone'])
        day = st.slider("Hari terakhir kontak (1-31)", min_value=1, max_value=31, value=15)
        month = st.selectbox("Bulan terakhir kontak", [
            'jan', 'feb', 'mar', 'apr', 'may', 'jun',
            'jul', 'aug', 'sep', 'oct', 'nov', 'dec'
        ])
        duration = st.number_input("⏱Durasi kontak (detik)", min_value=0, max_value=5000, value=500, step=10)
        campaign = st.number_input("Jumlah kontak pada kampanye ini", min_value=1, max_value=100, value=1, step=1)
        pdays = st.number_input("Hari sejak kontak terakhir (-1 jika belum pernah)", min_value=-1, max_value=1000, value=3, step=1)
        previous = st.number_input("Jumlah kontak sebelumnya", min_value=0, max_value=100, value=2, step=1)
        poutcome = st.selectbox("Hasil kampanye sebelumnya", ['failure', 'nonexistent', 'success'])

        submitted = st.form_submit_button("Prediksi")

        if submitted:
            data_baru = pd.DataFrame({
                'age': [age],
                'job': [job],
                'marital': [marital],
                'education': [education],
                'default': [default],
                'balance': [balance],
                'housing': [housing],
                'loan': [loan],
                'contact': [contact],
                'day': [day],
                'month': [month],
                'duration': [duration],
                'campaign': [campaign],
                'pdays': [pdays],
                'previous': [previous],
                'poutcome': [poutcome]
            })

            prediksi = model_pipeline.predict(data_baru)[0]
            prob = model_pipeline.predict_proba(data_baru)[0][1]

            st.success(f"✅ Prediksi: **{'Berlangganan' if prediksi == 'yes' else 'Tidak Berlangganan'}**")
            st.info(f"📈 Probabilitas berlangganan: **{prob:.2%}**")

if __name__ == "__main__":
    run()
