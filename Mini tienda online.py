articulos = {}
menu = ["1. Crear artículo",
"2. Listar artículos",
"3. Buscar artículo por id",
"4. Actualizar artículo",
"5. Eliminar artículo",
"6. Alternar activo/inactivo",
"7. Salir"]
print("Estas son las acciones que puedes realizar" ,menu)
def opcion():
    accion = ""
    while accion != 7:
        accion = int(input("Escoge qué opción desea realizar: "))
        match accion:
            case 1:
                print("Has elegido la opción de: " ,menu[0])
                id = int(input("Introduce el id del artículo que deseas crear: "))
                while id in articulos:
                    print("Ya existe un artículo con este ID, utiliza otro")
                    id = int(input("Introduce el id del artículo que deseas crear: "))
                if id not in articulos:
                    articulos["id"] = id
                    nombre = str(input("Introduce el nombre del artículo que deseas crear: "))
                    articulos["nombre"] = nombre
                    precio = float(input("Introduce el precio del artículo que deseas crear: "))
                    if precio > 0:
                        articulos["precio"] = precio
                    else:
                        print("No puedes crear un artículo con un valor menor o igual que 0")
                    stock = int(input("Introduce el stock del artículo que deseas crear: "))
                    if stock >= 0:
                        articulos["stock"] = stock
                    else:
                        print("No puedes crear un artículo con un stock menor que 0")
                    activo = stock > 0
                    if stock > 0:
                        articulos["activo"] = True
                    else:
                        articulos["activo"] = False
                    articulo = {
                        "id": id,
                        "nombre": nombre,
                        "precio": precio,
                        "stock": stock,
                        "activo": True
                    }
                    articulos[id] = articulo
                    print(articulos)
            case 2:
                print("Has elegido la opción de: " ,menu[1])
                print(articulos)
            case 3:
                print("Has elegido la opción de: " ,menu[2])
                id = int(input("Introduce el id del artículo que deseas buscar: "))
                if id in articulos:
                    print(articulos[id])
                else:
                    print("No encontrado")
            case 4:
                print("Has elegido la opción de: " ,menu[3])
                id = int(input("Introduce el id del artículo que deseas actualizar: "))
                if id in articulos:
                    articulo = articulos[id]    
                    print(articulo)
                    nuevo_nombre = input("Introduce un nuevo nombre al artículo existente: ")
                    if nuevo_nombre != "":
                        articulo["nombre"] = nuevo_nombre
                    nuevo_precio = float(input("Introduce un nuevo precio al artículo existente: "))
                    if nuevo_precio != "":
                        if nuevo_precio > 0: 
                            articulo["precio"] = nuevo_precio
                        else:
                            print("No puedes actualizar un artículo con un valor menor o igual que 0")
                    nuevo_stock = int(input("Introduce un nuevo stock al artículo existente: "))
                    if nuevo_stock != "":
                        if nuevo_stock >= 0:
                            articulo["stock"] = nuevo_stock
                            articulo["activo"] = nuevo_stock > 0
                        else:
                            print("No puedes actualizar un artículo con un stock menor que 0")
            case 5:
                print("Has elegido la opción de: " ,menu[4])
                id = int(input("Introduce el id del artículo que deseas eliminar: "))
                if id in articulos:
                    articulos[id]["activo"] = False
                else:
                    print("No encontrado")
            case 6:
                print("Has elegido la opción de: " ,menu[5])
                id = int(input("Introduce el id del artículo que deseas altrnar: "))
                if id in articulos:
                    articulos[id]["activo"] = True
            case 7:
                print("Has elegido la opción de: " ,menu[6])
                print("Saliendo...")
    return accion

accion = opcion()
