from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///shop.db'
db=SQLAlchemy

class Item(db.Model):
    id=db.Column(db.Integer, primary_key=True) #primaty_ket=True - поле является первичным ключем и при добавлении будет проставляться в автоматическом режиме
    title=db.Column(db.String(100), nullable=False) #nullable=False - поле не может быть пустым
    prise=db.Column(db.Integer, nullable=False)
    isActive=db.Column(db.Boolean, default=True) #default=True поле по умолчанию будет True


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