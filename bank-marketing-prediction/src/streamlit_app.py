import streamlit as st
import eda
import prediction

st.set_page_config(
    page_title='Bank Marketing APP',
    layout='wide',
    initial_sidebar_state='expanded'
)

def main():
    st.title("Bank Marketing App")
    
    menu = ["Exploratory Data Analysis", "Prediksi Langganan"]
    choice = st.sidebar.selectbox("Pilih Halaman", menu)

    if choice == "Exploratory Data Analysis":
        eda.run()
    elif choice == "Prediksi Langganan":
        prediction.run()

if __name__ == '__main__':
    main()
