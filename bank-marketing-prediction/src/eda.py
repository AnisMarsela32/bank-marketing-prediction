import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def run():
    st.title("Bank Marketing - Exploratory Data Analysis")
    st.markdown("Visualisasi distribusi dan hubungan fitur dengan target langganan (`y`)")

    # Load data
    df = pd.read_csv("./src/bank-full.csv", sep=";", quotechar='"')
    st.dataframe(df.head())

    st.markdown("## 1. Distribusi Target (y)")
    fig1 = plt.figure()
    sns.countplot(x='y', data=df)
    plt.title('Distribusi Target (y)')
    plt.xlabel('Langganan')
    plt.ylabel('Jumlah')
    st.pyplot(fig1)

    st.markdown("## 2. Distribusi Umur")
    fig2 = plt.figure(figsize=(10, 5))
    sns.histplot(df['age'], bins=30, kde=True)
    plt.title('Distribusi Umur')
    plt.xlabel('Umur')
    plt.ylabel('Jumlah')
    st.pyplot(fig2)

    st.markdown("## 3. Status Perumahan vs Langganan")
    fig3 = plt.figure()
    sns.countplot(x='housing', hue='y', data=df)
    plt.title('Status Perumahan vs Langganan')
    plt.xlabel('Punya Pinjaman Rumah')
    plt.ylabel('Jumlah')
    st.pyplot(fig3)

    st.markdown("## 4. Pekerjaan vs Langganan")
    fig4 = plt.figure(figsize=(12, 6))
    sns.countplot(x='job', hue='y', data=df, order=df['job'].value_counts().index)
    plt.title('Pekerjaan vs Langganan')
    plt.xlabel('Pekerjaan')
    plt.ylabel('Jumlah')
    plt.xticks(rotation=45)
    st.pyplot(fig4)

    st.markdown("## 5. Bulan vs Langganan")
    fig5 = plt.figure(figsize=(10, 5))
    sns.countplot(
        x='month', hue='y', data=df,
        order=['jan', 'feb', 'mar', 'apr', 'may', 'jun', 
               'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    )
    plt.title('Bulan vs Langganan')
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah')
    st.pyplot(fig5)

    st.markdown("## 6. Pinjaman Pribadi vs Langganan")
    fig6 = plt.figure()
    sns.countplot(x='loan', hue='y', data=df)
    plt.title('Pinjaman Pribadi vs Langganan')
    plt.xlabel('Punya Pinjaman Pribadi')
    plt.ylabel('Jumlah')
    st.pyplot(fig6)

    st.markdown("## 7. Distribusi Durasi (y = yes)")
    fig7 = plt.figure()
    sns.histplot(df[df['y'] == 'yes']['duration'], bins=50, kde=True)
    plt.title('Distribusi Durasi untuk Klien yang Berlangganan (y = yes)')
    plt.xlabel('Durasi (detik)')
    plt.ylabel('Jumlah')
    st.pyplot(fig7)

if __name__ == '__main__':
    run()
