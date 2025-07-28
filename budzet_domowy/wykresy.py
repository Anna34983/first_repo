import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

def wykres_kat_kolowy(df):
    data = df[df["kwota"] < 0].groupby("kategoria")["kwota"].sum().abs()
    if data.empty:
        st.info("Brak danych o wydatkach.")
        return
    fig, ax = plt.subplots()
    ax.pie(data, labels=data.index, autopct="%1.1f%%")
    ax.axis("equal")
    st.pyplot(fig)
    
def wykres_rok_kat_slupkowy(df, rok, wybrana_kategoria):
    df = df.copy()
    df["data"] = pd.to_datetime(df["data"])
    df_wyd = df[(df["kwota"] < 0) & (df["kategoria"] != "Przychód")].copy()
    df_wyd = df_wyd[df_wyd["data"].dt.year == rok]
    
    if wybrana_kategoria != "Wszystko":
        df_wyd = df_wyd[df_wyd["kategoria"] == wybrana_kategoria]

    if df_wyd.empty:
        st.info("Brak wydatków do wyświetlenia.")
        return

    # Dodanie miesiąca
    df_wyd["miesiac"] = df_wyd["data"].dt.month

    if wybrana_kategoria == "Wszystko":
        grouped = df_wyd.groupby(["miesiac", "kategoria"])["kwota"].sum().unstack(fill_value=0).abs()
        grouped = grouped.reindex(index=range(1, 13), fill_value=0)
        title = "Wydatki w kategoriach wg miesięcy"
        fig, ax = plt.subplots()
        grouped.plot(kind="bar", ax=ax)
        ax.legend(title="Kategoria")
    else:
        grouped = df_wyd.groupby("miesiac")["kwota"].sum().abs()
        grouped = grouped.reindex(index=range(1, 13), fill_value=0)
        title = f"Wydatki: {wybrana_kategoria} wg miesięcy"
        fig, ax = plt.subplots()
        grouped.plot(kind="bar", ax=ax, color="tab:blue")

    ax.set_title(title)
    ax.set_ylabel("Suma wydatków [zł]")
    ax.set_xlabel("Miesiąc")
    ax.set_xticks(range(0, 12))
    ax.set_xticklabels([str(m) for m in range(1, 13)])
    plt.tight_layout()
    st.pyplot(fig)