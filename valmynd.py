from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <div style="display:flex;">
	    <p style="padding-right:10px;"><a href="/Verkefni 2">Verkefni 2</a></p>
	</div>
    """

