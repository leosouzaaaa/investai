from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 InvestAI está no ar!</h1>
    <p>Entre em contato conosco:</p>
    <a href="https://wa.me/+55061998611133" target="_blank">
        📱 Fale no WhatsApp
    </a><br>
    <a href="leonardolopesesouza@gmail.com">
        📧 Enviar e-mail
    </a>
    """

if __name__ == "__main__":
    app.run(debug=True)
