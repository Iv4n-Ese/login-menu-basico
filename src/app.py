from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('/login.html')

@app.route('/index')
def Index():
    return render_template('index.html')

#@app.route('/panel')  // dashboard básico
#def Panel():
#    return render_template('panel.html')

@app.route('/salir')
def Salir():
    return redirect('/')

@app.route('/acceso')
def Acceso():
    return render_template('seleccion.html')

@app.route('/registro')
def Registro():
        return render_template('/registro.html')
    
@app.route('/recuperar')
def Recuperar():
    return render_template('recuperar.html')

if __name__ == '__main__':
    app.run(port = 3060, debug = True)