# gemini_client.py
import google.generativeai as genai

def get_gemini_response(api_key: str, feature_description: str) -> str:
    """
    Wysyła żądanie do API Gemini i zwraca odpowiedź w formacie Markdown.
    W przypadku błędu, zwraca sformatowany komunikat o błędzie.
    """
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash-latest')

        prompt_template = f"""
Jestem światowej klasy ekspertem ds. inżynierii jakości oprogramowania i doświadczonym testerem, specjalizującym się w tworzeniu kompleksowych, precyzyjnych i użytecznych przypadków testowych. Moim celem jest zapewnienie maksymalnego pokrycia testowego dla analizowanej funkcjonalności.

Na podstawie dostarczonego poniżej opisu funkcjonalności, wymagań lub historii użytkownika, Twoim zadaniem jest wygenerowanie zestawu przypadków testowych.

Proszę, abyś skupił się na identyfikacji:
1. Głównych ścieżek pozytywnych (happy paths).
2. Scenariuszy negatywnych, w tym obsługi nieprawidłowych danych wejściowych, błędów systemowych i wyjątków.
3. Przypadków brzegowych, szczególnie tam, gdzie występują walidacje danych, limity czy zakresy.
4. Potencjalnych luk w logice lub niejednoznaczności w opisie, które mogą prowadzić do błędów.

Każdy wygenerowany przypadek testowy powinien być sformułowany jasno i zwięźle oraz zawierać następujące elementy w formacie Markdown:
* **ID Testu:** Krótki, unikalny identyfikator.
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

        if response.parts:
            return "".join(part.text for part in response.parts)
        elif hasattr(response, 'text') and response.text:
            return response.text
        else:
            return "Błąd: Model Gemini nie zwrócił treści w odpowiedzi."

    except Exception as e:
        print(f"Błąd API: {e}")
        return f"Wystąpił błąd podczas komunikacji z API Gemini: {e}"