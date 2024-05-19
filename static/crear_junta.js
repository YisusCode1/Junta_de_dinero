document.getElementById('validar-datos-btn').addEventListener('click', function() {
    var participantes = document.getElementById('participantes').value;
    var monto = document.getElementById('monto').value;
    var direccionesContainer = document.getElementById('direcciones-billetera');
    var montoSortearContainer = document.getElementById('monto-a-sortear');
    var validacionContainer = document.getElementById('validacion-container');

    // Limpia las direcciones anteriores si existen
    direccionesContainer.innerHTML = '';
    montoSortearContainer.innerHTML = '';

    if (participantes >= 3 && participantes <= 18 && monto >= 30 && monto <= 300) {
        // Oculta el contenedor de validación
        validacionContainer.style.display = 'none';

        // Calcula el monto a sortear
        var montoTotal = participantes * monto;
        montoSortearContainer.innerHTML = '<p>Monto a sortear: ' + montoTotal + '</p>';

        // Genera los campos de direcciones con botones "Aporte"
        for (var i = 1; i <= participantes; i++) {
            var label = document.createElement('label');
            label.setAttribute('for', 'direccion-' + i);
            label.innerText = 'Dirección de Billetera ' + i + ':';

            var input = document.createElement('input');
            input.setAttribute('type', 'text');
            input.setAttribute('id', 'direccion-' + i);
            input.setAttribute('name', 'direccion-' + i);
            input.setAttribute('required', true);

            var button = document.createElement('button');
            button.setAttribute('type', 'button');
            button.innerText = 'Aporte';
            button.className = 'aporte-btn';

            direccionesContainer.appendChild(label);
            direccionesContainer.appendChild(input);
            direccionesContainer.appendChild(button);
            direccionesContainer.appendChild(document.createElement('br'));
        }

        // Muestra el botón "Crear Junta" después de generar las direcciones
        document.getElementById('crear-junta-btn').style.display = 'block';
    } else {
        alert('Por favor, ingrese un número válido de participantes (entre 3 y 18) y un monto a aportar (entre 30 y 300).');
    }
});

// Evento para verificar que todas las direcciones estén completas antes de permitir la creación de la junta
document.getElementById('crear-junta-form').addEventListener('submit', function(event) {
    var participantes = document.getElementById('participantes').value;
    for (var i = 1; i <= participantes; i++) {
        var direccion = document.getElementById('direccion-' + i);
        if (!direccion || !direccion.value) {
            event.preventDefault();
            alert('Por favor, complete todas las direcciones de billetera.');
            return;
        }
    }
});














