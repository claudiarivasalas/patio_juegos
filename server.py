from tablero_ajedrez_app import app
from tablero_ajedrez_app.controllers import controlador


if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración