Asystent AI do Generowania Przypadków Testowych
Prosta aplikacja webowa oparta na frameworku Flask, która wykorzystuje API Google Gemini do automatycznego generowania przypadków testowych na podstawie opisu funkcjonalności oprogramowania.

Autor: Aleksander Wajs - 36412

# Kluczowe Funkcje

### Interfejs Webowy: 
Prosty i czysty interfejs do wprowadzania opisu funkcjonalności.

### Integracja z AI: 
Wykorzystuje model gemini-1.5-flash do analizy tekstu i generowania treści.

### Generowanie Testów: 
Tworzy kompleksowe przypadki testowe, uwzględniając ścieżki pozytywne, negatywne i przypadki brzegowe.
### Formatowanie Wyników: 
Odpowiedź od AI w formacie Markdown jest konwertowana na czytelny HTML.

# Zastosowane Technologie
### Backend: 
Python 3, Flask
### Frontend: 
HTML5, CSS
### API: 
Google Gemini API

### Kluczowe biblioteki Python:
google-generativeai: Oficjalny klient Google do obsługi API.
python-dotenv: Do zarządzania zmiennymi środowiskowymi (klucz API).
mistune: Do konwersji odpowiedzi (Markdown) na HTML.

# Struktura Projektu

```
├── templates
│  └── index.html         
├── .env                   
├── app.py                   
├── gemini_client.py         
└── requirements.txt         
```
# Instalacja i Uruchomienie
Aby uruchomić projekt lokalnie, postępuj zgodnie z poniższymi krokami.

1. Wymagania wstępne
Zainstalowany Python 3.8+
Klucz API do Google Gemini (do uzyskania w Google AI Studio)
2. Utworzenie Środowiska Wirtualnego
Zalecane jest utworzenie środowiska wirtualnego, aby odizolować zależności projektu.



# Utwórz środowisko wirtualne
python -m venv venv

## Aktywuj środowisko
### Na Windows:
venv\Scripts\activate
### Na macOS/Linux:
source venv/bin/activate

3. Instalacja Zależności
Zainstaluj wszystkie potrzebne biblioteki za pomocą pliku requirements.txt.

```pip install -r requirements.txt```

4. Konfiguracja Klucza API
Stwórz w głównym katalogu projektu plik o nazwie .env.

Dodaj do niego swój klucz API w następującym formacie:

GEMINI_API_KEY="API_KEY"

5. Uruchomienie Serwera
Po wykonaniu powyższych kroków, uruchom serwer deweloperski Flask.

```python app.py```

Możesz również uruchomić aplikację bezpośrednio w edytorze kodu (np. PyCharm), klikając prawym przyciskiem na plik app.py i wybierając opcję "Run 'app'".

Po uruchomieniu serwera, aplikacja będzie dostępna w przeglądarce pod adresem: http://127.0.0.1:5001

### Jak to działa?

Użytkownik otwiera stronę główną w przeglądarce.
Wpisuje w formularzu opis funkcjonalności i klika przycisk "Generuj".
Przeglądarka wysyła zapytanie POST do serwera Flask.
Serwer (app.py) odbiera dane i wywołuje funkcję get_gemini_response() z modułu gemini_client.py, przekazując jej opis oraz klucz API.
Funkcja ta wysyła zapytanie do API Google Gemini ze specjalnie przygotowanym promptem.
API Gemini zwraca odpowiedź w formacie Markdown.
Serwer Flask konwertuje otrzymany Markdown na HTML za pomocą biblioteki mistune.
Na koniec, serwer renderuje szablon index.html, wstawiając w odpowiednie miejsce wygenerowaną treść i odsyła gotową stronę do przeglądarki użytkownika.
