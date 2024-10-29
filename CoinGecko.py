import requests

def obtener_precios_criptomonedas():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    parametros = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": False
    }
    respuesta = requests.get(url, params=parametros)
    
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        print(f"Error al obtener datos: {respuesta.status_code}")
        return []

def mostrar_precios(criptomonedas):
    if not criptomonedas:
        print("No hay datos de criptomonedas para mostrar.")
        return
    
    for i, cripto in enumerate(criptomonedas, start=1):
        print(f"\nCriptomoneda {i}:")
        print(f"  Nombre: {cripto['name']}")
        print(f"  Símbolo: {cripto['symbol']}")
        print(f"  Precio actual: ${cripto['current_price']}")
        print(f"  Cambio en 24h: {cripto['price_change_percentage_24h']}%")
        print(f"  Capitalización de mercado: ${cripto['market_cap']}")

def buscar_criptomoneda_por_nombre(nombre):
    url = f"https://api.coingecko.com/api/v3/coins/markets"
    parametros = {
        "vs_currency": "usd",
        "ids": nombre.lower(),  # CoinGecko usa nombres en minúsculas
        "order": "market_cap_desc",
        "sparkline": False
    }
    respuesta = requests.get(url, params=parametros)

    if respuesta.status_code == 200 and respuesta.json():
        cripto = respuesta.json()[0]
        print("\nInformación de la criptomoneda:")
        print(f"  Nombre: {cripto['name']}")
        print(f"  Símbolo: {cripto['symbol']}")
        print(f"  Precio actual: ${cripto['current_price']}")
        print(f"  Cambio en 24h: {cripto['price_change_percentage_24h']}%")
        print(f"  Capitalización de mercado: ${cripto['market_cap']}")
    else:
        print(f"No se encontró la criptomoneda '{nombre}'. Asegúrate de que el nombre es correcto y está en minúsculas.")

def menu():
    print("Bienvenido a la Aplicación de Criptomonedas")
    while True:
        print("\nOpciones:")
        print("1. Ver precios de las principales criptomonedas")
        print("2. Buscar una criptomoneda por nombre")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            criptomonedas = obtener_precios_criptomonedas()
            mostrar_precios(criptomonedas)
        
        elif opcion == "2":
            nombre = input("Ingresa el nombre de la criptomoneda (en minúsculas, e.g., bitcoin): ")
            buscar_criptomoneda_por_nombre(nombre)
        
        elif opcion == "3":
            print("Saliendo de la aplicación...")
            break
        
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()
