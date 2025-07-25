import streamlit as st
import pandas as pd
from baza_danych import init_db, insert_transaction, get_transactions
from eksport_danych import export_excel
from wykresy import plot_category_pie, plot_time_trend

st.set_page_config(page_title="Budżet domowy", layout="wide")
st.title("💰 Menedżer budżetu domowego")

# Inicjalizacja bazy
init_db()

# Formularz dodawania
st.header("➕ Dodaj transakcję")
with st.form("dodaj_form"):
    typ = st.radio("Typ transakcji", ["Przychód", "Wydatek"])
    data = st.date_input("Data")
    opis = st.text_input("Opis")
    kwota = st.number_input("Kwota", min_value=0.0, format="%.2f")
    kategoria = st.selectbox("Kategoria", ["Jedzenie", "Transport", "Zakupy", "Rozrywka", "Rachunki", "Inne"])
    submitted = st.form_submit_button("Dodaj")

    if submitted:
        kwota = kwota if typ == "Przychód" else -kwota
        insert_transaction(data, opis, kwota, kategoria)
        st.success("✅ Transakcja dodana!")

# Historia
df = get_transactions()
st.header("📋 Historia transakcji")
st.dataframe(df.sort_values("data", ascending=False), use_container_width=True)

# Podsumowanie
if not df.empty:
    st.subheader("📈 Podsumowanie finansowe")
    col1, col2, col3 = st.columns(3)
    col1.metric("Suma przychodów", f"{df[df['kwota'] > 0]['kwota'].sum():.2f} zł")
    col2.metric("Suma wydatków", f"{df[df['kwota'] < 0]['kwota'].sum():.2f} zł")
    col3.metric("Saldo", f"{df['kwota'].sum():.2f} zł")

    # Wykresy
    st.header("📊 Wizualizacje")
    col4, col5 = st.columns(2)
    with col4:
        st.subheader("Wydatki wg kategorii")
        plot_category_pie(df)
    with col5:
        st.subheader("Trend czasowy")
        plot_time_trend(df)

# Eksport
st.header("📤 Eksport do Excela")
st.download_button("📥 Pobierz Excel", data=export_excel(df),
                   file_name="budzet_domowy.xlsx",
                   mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
