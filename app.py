# app.py
import os
import mistune
from flask import Flask, render_template, request
from dotenv import load_dotenv
from gemini_client import get_gemini_response

# Załaduj zmienne środowiskowe (czyli klucz API) z pliku .env
load_dotenv()

# Utwórz instancję aplikacji Flask
app = Flask(__name__)

# Pobierz klucz API ze zmiennych środowiskowych
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


@app.route('/', methods=['GET', 'POST'])
def index():
    generated_cases_html = ""
    feature_description_input = ""

    if not GEMINI_API_KEY:
        # Wyświetl błąd, jeśli klucz API nie jest skonfigurowany
        error_html = "<h1>Błąd Konfiguracji</h1><p class='error'>Brak klucza GEMINI_API_KEY. Upewnij się, że utworzyłeś plik .env i dodałeś do niego swój klucz.</p>"
        return render_template('index.html', generated_cases_html=error_html, feature_description_input="")

    if request.method == 'POST':
        # Użytkownik wysłał formularz
        feature_description_input = request.form.get('feature_description')
        if feature_description_input:
            # Wywołaj logikę Gemini
            markdown_response = get_gemini_response(GEMINI_API_KEY, feature_description_input)

            # Konwertuj odpowiedź z Markdown na HTML
            generated_cases_html = mistune.html(markdown_response)

    # Dla żądania GET lub po przetworzeniu POST, wyrenderuj stronę
    # Przekaż do szablonu wygenerowane dane oraz treść wpisaną przez użytkownika
    return render_template('index.html', generated_cases_html=generated_cases_html,
                           feature_description_input=feature_description_input)


# Ten blok pozwala uruchomić serwer bezpośrednio z PyCharma
if __name__ == '__main__':
    # debug=True sprawia, że serwer automatycznie restartuje się po zmianach w kodzie
    app.run(debug=True, port=5001)