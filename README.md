# Plataforma de Gestión de Empleados

El siguiente repositorio, cumple con el siguiente enunciado:


Empresas Polar requiere un sistema para la gestión de sus empleados en el cual se pueda visualizar los datos de los mismos.

Los datos que se tienen de los empleados además de sus datos personales son, fecha de ingreso, tipo de contrato, fecha de término de contrato, cargo, dependencia en la que labora y salario devengado.

Los tipos de usuarios que debe manejar el sistema son superadministrador, administrador, y usuario final.

El usuario final debe estar en la capacidad poder visualizar su información y una retroalimentación realizada mensualmente por la compañía acerca de su desempeño junto con un puntaje asignado.

El administrador de la plataforma debe estar en la capacidad de poder agregar usuarios al sistema y gestionar los datos de los mismos.

Un superadministrador ejerce el control total de la plataforma (usuarios y administradores).

## Explicación:

El sistema esta desarrollado en VUE (Framework para el Front-end) y en Flask (Framework de python para el Back-end)

### En el repositorio encontrará las siguientes carpetas:

- Client (VUE 2, haciendo uso de Bootstrap, Fontawesome y SweetAlert2)
- Database (Script SQL de creación para la base de datos SQLite3)
- Server (Programación de la API REST - Flask)

# Despliegue y demostración

Para el despliegue y ver el funcionamiento de la plataforma, simplemente necesitamos lanzar el servidor FLASK, pues en este ya se encuentra el "BUILD" del cliente hecho en VUE.

Lo primero que debemos hacer es clonar el repositorio y posteriormente ubicarnos en la carpeta "server"

```bash
cd server
```
### Configurar variables de configuración

Una vez dentro de la carpeta debemos configurar el archivo config.py que se encuentra dentro de la carpeta "src" en la linea 10 y 11 para que funcione corectamente el envio de correos:

```bash
CORREO_EMPRESA = 'su_correo'
PASSWORD_CORREO = 'contraseña_correo'
```

### Instalación de dependencias

En el proyecto se distribuye un fichero (requirements.txt) con todas las dependencias. Para instalarlas basta con ejectuar:

```bash
pip install -r requirements.txt
```

### Variables de entorno

Para que el sistema funcione debe configurar las siguientes variables de entorno ejecutando los siguientes comandos:

```bash
$env:FLASK_ENV = "development"
$env:FLASK_APP = "src/app.py"
```

### Ejecución con el servidor que trae Flask

Una vez que haya descargado el proyecto, creado las variables de entorno e instalado las dependencias, pueds arrancar el proyecto ejecutando:

```bash
flask run
```