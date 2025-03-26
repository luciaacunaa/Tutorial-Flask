from flask import Flask

app = Flask(__name__)

@app.route("/")
def principal():
    return """
     <a href='/jiji'>jiji</a> 
     <a href='/chau'>!!</a>
    """

@app.route("/jiji")
def jijiji():
    return "<h2>MUEJEJEJE</h2>"

@app.route("/chau")
def jijijint():
    return "<h2>muejejeje</h2>"

@app.route("/sumar/<int:n1>/<int:n2>")
def suma(n1, n2):
    suma = n1+n2
    return F"<h2>{n1} más {n2} es igual a {suma}</h2>"

    