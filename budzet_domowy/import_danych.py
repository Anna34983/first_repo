import streamlit as st
import pandas as pd

wymagane_kol = {"data", "opis", "kwota", "kategoria"}
wymagane_kat = ["Rachunki", "Kredyt", "Jedzenie", "Ubrania", "Auto", "Rozrywka", "Inne", "Przychód"]

def import_danych(insert_transaction_fn):
    
    uploaded_file = st.file_uploader(
        label="Dodaj transakcje za pomocą pliku .csv lub .xlsx",
        type=["csv", "xlsx"],
        label_visibility="collapsed"
        )

    if uploaded_file is not None:
        if uploaded_file.name.endswith(".csv"):
            df_import = pd.read_csv(uploaded_file)
        else:
            df_import = pd.read_excel(uploaded_file)

        if "data" in df_import.columns:
            df_import["data"] = pd.to_datetime(df_import["data"]).dt.strftime("%Y-%m-%d")
        
        st.write("Podgląd importu:", df_import.head())
        
        if wymagane_kol.issubset(df_import.columns):
            unikalne_kat = set(df_import["kategoria"].unique())
            nieprawidlowe_kat = unikalne_kat - set(wymagane_kat)
            if nieprawidlowe_kat:
                st.error(f"Plik zawiera niedozwolone kategorie: {', '.join(nieprawidlowe_kat)}\n\n"
                         f"Dopuszczalne: {', '.join(wymagane_kat)}")
            else:
                if st.button("Importuj dane"):
                    licznik = 0
                    for _, row in df_import.iterrows():
                        data_str = str(row["data"])
                        if isinstance(row["data"], pd.Timestamp):
                            data_str = row["data"].strftime("%Y-%m-%d")
                        insert_transaction_fn(
                            data_str,
                            row["opis"],
                            row["kwota"],
                            row["kategoria"]
                        )
                        licznik += 1
                    st.success(f"Zaimportowano {licznik} wierszy!")
        else:
            st.error(f"Plik musi zawierać kolumny: {', '.join(wymagane_kol)}")