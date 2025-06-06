# main_app.py
# Główny plik aplikacji Streamlit

import streamlit as st
import google.generativeai as genai
import os


# --- Konfiguracja i Logika API Gemini ---
# W idealnym świecie, ta sekcja byłaby w osobnym module np. gemini_client.py

def get_gemini_response(api_key: str, feature_description: str) -> str:
    """
    Wysyła żądanie do API Gemini i zwraca odpowiedź.

    Args:
        api_key: Klucz API Gemini.
        feature_description: Opis funkcjonalności dostarczony przez użytkownika.

    Returns:
        Odpowiedź z modelu Gemini jako string.
        Zwraca pusty string w przypadku błędu.
    """
    try:
        genai.configure(api_key=api_key)

        # Definicja modelu - upewnij się, że używasz odpowiedniego modelu, np. 'gemini-1.5-flash' lub 'gemini-pro'
        # Dla Gemini 2.0, konkretna nazwa modelu może się różnić.
        # Na przykład, jeśli to 'gemini-1.5-flash-latest':
        model = genai.GenerativeModel('gemini-1.5-flash-latest')  # Zmień na właściwy model Gemini 2.0

        # Wyrafinowany prompt dla agenta
        prompt_template = f"""
Jestem światowej klasy ekspertem ds. inżynierii jakości oprogramowania i doświadczonym testerem, specjalizującym się w tworzeniu kompleksowych, precyzyjnych i użytecznych przypadków testowych. Moim celem jest zapewnienie maksymalnego pokrycia testowego dla analizowanej funkcjonalności.

Na podstawie dostarczonego poniżej opisu funkcjonalności, wymagań lub historii użytkownika, Twoim zadaniem jest wygenerowanie zestawu przypadków testowych.

Proszę, abyś skupił się na identyfikacji:
1. Głównych ścieżek pozytywnych (happy paths).
2. Scenariuszy negatywnych, w tym obsługi nieprawidłowych danych wejściowych, błędów systemowych i wyjątków.
3. Przypadków brzegowych, szczególnie tam, gdzie występują walidacje danych, limity czy zakresy.
4. Potencjalnych luk w logice lub niejednoznaczności w opisie, które mogą prowadzić do błędów.

Każdy wygenerowany przypadek testowy powinien być sformułowany jasno i zwięźle oraz zawierać następujące elementy w formacie Markdown:
* **ID Testu:** Krótki, unikalny identyfikator (np. TC_LOGIN_001).
* **Opis Testu:** Jedno zdanie opisujące cel testu.
* **Warunki Wstępne (jeśli dotyczy):** Co musi być spełnione przed wykonaniem testu.
* **Kroki do Wykonania:** Numerowana lista konkretnych akcji do wykonania przez testera.
* **Oczekiwany Rezultat:** Jasny opis tego, co powinno się wydarzyć po wykonaniu kroków.
* **Sugerowany Priorytet:** (np. Wysoki, Średni, Niski) - na podstawie krytyczności testowanej funkcjonalności.
* **Typ Testu:** (np. Funkcjonalny, Walidacja danych, UI, Bezpieczeństwo, Wydajność - wybierz najbardziej odpowiedni).

Odpowiadaj precyzyjnie, profesjonalnie i w sposób ustrukturyzowany. Preferowany format to Markdown, gdzie każdy przypadek testowy jest wyraźnie oddzielony. Unikaj ogólników i dostarczaj konkretne, praktyczne sugestie. Używaj polskiego języka w odpowiedziach.

Oto opis funkcjonalności do analizy:
"""
        full_prompt = prompt_template + f'"""\n{feature_description}\n"""'

        response = model.generate_content(full_prompt)

        # Sprawdzanie, czy odpowiedź zawiera tekst
        if response.parts:
            return "".join(part.text for part in response.parts)
        elif response.text:  # Dla starszych wersji API lub niektórych modeli
            return response.text
        else:
            st.error("Model nie zwrócił tekstu w odpowiedzi. Sprawdź konfigurację i prompt.")
            # Można też zalogować całą odpowiedź dla debugowania
            # st.json(response) # Zachowaj ostrożność, może zawierać wrażliwe dane
            return "Błąd: Model nie zwrócił treści."

    except Exception as e:
        st.error(f"Wystąpił błąd podczas komunikacji z API Gemini: {e}")
        return ""


