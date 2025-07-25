import matplotlib.pyplot as plt
import streamlit as st

def plot_category_pie(df):
    data = df[df["kwota"] < 0].groupby("kategoria")["kwota"].sum().abs()
    if data.empty:
        st.info("Brak danych o wydatkach.")
        return
    fig, ax = plt.subplots()
    ax.pie(data, labels=data.index, autopct="%1.1f%%")
    ax.axis("equal")
    st.pyplot(fig)

def plot_time_trend(df):
    grouped = df.groupby("data")["kwota"].sum().reset_index()
    fig, ax = plt.subplots()
    ax.plot(grouped["data"], grouped["kwota"], marker="o")
    ax.set_xlabel("Data")
    ax.set_ylabel("Kwota")
    ax.set_title("Przepływ finansowy")
    st.pyplot(fig)
