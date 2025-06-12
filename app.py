import os
import mistune
from flask import Flask, render_template, request
from dotenv import load_dotenv
from gemini_client import get_gemini_response

load_dotenv()
app = Flask(__name__)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
@app.route('/', methods=['GET', 'POST'])
def index():
    generated_cases_html = ""
    feature_description_input = ""

    if not GEMINI_API_KEY:
        error_html = "<h1>Błąd Konfiguracji</h1><p class='error'>Brak klucza GEMINI_API_KEY. Upewnij się, że utworzyłeś plik .env i dodałeś do niego swój klucz.</p>"
        return render_template('index.html', generated_cases_html=error_html, feature_description_input="")

    if request.method == 'POST':
        feature_description_input = request.form.get('feature_description')
        if feature_description_input:
            markdown_response = get_gemini_response(GEMINI_API_KEY, feature_description_input)

            generated_cases_html = mistune.html(markdown_response)

    return render_template('index.html', generated_cases_html=generated_cases_html,
                           feature_description_input=feature_description_input)

if __name__ == '__main__':
    app.run(debug=True, port=5001)