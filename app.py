from flask import Flask, render_template, request, redirect, url_for  # type: ignore
import random

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/crear_junta', methods=['GET', 'POST'])
def crear_junta():
    if request.method == 'POST':
        participantes = int(request.form['participantes'])
        monto = int(request.form['monto'])
        direcciones = [request.form[f'direccion-{i}']
                       for i in range(1, participantes + 1)]

        # Selección aleatoria de ganadores (uno por mes)
        ganadores = random.sample(direcciones, len(direcciones))

        return redirect(url_for('resultados', ganadores=','.join(ganadores)))

    return render_template('crear_junta.html')


@app.route('/resultados')
def resultados():
    ganadores = request.args.get('ganadores').split(',')
    return render_template('resultados.html', ganadores=ganadores)


@app.route('/unirse_junta')
def unirse_junta():
    return render_template('unirse_junta.html')


if __name__ == '__main__':
    app.run(debug=True)
