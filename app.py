from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <div style="display:flex;">
	    <p style="padding-right:10px;"><a href="/">About</a></p>
	    <p style="padding-right:10px;"><a href="/pictures">Pictures</a></p>
	    <p style="padding-right:10px;"><a href="/biography">Biography</a></p>
	</div>
    """

@app.route("/pictures")
def pictures():
	return("<a href='/'>pictures</a>")

@app.route("/biography")
def biography():
	return("<a href='/'>biography</a>")