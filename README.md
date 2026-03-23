<div align="center">

![Proteus Banner](https://capsule-render.vercel.app/api?type=waving&color=1e293b&height=250&section=header&text=Conexion%20Proteus&fontSize=60&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Conexi%C3%B3n%20de%20simulaci%C3%B3n%20Proteus%20con%20servicios%20y%20web.&descAlignY=55&descSize=20)

[![Estado del Proyecto](https://img.shields.io/badge/Estado-Activo-success?style=for-the-badge)](https://github.com/y0ner/Proyecto-Conexion-Proteus)
[![Mantenimiento](https://img.shields.io/badge/Mantenimiento-Continuo-blue?style=for-the-badge)](https://github.com/y0ner/Proyecto-Conexion-Proteus)
[![Licencia](https://img.shields.io/badge/Licencia-MIT-green?style=for-the-badge)](https://github.com/y0ner/Proyecto-Conexion-Proteus)

</div>

En este proyecto tecnológico llevaremos a cabo una integración de simulación de circuitos y componentes electrónicos sobre **Proteus**. Permitiendo mapear y comunicar la data de sensores a través de los puertos de hardware virtual hacia una página web estática.

---

## Guía de Inicio Rápido

Para instanciar este proyecto, conectar los servidores de virtualización de puerto y ejecutar el entorno, debe seguir de cerca los siguientes pasos:

### 1. Requerimientos Base
Asegúrese de poseer previamente instalado en su sistema principal **Python** (versión recomendada `3.12.0`).

### 2. Configuración del Gestor 
Abriremos la consola de comandos nativa (`cmd` o `powershell`) y procederemos a la instalación de nuestra envoltura de entorno (Pipenv):
```bash
pip install pipenv
```

### 3. Integración en el Entorno Virtual 
Nos ubicaremos en el sub-directorio de inicio `Main` y asignaremos acceso a la consola virtual.
```bash
cd Main
pipenv shell
```

### 4. Instalación de Dependencias 
Inmediatamente nos redireccionaremos hacia la carpeta de origen `src`, la cual está capacitada con un control de requisitos.
```bash
cd src
pip install -r requirements.txt
```

### 5. Lanzamiento y Control
Procederemos finalmente a inicializar ambos servicios para establecer la pasarela de control electrónico:  
1. Ejecute el oyente del servidor serial: `python Serial.py`  
2. Ejecute el nucleo principal: `python main.py`  
3. Posteriormente inicie su proyecto de diagrama lógico en Proteus y valide la comunicación. ¡Listo!

---

<div align="center">
  <i>Desarrollado y mantenido con estándares de calidad técnica por <a href="https://github.com/y0ner">y0ner</a></i>
</div>
