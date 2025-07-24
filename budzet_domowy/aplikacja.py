import streamlit as st
import pandas as pd
from db import init_db, insert_transaction, get_transactions
from utils import export_excel
from charts import plot_category_pie, plot_time_trend

st.set_page_config(page_title="Budżet domowy", layout="wide")
st.title("💰 Menedżer budżetu domowego")

# Inicjalizacja bazy
init_db()

# Formularz dodawania
st.header("➕ Dodaj transakcję")
with st.form("dodaj_form"):
    data = st.date_input("Data")
    opis = st.text_input("Opis")
    kwota = st.number_input("Kwota", format="%.2f")
    kategoria = st.selectbox("Kategoria", ["Jedzenie", "Transport", "Zakupy", "Rozrywka", "Rachunki", "Inne"])
    submitted = st.form_submit_button("Dodaj")

    if submitted:
        insert_transaction(data, opis, kwota, kategoria)
        st.success("✅ Transakcja dodana!")

# Dane z bazy
df = get_transactions()

# Tabela danych
st.header("📋 Historia transakcji")
st.dataframe(df.sort_values("data", ascending=False), use_container_width=True)

# Wykresy
if not df.empty:
    st.header("📊 Wizualizacje")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Wydatki wg kategorii")
        plot_category_pie(df)
    with col2:
        st.subheader("Trend czasowy")
        plot_time_trend(df)

# Eksport
st.header("📤 Eksport do Excela")
st.download_button("📥 Pobierz Excel", data=export_excel(df),
                   file_name="budzet_domowy.xlsx",
                   mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
