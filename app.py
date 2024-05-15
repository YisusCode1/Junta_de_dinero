from flask import Flask, render_template, request, redirect, url_for  # type: ignore

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/crear_junta')
def crear_junta():
    return render_template('crear_junta.html')


@app.route('/unirse_junta')
def unirse_junta():
    return render_template('unirse_junta.html')


@app.route('/resultados.html')
def resultados():
    # Aquí se debería implementar la lógica para mostrar los resultados de la junta
    return render_template('resultados.html')


if __name__ == '__main__':
    app.run(debug=True)
