import streamlit as st
import pandas as pd
from style import linia_pionowa, linia_pozioma, naglowek
from logowanie import akcje
from baza_danych import init_db, insert_transaction, get_transactions
from import_danych import import_danych
from eksport_danych import export_excel
from wykresy import wybor_miesiaca, wykres_kat_kolowy, wybor_roku_kategorii, wykres_rok_kat_slupkowy

st.set_page_config(page_title="Budżet domowy", layout="wide")

# Panel nagłówka: tytuł strony, logowanie
# Po zalogowaniu podsumowanie wraz z możliwością odświeżenia strony i wylogowania
st.markdown("<h1 style='text-align:center;color:green'>MENADŻER BUDŻETU DOMOWEGO</h1></br>", unsafe_allow_html=True)
linia_pozioma()

# Inicjalizacja bazy
init_db()
    
coll1, coll2 = st.columns([2, 4])
with coll1:
    st.image(r"C:\Users\Robert\Desktop\PYTHON\first_repo\budzet_domowy\aplikacja_grafika_01.jpg", width=550)
with coll2:
    akcje()
    # Podsumowanie transakcji
    df = get_transactions()
    df["data"] = pd.to_datetime(df["data"])
    df["rok_miesiac"] = df["data"].dt.to_period("M").astype(str)
    miesiace = sorted(df["rok_miesiac"].unique(), reverse=True)
    opcje = ["Wszystko"] + miesiace
    naglowek("Podsumowanie finansowe", podkreslenie=True)
    st.markdown("<p>*<i> Po dodaniu transakcji należy odświeżyć dane</i></p>",unsafe_allow_html=True)
    wybor = st.selectbox("Wybierz miesiąc:", opcje, key="sb_podsumowanie")
    
    if wybor != "Wszystko":
        df = df[df["rok_miesiac"] == wybor]
    przychody = df[df['kwota'] > 0]['kwota'].sum()
    wydatki = df[df['kwota'] < 0]['kwota'].sum()
    saldo = df['kwota'].sum()
    
    if not df.empty:
        col1, col2, col3 = st.columns(3)
        col1.metric("Suma przychodów", f"{przychody:.2f} zł")
        col2.metric("Suma wydatków", f"{wydatki:.2f} zł")
        if saldo >= 0:
            col3.metric("Saldo / Oszczędności", f"{saldo:.2f} zł", delta="👍", delta_color="normal")
        else:
            col3.metric("Saldo / Zadłużenie", f"{saldo:.2f} zł", delta="👎", delta_color="inverse")
    
    if df.empty:
        st.info("Brak danych do wyświetlenia.")
    
# Panel główny
linia_pozioma()

ca1, ca2, ca3 = st.columns ([0.93, 0.05, 2])
with ca1:
    
    # Formularz dodawania transakcji
    naglowek("Dodawanie transakcji", podkreslenie=True)

    typ = st.radio("Typ transakcji", ["Przychód", "Wydatek"], horizontal=True, key="typ_transakcji")
    data = st.date_input("Data")
    opis = st.text_input("Opis")
    kwota = st.number_input("Kwota", min_value=0.0, step=1.0, format="%.2f")

    # Dynamiczne pole kategorii
    if typ == "Wydatek":
        kategoria = st.selectbox("Kategoria", ["Rachunki", "Kredyt", "Jedzenie", "Ubrania", "Auto", "Rozrywka", "Inne"])
    else:
        kategoria = "Przychód"
        st.markdown(f"**Kategoria:** {kategoria}")

    # Przycisk dodania transakcji
    if st.button("➕ Dodaj transakcję"):
        if typ == "Wydatek":
            kwota = -kwota
        insert_transaction(data, opis, kwota, kategoria)
        st.success("✅ Transakcja dodana!")
    
    # Import danych z pliku .csv lub .xlsx
    naglowek("Import danych", podkreslenie=True)
    st.markdown("<p>Możliwość importu transakcji z pliku <b>.csv</b> lub <b>.xlsx</b>. </br> *<i> Wymagane kolumny: data, opis, kwota, kategoria. </br>**<i> Dostępne kategorie: Rachunki, Kredyt, Jedzenie, Ubrania, Auto, Rozrywka, Inne, Przychód</i></p>",unsafe_allow_html=True)
    import_danych(insert_transaction)
        
with ca2:
    # Linia rozdzielająca dodawanie transakcji z wyświetlanymi danymi
    linia_pionowa()

with ca3:
    # Historia transakcji
    df = get_transactions()
    ca3_1, ca3_2 = st.columns ([4, 1])
    with ca3_1:
        naglowek("Historia transakcji", podkreslenie=True)
    with ca3_2:
        st.markdown("</br>", unsafe_allow_html=True) # wyrównanie przycisku z nagłówkiem
        st.download_button("📥 Pobierz Excel", data=export_excel(df),
                        file_name="budzet_domowy.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                        )
    st.dataframe(df.sort_values("id", ascending=False), use_container_width=True)
    
    # Analiza wydatków
    naglowek("Analiza wydatków", podkreslenie=True)
    df["data"] = pd.to_datetime(df["data"])
    df["rok_miesiac"] = df["data"].dt.to_period("M").astype(str)
    col4, col5 = st.columns(2)
    with col4:
        st.subheader("Wydatki wg kategorii")
        wybor = wybor_miesiaca(df, key="sb_wydatki")
        st.markdown("</br></br>", unsafe_allow_html=True) # wyrównanie wykresów
        # Filtrowanie danych
        if wybor != "Wszystko":
            df_wykres = df[df["rok_miesiac"].astype(str) == wybor]
        else:
            df_wykres = df
        wykres_kat_kolowy(df_wykres)
    with col5:
        st.subheader("Wydatki wg kategorii w czasie")     
        rok, wybrana_kategoria = wybor_roku_kategorii(df)
        wykres_rok_kat_slupkowy(df, rok, wybrana_kategoria)