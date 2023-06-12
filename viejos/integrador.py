MIN_CANT = 0
MAX_CANT = 1000
MIN_PRECIO = 100
MAX_PRECIO = 301
tipo_prod = ["b", "j", "a"]
precio_prod = range(MIN_PRECIO, MAX_PRECIO)
cant_prod = range(MIN_CANT,MAX_CANT)
cant_stock = range(5)

total_jabon = 0

for i in cant_stock:
    producto = input("Ingrese un tipo de producto: ")
    while not (producto in tipo_prod):
        producto = input("Ingrese un tipo de producto válido (b,j,a): ")

    precio = input("ingrese el precio del producto: ")
    while not ( precio.isdigit() and int(precio) in precio_prod):
        precio = input("ingrese un precio válido (100 a 300): ")

    precio = int(precio)

    cantidad = input("Ingrese la cantidad: ")
    while not (cantidad.isdigit() and int(cantidad) in cant_prod):
        cantidad = input("Ingrese una cantidad válida {} y {}".format(MIN_CANT, MAX_CANT))

    cantidad = int(cantidad)
    marca_fabricante = input("Ingrese la marca y el fabricante: ")
    while len(marca_fabricante) == 0:
        marca_fabricante = input("Ingrese la marca y el fabricante válido: ")

    if producto == "j":
        total_jabon = total_jabon + cantidad

    if i==0:
        item_mas_unidades = marca_fabricante
        total_item = cantidad
        
        if producto == "b":
            barbijo_cantidad = cantidad
            barbijo_fabricante = marca_fabricante

    else:

        if total_item < cantidad:
            item_mas_unidades = marca_fabricante
            total_item = cantidad
            nombre_item = producto

        if producto == "b":
            if barbijo_cantidad < precio:
                barbijo_cantidad = cantidad
                barbijo_fabricante = marca_fabricante

print("el más caro de los barbijos, {} del {}".format(barbijo_cantidad, barbijo_fabricante))
print("item con más unidades es, el fabricante es {}".format(nombre_item. item_mas_unidades))
print("cuantas unidades de jabon {}".format(total_jabon))
