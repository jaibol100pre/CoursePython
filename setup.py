from setuptools import setup

setup (

    name="Paquete calculos",
    version="1.0",
    descripcion="Calcula la edad de una persona",
    author="Jaibol",
    author_email="jaibolsantaella@gmail.com",
    url="profesionalesdevenezuela.org.ve",
    #package=["Directorio","SubDirectorio.Modulo"]
    package=["CarpetaPaquetes","SubModulos.Calcular"]

)

'''
Abrir un terminal y crear un archivo distribuible

cd /raiz-del-proyecto
cd ~/CoursePython-original/
python3 setup.py sdist

--Ir a la Raiz del proyecto
cd /raiz-del-proyecto/dist
cd ~/CoursePython-original/dist

--Crear Entorno Virtual
python3 -m venv .venv

--Activar el entono Virtual 
source .venv/bin/activate

--Si deseas desactivar tu entorno virtual escribe:
deactivate

--Verificar que el entorno Virtual está activo
which python
cd ~/CoursePython-original/dist
pip3 install 'Paquete calculos-1.0.tar.gz'
pip list

--Desinstalar
~/CoursePython-original/dist$ pip3 uninstall Paquete-calculos

'''