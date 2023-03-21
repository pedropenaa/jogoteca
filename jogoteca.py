from flask import Flask, render_template, request, redirect, session, flash



class Jogo:
    def __init__(self, nome, categoria, console) :
      self.nome      = nome 
      self.categoria = categoria
      self.console   = console


jogo1 = Jogo('Valorant','FPS', 'PC')
jogo2 = Jogo('Rainbow six', 'FPS', 'xbox')
jogo3= Jogo('Homem Aranha', 'História', 'PS4')
lista = [jogo1, jogo2, jogo3]


app = Flask(__name__)
app.secret_key = "cano"



@app.route("/")
def index():
  
    return render_template('lista.html', titulo = 'Jogos', jogos= lista)



@app.route("/novo")
def novo_jogo():
    return render_template("novo.html", titulo = "Novo Jogo")





@app.route("/criar", methods = ['POST'])
def criar():
    nome      = request.form['nome']
    categoria = request.form['categoria']
    console   = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')





@app.route("/login")
def login():
    return render_template("login.html")






@app.route("/autenticar", methods=['POST'])
def autenticar():

    if 'harry' == request.form['usuario'] and 'alohomora' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + 'Usuario logado com sucesso')
        return redirect('/')
    else:
        flash('Usuario não Logado ')
        return redirect("/login")
    
    
    
    










app.run(debug=True)
