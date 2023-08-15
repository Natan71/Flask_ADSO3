from flask import Flask
app=Flask(__name__)

@app.route('/') #decorador que dara como retorno un string asignado
def inicio():
    return "<h1> Hola, es mi Primera Aplicación Web con ADSO3</h1>"

@app.route('/registro')
def adicionar():
    return "<h1> Registrar Usuario </h1>"

@app.route('/consulta')
def consulta():
    return "<h1> Consultar </h1>"

@app.route('/fin')
def salir():
    return "<h1> Nos Vemos </h1>"

if __name__ == '__main__': # este fragmento de codigo permite iniciar el servidor web directamente
    app.run('127.0.0.1', 5000, debug=True) # con "debug" si se hace una modificación reiniciara el servicio