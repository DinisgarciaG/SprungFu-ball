from flask import Flask, render_template

app = Flask(__name__)

# criar a 1º página do site 
# route -> sprungfußb.com/
# função -> o que queres exibir nessa página
#template 

@app.route("/")
def hompage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

#colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

#servidor do git hub
