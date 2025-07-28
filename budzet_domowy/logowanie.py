import streamlit as st

# Dane logowania (dla uproszczenia w kodzie)
USERNAME = "admin"
PASSWORD = "wsb2025"

def akcje():
    # Formularz logowania

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.markdown("<h2 style='text-decoration: underline;'>Logowanie</h2>", unsafe_allow_html=True)
        username = st.text_input("Nazwa użytkownika")
        password = st.text_input("Hasło", type="password")
        login_btn = st.button("🔐Zaloguj")

        if login_btn:
            if username == USERNAME and password == PASSWORD:
                st.session_state.logged_in = True
                st.success("✅ Zalogowano pomyślnie")
                st.rerun()
            else:
                st.error("❌ Nieprawidłowa nazwa użytkownika lub hasło")

        st.stop()  # zatrzymuje dalsze ładowanie aplikacji

    # Przyciski wylogowania i odświeżania danych
    if st.session_state.get("logged_in", False):
        _, col1, col2 = st.columns([3, 1, 1])
        with col1:
            if st.button("🔄 Odśwież dane", key="refresh_button"):
                st.rerun()
        with col2:
            if st.button("📴 Wyloguj", key="logout_button"):
                st.session_state.logged_in = False
                st.rerun()