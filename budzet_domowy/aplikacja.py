import streamlit as st
import pandas as pd
from logowanie import akcje
from baza_danych import init_db, insert_transaction, get_transactions
from import_danych import import_danych
from eksport_danych import export_excel
from wykresy import wykres_kat_kolowy, wykres_rok_kat_slupkowy

st.set_page_config(page_title="Budżet domowy", layout="wide")

# Panel główny: tytuł strony, logowanie
# Po zalogowaniu podsumowanie wraz z możliwością odświeżenia strony i wylogowania
st.markdown("<h1 style='text-align:center;color:green'>MENADŻER BUDŻETU DOMOWEGO</h1></br>", unsafe_allow_html=True)
st.markdown("""
    <div style="
        height: 100%;
        width: 100%;
        display: flex;
        justify-content: center;
        ">
        <div style="border-bottom: 2px solid gray; width: 100%;"></div>
    </div>
""", unsafe_allow_html=True)
    
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
    st.markdown("<h2 style='text-decoration: underline;'>Podsumowanie finansowe</h2>", unsafe_allow_html=True)
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

init_db()

# Panel treści
st.markdown("""
<div style="
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    ">
    <div style="border-bottom: 2px solid gray; width: 100%;"></div>
</div>
""", unsafe_allow_html=True)

ca1, ca2, ca3 = st.columns ([0.93, 0.05, 2])
with ca1:
    # Formularz dodawania transakcji
    st.markdown("<h2 style='text-decoration: underline;'>Dodawanie transakcji</h2>", unsafe_allow_html=True)

    typ = st.radio("Typ transakcji", ["Przychód", "Wydatek"], horizontal=True, key="typ_transakcji")
    data = st.date_input("Data")
    opis = st.text_input("Opis")
    kwota = st.number_input("Kwota", min_value=0.0, format="%.2f")

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
    
    # Import danych
    import_danych(insert_transaction)
        
with ca2:
    st.markdown("""
    <div style="
        height: 100%;
        width: 100%;
        display: flex;
        justify-content: center;
        ">
        <div style="border-right: 2px solid gray; height: 135vh;"></div>
    </div>
    """, unsafe_allow_html=True)

with ca3:
    # Historia transakcji
    df = get_transactions()
    ca3_1, ca3_2 = st.columns ([4, 1])
    with ca3_1:
        st.markdown("<h2 style='text-decoration: underline;'>Historia transakcji", unsafe_allow_html=True)
    with ca3_2:
        st.markdown("</br>", unsafe_allow_html=True)
        st.download_button("📥 Pobierz Excel", data=export_excel(df),
                        file_name="budzet_domowy.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                        )
    st.dataframe(df.sort_values("id", ascending=False), use_container_width=True)
    
    # Analiza wydatków
    st.markdown("<h2 style='text-decoration: underline;'>Analiza wydatków", unsafe_allow_html=True)
    df["data"] = pd.to_datetime(df["data"])
    col4, col5 = st.columns(2)
    with col4:
        st.subheader("Wydatki wg kategorii")
        df["rok_miesiac"] = df["data"].dt.to_period("M").astype(str)  # kolumna miesiąc-rok, np. 2024-07
        # Lista miesięcy do wyboru + opcja "Wszystko"
        miesiace = sorted(df["rok_miesiac"].unique(), reverse=True)
        opcje = ["Wszystko"] + miesiace
        # Selectbox
        wybor = st.selectbox("Wybierz miesiąc:", opcje, key="sb_wydatki")
        st.markdown("</br></br>", unsafe_allow_html=True)
        # Filtrowanie danych
        if wybor != "Wszystko":
            df_plot = df[df["rok_miesiac"].astype(str) == wybor]
        else:
            df_plot = df
        wykres_kat_kolowy(df_plot)
    with col5:
        st.subheader("Wydatki wg kategorii w czasie")
        # Dodaj selectboxy do wyboru roku i kategorii
        lata = sorted(df["data"].apply(lambda x: pd.to_datetime(x).year).unique())
        rok = st.selectbox("Wybierz rok:", lata, index=len(lata)-1)
        kategorie = sorted([kat for kat in df["kategoria"].unique() if kat != "Przychód"])
        kategorie_opcje = ["Wszystko"] + kategorie
        wybrana_kategoria = st.selectbox("Wybierz kategorię wydatków:", kategorie_opcje)
        # Wywołaj wykres
        wykres_rok_kat_slupkowy(df, rok, wybrana_kategoria)