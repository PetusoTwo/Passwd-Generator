<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Generador de Contraseñas Aleatorias</title>
</head>
<body>
    <h1>Generador de Contraseñas Aleatorias</h1>
    <p>Este programa en Python genera contraseñas aleatorias basadas en la cantidad de caracteres especificada por el usuario. La contraseña generada puede incluir números, letras y caracteres especiales, dependiendo de la preferencia del usuario.</p>

    <h2>Descripción</h2>
    <p>El generador de contraseñas permite al usuario:</p>
    <ul>
        <li>Especificar la longitud total de la contraseña.</li>
        <li>Decidir si la contraseña debe incluir números.</li>
        <li>Decidir si la contraseña debe incluir caracteres especiales.</li>
    </ul>

    <h2>Requisitos</h2>
    <ul>
        <li>Python 3.x</li>
        <li>PyQt6</li>
    </ul>

    <h2>Instalación</h2>
    <ol>
        <li><strong>Clona el repositorio:</strong>
            <pre><code>git clone https://github.com/PetusoTwo/Password-Generator.git</code></pre>
        </li>
        <li><strong>Accede al directorio del proyecto:</strong>
            <pre><code>cd Password-Generator</code></pre>
        </li>
        <li><strong>Instala las dependencias:</strong>
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
    </ol>

    <h2>Uso</h2>
    <ol>
        <li><strong>Ejecuta el programa:</strong>
            <pre><code>python main.py</code></pre>
        </li>
        <li><strong>Interfaz de usuario:</strong>
            <ul>
                <li><strong>Campo de texto para la cantidad:</strong> Ingresa el número total de caracteres para la contraseña.</li>
                <li><strong>Botón "Generar":</strong> Genera una contraseña aleatoria basada en las configuraciones actuales.</li>
                <li><strong>Botón "Copiar":</strong> Copia la contraseña generada al portapapeles.</li>
                <li><strong>Configuraciones de la contraseña:</strong>
                    <ul>
                        <li>Un cuadro de diálogo aparecerá preguntando si deseas incluir números en la contraseña.</li>
                        <li>Otro cuadro de diálogo aparecerá preguntando si deseas incluir caracteres especiales en la contraseña.</li>
                    </ul>
                </li>
            </ul>
        </li>
    </ol>

    <h2>Ejemplo</h2>
    <ol>
        <li>Ingresa una cantidad en el campo de texto.</li>
        <li>Cuando se te pregunte, selecciona si deseas incluir números y caracteres especiales.</li>
        <li>Presiona el botón "Generar" para obtener la contraseña aleatoria.</li>
        <li>Usa el botón "Copiar" para copiar la contraseña al portapapeles.</li>
    </ol>

    <h2>Capturas de Pantalla</h2>
    <img src="https://github.com/user-attachments/assets/ba07d102-2a93-416a-8843-b144abe164be" alt="Interfaz de Usuario">

    <h2>Contribuciones</h2>
    <p>Si deseas contribuir a este proyecto, por favor sigue estos pasos:</p>
    <ol>
        <li>Haz un fork del repositorio.</li>
        <li>Crea una nueva rama (<code>git checkout -b feature/nueva-funcionalidad</code>).</li>
        <li>Realiza tus cambios y haz commits (<code>git commit -am 'Agrega nueva funcionalidad'</code>).</li>
        <li>Empuja tus cambios (<code>git push origin feature/nueva-funcionalidad</code>).</li>
        <li>Crea un nuevo Pull Request.</li>
    </ol>

    <h2>Licencia</h2>
    <p>Este proyecto está licenciado bajo los términos de la Licencia MIT. Consulta el archivo <a href="LICENSE">LICENSE</a> para más detalles.</p>
</body>
</html>