# --- Interfejs Użytkownika Streamlit ---
# W idealnym świecie, ta sekcja mogłaby być w osobnym module np. ui_components.py

def run_ui():
    """
    Główna funkcja uruchamiająca interfejs użytkownika Streamlit.
    """
    st.set_page_config(page_title="Asystent AI dla Testera", layout="wide")

    st.title("🤖 Asystent AI do Generowania Przypadków Testowych")
    st.markdown("---")

    st.sidebar.header("O Agencie")
    st.sidebar.info(
        """
        Witaj! Jestem Twoim inteligentnym asystentem do generowania przypadków testowych,
        wspieranym przez Gemini. Opisz funkcjonalność, którą chcesz przetestować,
        a ja przygotuję dla Ciebie zestaw kompleksowych testów.
        Specjalizuję się w tworzeniu testów funkcjonalnych, negatywnych i brzegowych.
        """
    )

    st.sidebar.header("Konfiguracja")
    # Użyj st.secrets dla klucza API w środowisku produkcyjnym Streamlit Cloud
    # Dla lokalnego uruchomienia, można użyć text_input lub zmiennych środowiskowych
    # api_key_from_env = os.getenv("GEMINI_API_KEY")
    # api_key = st.sidebar.text_input("🔑 Wprowadź swój klucz API Gemini:", type="password", value=api_key_from_env or "")

    # Użyjemy st.secrets jeśli jest dostępne, w przeciwnym razie poprosimy o wprowadzenie
    try:
        api_key = st.secrets["AIzaSyC8KpZS680WqJABpxWPAuR5m2WR5JhCRGQ"]
        st.sidebar.success("Klucz API Gemini załadowany z sekretów!")
    except (FileNotFoundError, KeyError):
        st.sidebar.warning("Nie znaleziono klucza API w sekretach Streamlit.")
        api_key = st.sidebar.text_input("🔑 Wprowadź swój klucz API Gemini:", type="password")

    st.subheader("📝 Opisz funkcjonalność do przetestowania:")
    feature_description_input = st.text_area(
        "Wprowadź szczegółowy opis funkcjonalności, wymagania, historyjkę użytkownika itp.",
        height=200,
        placeholder="Np. Funkcjonalność logowania użytkownika za pomocą emaila i hasła, z opcją 'Zapomniałem hasła'."
    )

    if 'generated_cases' not in st.session_state:
        st.session_state.generated_cases = ""

    col1, col2 = st.columns([1, 5])  # Układ dla przycisków

    with col1:
        if st.button("🚀 Generuj Przypadki Testowe", use_container_width=True, type="primary"):
            if not api_key:
                st.error("🚨 Proszę wprowadzić klucz API Gemini w panelu bocznym.")
            elif not feature_description_input:
                st.warning("📋 Proszę wprowadzić opis funkcjonalności.")
            else:
                with st.spinner("🧠 Myślę... Generowanie przypadków testowych..."):
                    response_text = get_gemini_response(api_key, feature_description_input)
                    st.session_state.generated_cases = response_text

    with col2:
        if st.session_state.generated_cases:
            if st.button("📋 Kopiuj do schowka", use_container_width=True):
                st.code(f"navigator.clipboard.writeText(`{st.session_state.generated_cases.replace('`', '\\')}`)",
                        language='javascript')  # Hack do kopiowania w Streamlit
                st.success("Skopiowano do schowka (jeśli przeglądarka na to pozwala).")

    st.markdown("---")

    if st.session_state.generated_cases:
        st.subheader("💡 Wygenerowane Przypadki Testowe:")
        st.markdown(st.session_state.generated_cases)
    else:
        st.info("Tutaj pojawią się wygenerowane przypadki testowe po kliknięciu przycisku 'Generuj'.")

    st.markdown("---")
    st.caption("Aplikacja stworzona z użyciem Streamlit i Google Gemini.")


# --- Uruchomienie Aplikacji ---
if __name__ == "__main__":
    run_ui()

