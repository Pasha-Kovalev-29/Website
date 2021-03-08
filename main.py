from flask import Flask, render_template
from flask import SQLAlchemy


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///shop.db'
db=SQLAlchemy



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