document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('participantes').addEventListener('change', function() {
        generarDirecciones();
    });

    document.getElementById('monto').addEventListener('change', function() {
        generarDirecciones();
    });

    var crearJuntaLink = document.getElementById('crear-junta-link');

    function generarDirecciones() {
        var participantes = parseInt(document.getElementById('participantes').value);
        var monto = parseInt(document.getElementById('monto').value);
        var direccionesBilleteraDiv = document.getElementById('direcciones-billetera');
        direccionesBilleteraDiv.innerHTML = '';

        if (participantes < 3 || participantes > 20 || isNaN(monto)) {
            document.getElementById('crear-junta-btn').style.display = 'none';
            return;
        }

        for (var i = 1; i <= participantes; i++) {
            var label = document.createElement('label');
            label.textContent = 'Dirección de Billetera ' + i + ':';
            var input = document.createElement('input');
            input.type = 'text';
            input.name = 'direccion_billetera_' + i;
            input.required = true;
            input.addEventListener('input', verificarCamposDirecciones);
            var br = document.createElement('br');
            direccionesBilleteraDiv.appendChild(label);
            direccionesBilleteraDiv.appendChild(input);
            direccionesBilleteraDiv.appendChild(br);
        }

        var montoSortearDiv = document.getElementById('monto-a-sortear');
        var montoSortear = participantes * monto;
        montoSortearDiv.textContent = 'Monto a Sortear: ' + montoSortear;

        crearJuntaLink.href = '/resultados.html?participantes=' + participantes;

        document.getElementById('crear-junta-btn').style.display = 'block';
    }

    function verificarCamposDirecciones() {
        var inputs = document.querySelectorAll('#direcciones-billetera input');
        var todosLlenos = true;
        for (var i = 0; i < inputs.length; i++) {
            if (!inputs[i].value) {
                todosLlenos = false;
                break;
            }
        }
        if (todosLlenos) {
            document.getElementById('crear-junta-btn').style.display = 'block';
        } else {
            document.getElementById('crear-junta-btn').style.display = 'none';
        }
    }
});









