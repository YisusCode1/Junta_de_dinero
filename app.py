from flask import Flask, render_template, request, redirect, url_for  # type: ignore

from junta_dinero import JuntaDeDinero

import random

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    total = None
    if request.method == 'POST':
        num_personas = int(request.form['num_personas'])
        aporte = int(request.form['aporte'])
        if num_personas < 3:
            error = "El número de personas debe ser al menos 3."
            return render_template('index.html', error=error)
        else:
            total = num_personas * aporte
            # Redirigir a la página de resultados con los parámetros en la URL
            return redirect(url_for('mostrar_ganadores', num_personas=num_personas, aporte=aporte))
    return render_template('index.html', total=total)


@app.route('/resultados', methods=['GET'])
def mostrar_ganadores():
    # Obtener los parámetros de la URL
    num_personas_str = request.args.get('num_personas')
    aporte_str = request.args.get('aporte')

    # Verificar si los valores no son None y convertirlos a enteros
    if num_personas_str is not None and aporte_str is not None:
        num_personas = int(num_personas_str)
        aporte = int(aporte_str)
    else:
        # Si los valores faltan, mostrar un mensaje de error o redirigir a otra página
        return "Error: los parámetros num_personas y aporte son necesarios en la URL"

    # Crear la instancia de JuntaDeDinero con los parámetros de la URL
    junta = JuntaDeDinero(num_personas=num_personas, aporte=aporte)

    # Ejecutar la junta y obtener los ganadores
    ganadores = junta.ejecutar_junta()
    random.shuffle(ganadores)  # Mezclar la lista de ganadores

    # Calcular el monto total que se va a sortear
    monto_sorteo = num_personas * aporte

    # Renderizar el template 'resultados.html' con los ganadores y el monto del sorteo
    return render_template('resultados.html', ganadores=ganadores, monto_sorteo=monto_sorteo)


if __name__ == '__main__':
    app.run(debug=True)
