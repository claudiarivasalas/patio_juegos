from tablero_ajedrez_app import app
from flask import render_template, request, redirect

#http://localhost:5000: debería mostrar un tablero de ajedrez de 8 por 8
@app.route('/')
def ajedrez1():
    return render_template('ajedrez.html', numero1=8, numero2=4)

# http://localhost:5000/4: debería mostrar un tablero de ajedrez de 8 por 4
@app.route('/4')
def ajedrez2():
    return render_template('ajedrez.html', numero1=4, numero2=4)

# Haz que otra ruta acepte un solo parámetro (es decir, "/") y renderiza un tablero de ajedrez
# con x cantidad de filas, con colores alternos
@app.route('/<int:numero>')
def ajedrez3(numero):
    return render_template('ajedrez.html', numero1=numero, numero2=int(numero/2))

#BONUS NINJA: Haz que otra ruta acepte 2 parámetro (es decir, "//") y renderiza un tablero de ajedrez
# con x filas e y columnas Las columnas, con colores alternos

@app.route('/<int:numero1>/<int:numero2>')
def ajedrez4(numero1, numero2):
    return render_template('ajedrez.html', numero1=numero2, numero2=int(numero1/2))

#BONUS SENSEI: Haz que otra ruta acepte 4 parámetro (es decir, "////") y 
#renderiza un tablero de ajedrez con x filas e y columnas, con colores alternos, color1 y color2
@app.route('/<int:numero1>/<int:numero2>/<color1>/<color2>')
def ajedrez5(numero1, numero2, color1, color2):
    return render_template('ajedrez.html', numero1=numero2, numero2=int(numero1/2), color1=color1, color2=color2)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "ESTA RUTA NO FUE ENCONTRADA", 404
    #return render_template('404.html'), 404