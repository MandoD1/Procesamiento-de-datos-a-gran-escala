import requests
import pandas as pd
import matplotlib.pyplot as plt

# Configuración
API_KEY = "88d58063ff2b3ec4a7b6f8122aa8f369"  # Reemplázala con tu clave de OpenWeather
CITIES = ["Bogotá", "Buenaventura"]

# Función para obtener datos meteorológicos
def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if "list" not in data:
        print(f"Error en la respuesta de la API para {city}:", data)
        return None
    
    weather_list = data['list']
    df = pd.DataFrame({
        'Fecha': [item['dt_txt'] for item in weather_list],
        'Temperatura (°C)': [item['main']['temp'] for item in weather_list],
        'Humedad (%)': [item['main']['humidity'] for item in weather_list],
        'Vel. Viento (m/s)': [item['wind']['speed'] for item in weather_list],
        'Precipitación (mm)': [item['rain']['3h'] if 'rain' in item and '3h' in item['rain'] else 0 for item in weather_list]
    })
    
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    return df

# Obtener datos para ambas ciudades
df_bogota = get_weather_data("Bogotá")
df_buenaventura = get_weather_data("Buenaventura")

if df_bogota is not None and df_buenaventura is not None:
    # **1. Comparación de Temperaturas**
    plt.figure(figsize=(10, 5))
    plt.plot(df_bogota['Fecha'], df_bogota['Temperatura (°C)'], marker='o', linestyle='-', label="Bogotá")
    plt.plot(df_buenaventura['Fecha'], df_buenaventura['Temperatura (°C)'], marker='s', linestyle='--', label="Buenaventura")
    plt.xlabel("Fecha")
    plt.ylabel("Temperatura (°C)")
    plt.title("Comparación de Temperaturas entre Bogotá y Buenaventura")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    plt.show()
    
    # **2. Comparación de Humedad**
    plt.figure(figsize=(10, 5))
    plt.plot(df_bogota['Fecha'], df_bogota['Humedad (%)'], marker='o', linestyle='-', label="Bogotá")
    plt.plot(df_buenaventura['Fecha'], df_buenaventura['Humedad (%)'], marker='s', linestyle='--', label="Buenaventura")
    plt.xlabel("Fecha")
    plt.ylabel("Humedad (%)")
    plt.title("Comparación de Humedad entre Bogotá y Buenaventura")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    plt.show()
    
    # **3. Comparación de Velocidad del Viento**
    plt.figure(figsize=(10, 5))
    plt.plot(df_bogota['Fecha'], df_bogota['Vel. Viento (m/s)'], marker='o', linestyle='-', label="Bogotá")
    plt.plot(df_buenaventura['Fecha'], df_buenaventura['Vel. Viento (m/s)'], marker='s', linestyle='--', label="Buenaventura")
    plt.xlabel("Fecha")
    plt.ylabel("Velocidad del Viento (m/s)")
    plt.title("Comparación de Velocidad del Viento entre Bogotá y Buenaventura")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    plt.show()
    
    # **4. Dispersión de Temperatura vs. Humedad**
    plt.figure(figsize=(8, 5))
    plt.scatter(df_bogota['Temperatura (°C)'], df_bogota['Humedad (%)'], color='blue', alpha=0.6, label="Bogotá")
    plt.scatter(df_buenaventura['Temperatura (°C)'], df_buenaventura['Humedad (%)'], color='red', alpha=0.6, label="Buenaventura")
    plt.xlabel("Temperatura (°C)")
    plt.ylabel("Humedad (%)")
    plt.title("Comparación de Relación Temperatura vs. Humedad")
    plt.legend()
    plt.grid()
    plt.show()
    
    # **5. Comparación de Precipitación**
    plt.figure(figsize=(10, 5))
    plt.plot(df_bogota['Fecha'], df_bogota['Precipitación (mm)'], marker='o', linestyle='-', label="Bogotá")
    plt.plot(df_buenaventura['Fecha'], df_buenaventura['Precipitación (mm)'], marker='s', linestyle='--', label="Buenaventura")
    plt.xlabel("Fecha")
    plt.ylabel("Precipitación (mm)")
    plt.title("Comparación de Precipitación entre Bogotá y Buenaventura")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    plt.show()
    
    # **Conclusión:**
    print("\nConclusión:")
    print("- Bogotá presenta temperaturas más bajas y variabilidad en la humedad.")
    print("- Buenaventura tiene una humedad más alta y estable, debido a su cercanía con el océano.")
    print("- La velocidad del viento en ambas ciudades varía considerablemente.")
    print("- Buenaventura recibe significativamente más precipitaciones que Bogotá, lo que refuerza su clima húmedo y lluvioso.")
