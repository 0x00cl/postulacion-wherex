# Postulación Wherex

Prueba tecnica para postular al puesto de DevOps Engineer Junior en Wherex.

## Ejecucion app metricas

Pimero clonar el repositorio e ingresar al repositorio clonado

```
$ git clone https://github.com/0x00cl/postulacion-wherex.git
$ cd postulacion-wherex
```

### Local (desarrollo)

Activar ambiente virtual de Python

```
$ python -m venv venv
```

Una vez activado el ambiente virtual, instalar dependencias y ejecutar flask.

```
$ pip install -r requirements.txt
$ export FLASK_APP=myapp
$ export FLASK_DEBUG=1
$ flask run
```

La aplicación deberia quedar disponible en http://localhost:5000/metrics


### Docker/Podman

Ejecutar el script bash `deploy.sh`

```
$ ./deploy.sh
```

Se construye una imagen llamada `wherex/metrics:latest` y queda corriendo como contenedor, quedando disponible en http://localhost:8000/metrics

## Configuración

### Gunicorn (Despliegue para producción)

Gunicorn es un servidor Python WSGI que se utiliza para desplegar aplicaciones desarrolladas con Flask en ambientes de producción.

La configuración de acuerdo a su [documentación](https://docs.gunicorn.org/en/stable/configure.html) tiene el siguiente orden

De menos a más importante/precendencia:

1. Environment Variables
2. Framework Settings
3. Configuration File
4. GUNICORN_CMD_ARGS
5. Command Line

Por lo que si se quiere ejecutar en contenedor se le puede pasar la variable de ambiente `GUNICORN_CMD_ARGS` al comando de docker con las configuraciones deseadas, por ejemplo el numero de `workers`.

```
$ docker run -p 8000:8000 -e GUNICORN_CMD_ARGS="--workers=4" wherex/metrics
```