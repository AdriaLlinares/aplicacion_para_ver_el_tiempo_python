import urllib.request, json 

def termometro():
    url_tiempo = ""
    url_tiempo_barcelona = "https://api.open-meteo.com/v1/forecast?latitude=41.38879&longitude=2.15899&current=temperature_2m,wind_speed_10m&hourly=relative_humidity_2m"
    url_tiempo_segovia   = "https://api.open-meteo.com/v1/forecast?latitude=40.9481&longitude=-4.1184&current=temperature_2m,wind_speed_10m&hourly=relative_humidity_2m"
    url_tiempo_madrid    = "https://api.open-meteo.com/v1/forecast?latitude=40.4168&longitude=-3.7038&current=temperature_2m,wind_speed_10m&hourly=relative_humidity_2m"

    ciudad = ""

    print("Selecciona la ciudad de la que quieres saber el tiempo")
    print("1. Barcelona")
    print("2. Segovia")
    print("3. Madrid")

    opcion = input("Selecciona una opción (1-3): ")

    match opcion:
        case "1":
            print("Has seleccionado Barcelona")
            url_tiempo = url_tiempo_barcelona
            ciudad = "Barcelona"
        case "2":
            print("Has seleccionado Segovia")
            url_tiempo = url_tiempo_segovia
            ciudad = "Segovia"
        case "3":
            print("Has seleccionado Madrid")
            url_tiempo = url_tiempo_madrid
            ciudad = "Madrid"
        case _:
            print("Opción no válida, vuelve a intentarlo")
            exit()

    with urllib.request.urlopen(url_tiempo) as datos:
        parseado = json.load(datos)
        temperatura = parseado["current"]["temperature_2m"]
        viento = parseado["current"]["wind_speed_10m"]
        humedad = parseado["hourly"]["relative_humidity_2m"][0]

        print("El tiempo en "+str (ciudad) + " es:")
        print("Temperatura: "+str (temperatura) +"°C")
        print("Velocidad del viento: "+str (viento) +"km/h")
        print("Humedad relativa: "+str (humedad) +"%")

termometro()