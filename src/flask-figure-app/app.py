from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

figure_colors = {"square": "#808080", "circle": "#808080", "triangle": "#808080"} # code smell

@app.route('/')
def index():
    return render_template('index.html', figure_colors=figure_colors)

@app.route('/change-color', methods=['POST'])
def change_color():
    data = request.get_json()
    figure_type = data.get('figure_type')
    new_color = data.get('new_color')

    if figure_type:
        # begin - code smell
        if figure_type == "square":
            figure_colors["square"] = new_color
        elif figure_type == "circle":
            figure_colors["circle"] = new_color
        elif figure_type == "triangle":
            figure_colors["triangle"] = new_color
        # end - code smell
        return jsonify({"status": "success", "figure_colors": figure_colors})
    return jsonify({"status": "error", "message": "figure type error"}), 400

@app.route('/change-color-all', methods=['POST'])
def change_color_all():
    data = request.get_json()
    new_color = data.get('new_color')

    if new_color:
        figure_colors["square"] = new_color # code smell
        figure_colors["circle"] = new_color # code smell
        figure_colors["triangle"] = new_color # code smell
        return jsonify({"status": "success", "figure_colors": figure_colors})
    return jsonify({"status": "error", "message": "new color error"}), 400

if __name__ == '__main__':
    app.run(debug=True)