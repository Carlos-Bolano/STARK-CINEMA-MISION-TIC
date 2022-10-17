from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def indox():    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(Debug=True, port=5500)
    
@app.route('/equipo')
def quehay():
    return "Equipo Crack" 
