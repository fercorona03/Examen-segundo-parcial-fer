#Examen segundo parcial 

#Parte 1: clase Proucto
class Producto:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio 
def aplicar_descuento(self, porcentaje):
        """Modifica el precio aplicando un descuento."""
        self.precio -= self.precio * (porcentaje / 100)

def calcular_envio(self):
        """Método vacío ubicado en clases hijas."""
        pass

# clase ProductoFisico
class ProductoFisico(Producto):
    def __init__(self, id, nombre, precio, peso):
        super().__init__(id, nombre, precio)
        self.peso = peso

    def calcular_envio(self):
        """Calcula el costo de envío basado en el peso."""
        return 10 * self.peso
# clase ProductoDigital
class ProductoDigital(Producto):
    def __init__(self, id, nombre, precio, tamaño_archivo):
        super().__init__(id, nombre, precio)
        self.tamaño_archivo = tamaño_archivo

    def calcular_envio(self):
        """Para productos digitales, el costo de envío es 0."""
        return 0
    #Parte 2: Leer archivo CSV
def leer_productos_csv(archivo):
    productos = []
    with open(archivo, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Fpo'] == 'Fisico':
                producto = ProductoFisico(row['id'], row['nombre'], float(row['precio']), float(row['atributo_extra']))
            elif row['Fpo'] == 'Digital':
                producto = ProductoDigital(row['id'], row['nombre'], float(row['precio']), float(row['atributo_extra']))
            productos.append(producto)
    return productos 
#Parte 2: Leer archivo CSV
def leer_productos_csv(archivo):
    productos = []
    with open(archivo, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Fpo'] == 'Fisico':
                producto = ProductoFisico(row['id'], row['nombre'], float(row['precio']), float(row['atributo_extra']))
            elif row['Fpo'] == 'Digital':
                producto = ProductoDigital(row['id'], row['nombre'], float(row['precio']), float(row['atributo_extra']))
            productos.append(producto)
    return productos

#Asumimos que ya tienes definidas las clases producto, ProductoFisico y ProductoDigital
# Lista de productos (usando los datos del CSV que compartiste)
productos = [
    ProductoFisico("1", "Notebook", 1200.0, 2.5),
    ProductoDigital("2", "Software", 200.0, 150.0),
    ProductoFisico("3", "Impresora", 300.0, 7.0),
    ProductoDigital("4", "Ebook", 15.0, 5.0)
]

# Simulación de compra (usuario selecciona todos)
compra = productos

# Aplicar descuento del 10% al primer y último producto
if compra:
    compra[0].aplicar_descuento(10)
    compra[-1].aplicar_descuento(10)

# Calcular totales
total_productos = sum(p.precio for p in compra)
envio_total = sum(p.calcular_envio() for p in compra if isinstance(p, ProductoFisico))
total_final = total_productos + envio_total

# Generar el recibo
lineas = []
lineas.append("RECIBO DE COMPRA\n")
lineas.append("-" * 60 + "\n")
lineas.append(f"{'ID':<6}{'Nombre':<20}{'Precio':<10}{'Tipo':<10}{'Extra':<15}{'Envío':<10}\n")
lineas.append("-" * 60 + "\n")

for p in compra:
    tipo = "Fisico" if isinstance(p, ProductoFisico) else "Digital"
    extra = f"{p.peso} kg" if tipo == "Fisico" else f"{p.tamaño_archivo} MB"
    envio = p.calcular_envio()
    lineas.append(f"{p.id:<6}{p.nombre:<20}{p.precio:<10.2f}{tipo:<10}{extra:<15}{envio:<10.2f}\n")

lineas.append("-" * 60 + "\n")
lineas.append(f"{'TOTAL COMPRA:':<30}${total_final:.2f}\n")

# Guardar en archivo
with open("recibo_compra.txt", "w", encoding="utf-8") as f:
    f.writelines(lineas)
    


