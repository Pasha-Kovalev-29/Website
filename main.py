from flask import Flask, render_template

app=Flask(__name__)

#главная страница
@app.route('/')
def index():
    return render_template('index.html')

#страница с информацией про магазин
@app.route('/about')
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.run(debug=True)