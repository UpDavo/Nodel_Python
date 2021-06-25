from flask import Flask
from Reto1.clases.create_table import create_table
from Reto2.clases.set_sheets_instagram import set_sheets_instagram

app = Flask(__name__)
PORT = 5000
DEBUG = False


@app.errorhandler(404)
def not_found(error):
    return "No encontrado"


@app.route("/", methods=["GET"])
def index():
    return "Hola Mundo"


@app.route("/setSheets", methods=["GET"])
def setSheets():
    tabla = create_table(0, 1, "Analisis")
    resultado = tabla.init()
    print(resultado)
    return "Done"

@app.route("/setInstagram", methods=["GET"])
def setInstagram():
    instanciaInstagram = set_sheets_instagram()
    dataFrame = instanciaInstagram.getData()
    resultado = instanciaInstagram.ingresarTablaGoogleSheets(1,"Instagram Data",dataFrame)
    print(resultado)
    return "Done"

@app.route("/sendInvitations", methods=["GET"])
def sendInvitations():
    return "Done"


if __name__ == "__main__":
    app.run(port=PORT, debug=DEBUG)
