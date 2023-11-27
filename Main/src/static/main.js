// Definir la URL de la API y el intervalo de consulta
const API_URL = "http://127.0.0.1:8000/sensor";
const intervaloConsulta = 1000;

// Arreglos para almacenar valores de temperatura y humedad
let temperaturaValues = [];
let humedadValues = [];

// Función para reemplazar clases de un elemento
function replaceClass(element, oldClass, newClass) {
  const classesToRemove = oldClass.split(' ');
  const classesToAdd = newClass.split(' ');

  classesToRemove.forEach(className => {
    if (element.classList.contains(className)) {
      element.classList.remove(className);
    }
  });

  classesToAdd.forEach(className => {
    element.classList.add(className);
  });
}

// Función para calcular el promedio de un conjunto de datos
function calcularPromedio(datos) {
  return parseInt((datos[0] + datos[2] + datos[4]) / 3);
}

// Función para mostrar datos de temperatura y humedad promedio
function mostrarDatosPromedio(promedioTemperatura, promedioHumedad) {
  document.getElementById("pTemp").innerText = promedioTemperatura + "°C";
  document.getElementById("pHum").innerText = promedioHumedad + "%";
}

// Función para mostrar datos de sensores individuales
function mostrarDatosSensores(data) {
  document.getElementById("sensor1").innerText = data[0][0] + "°C";
  document.getElementById("sensor2").innerText = data[0][2] + "°C";
  document.getElementById("sensor3").innerText = data[0][4] + "°C";
  document.getElementById("hum1").innerText = data[0][1] + "%";
  document.getElementById("hum2").innerText = data[0][3] + "%";
  document.getElementById("hum3").innerText = data[0][5] + "%";
  document.getElementById("twater").innerText = data[0][6] + "°C";
}

// Función para actualizar las clases basadas en el promedio de temperatura
function actualizarClasesPromedioTemperatura(promedioTemperatura) {
  const waves = ["w1", "w2", "w3", "w4"];

  waves.forEach((wave, index) => {
    const threshold = 45 - index * 5;
    const condition = promedioTemperatura > threshold;
    const classToAdd = condition ? "none none" : `wave wave${index + 1}`;
    const classToRemove = condition ? `wave wave${index + 1}` : "none none";

    replaceClass(document.getElementById(wave), classToRemove, classToAdd);
  });
}

// Función asincrónica para obtener datos de la API
async function obtenerDatosDeLaAPI() {
  try {
    // Obtener datos de la API
    const response = await fetch(API_URL);
    const data = await response.json();

    // Calcular promedios y mostrar datos
    const promedioTemperatura = calcularPromedio(data[0].slice(0, 6));
    const promedioHumedad = calcularPromedio(data[0].slice(1, 7));

    mostrarDatosPromedio(promedioTemperatura, promedioHumedad);
    mostrarDatosSensores(data);
    actualizarClasesPromedioTemperatura(promedioTemperatura);

    // Mostrar información en la consola
    console.log("Valores de la API:", data);
    console.log("Promedio de Temperatura:", promedioTemperatura);
    console.log("Promedio de Humedad:", promedioHumedad);

  } catch (error) {
    // Manejar errores en la obtención de datos de la API
    console.error("Error al obtener datos de la API:", error);

  } finally {
    // Configurar la siguiente consulta después del intervalo especificado
    setTimeout(obtenerDatosDeLaAPI, intervaloConsulta);
  }
}

// Iniciar la obtención de datos de la API
obtenerDatosDeLaAPI();
