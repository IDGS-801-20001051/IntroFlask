from flask import Flask, render_template, request
from io import open
from datetime import datetime

app = Flask(__name__)

class SalaDeCine:
    precio_entrada = 12
    lista_ventas = []

    def calcular_rebaja(self, total, entradas):
        if entradas > 5:
            return total * 0.85
        elif 3 <= entradas <= 5:
            return total * 0.90
        else:
            return total

    def validar_entradas(self, asistentes, entradas):
        return entradas <= asistentes * 7

    def guardar_venta(self, comprador, total):
        self.lista_ventas.append((comprador, total))

    def mostrar_resumen_ventas(self):
        if not self.lista_ventas:
            return "No se realizaron ventas."
        else:
            resumen = ""
            total_recaudado = 0
            for comprador, total in self.lista_ventas:
                resumen += f"{comprador}: ${total:.2f}<br>"
                total_recaudado += total
            resumen += f"Total Recaudado: ${total_recaudado:.2f}"
            return resumen

cine = SalaDeCine()



class Usuario:
    def __init__(self, nombre, apellido_p, apellido_m, dia, mes, anio, sexo):
        self.nombre = nombre
        self.apellido_p = apellido_p
        self.apellido_m = apellido_m
        self.dia = int(dia)
        self.mes = int(mes)
        self.anio = int(anio)
        self.sexo = sexo
        self.edad = self.calcular_edad()
        self.signo_chino = self.obtener_signo_chino()

    def calcular_edad(self):
        hoy = datetime.today()
        edad = hoy.year - self.anio - ((hoy.month, hoy.day) < (self.mes, self.dia))
        return edad

    def obtener_signo_chino(self):
        signos_chinos = [
            "mono", "gallo", "perro", "cerdo", "rata", "buey",
            "tigre", "conejo", "dragon", "serpiente", "caballo", "cabra"
        ]
        return signos_chinos[self.anio % 12]


@app.route("/")
def index():
    titulo="IDGS801"
    lista=["perdro","juan","luis"]
    return render_template("index.html",titulo=titulo,lista=lista)

@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")

@app.route("/hola")
def hola():
    return "<h1>Hola mundo hola</h1>"

@app.route("/user/<string:usuario>")
def user(usuario):
    return f"<h1<!Hola,{usuario}</h1>"

@app.route("/numero/<int:n>")
def numero(n):
    return f"<h1>El numero es: {n}</h1>"

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return f"<h1>Hola, {username} Tu ID es: {id}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return f"La suma es: {n1+n2}"

@app.route("/default/")
@app.route("/default/<string:param>")
def func(param="juan"):
    return f"<h1>Hola, {param}<h1>"



@app.route("/OperasBas", methods=["GET", "POST"])
def operas():
    resultado = None
 
    if request.method == "POST":
        n1 = int(request.form.get("n1"))
        n2 = int(request.form.get("n2"))
        operacion = request.form.get("operacion")
 
        if operacion == "suma":
            resultado = f"{n1} + {n2} = {n1 + n2}"
        elif operacion == "resta":
            resultado = f"{n1} - {n2} = {n1 - n2}"
        elif operacion == "multiplicacion":
            resultado = f"{n1} * {n2} = {n1 * n2}"
        elif operacion == "division":
            if n2 != 0:
                resultado = f"{n1} / {n2} = {n1 / n2}"
            else:
                resultado = "Error: No se puede dividir por cero."
 
    return render_template("OperasBas.html", resultado=resultado)


@app.route("/cinepolis", methods=["GET", "POST"])
def cinepolis():
    resultado = None

    if request.method == "POST":
        nombre_cliente = request.form.get("nombre")
        cantidad_personas = int(request.form.get("personas"))
        numero_entradas = int(request.form.get("boletos"))
        forma_pago = request.form.get("metodo_pago")

        if cine.validar_entradas(cantidad_personas, numero_entradas):
            total_sin_descuento = cine.precio_entrada * numero_entradas
            total_con_descuento = cine.calcular_rebaja(total_sin_descuento, numero_entradas)

            if forma_pago == "tarjeta":
                total_con_descuento *= 0.90

            cine.guardar_venta(nombre_cliente, total_con_descuento)
            resultado = f"${total_con_descuento:.2f}"
        else:
            resultado = "No puedes comprar más de 7 boletos por persona."

    return render_template("cinepolis.html", resultado=resultado)

@app.route("/zodiaco", methods=["GET", "POST"])
def zodiaco():
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido_p = request.form["apellido_p"]
        apellido_m = request.form["apellido_m"]
        dia = request.form["dia"]
        mes = request.form["mes"]
        anio = request.form["anio"]
        sexo = request.form["sexo"]

        usuario = Usuario(nombre, apellido_p, apellido_m, dia, mes, anio, sexo)
        return render_template("zodiaco.html", usuario=usuario)

    return render_template("zodiaco.html", usuario=None)



if __name__ =="__main__":
    app.run(debug=True, port=3000) 