from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #настройка позволяющая выполнять какие-либо настройки с БД
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)  # primaty_ket=True - поле является первичным ключем и при добавлении будет проставляться в автоматическом режиме
    title = db.Column(db.String(100), nullable=False)  # nullable=False - поле не может быть пустым
    prise = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)  # default=True поле по умолчанию будет True
    # text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return self.title

# главная страница
@app.route('/')
def index():
    items= Item.query.order_by(Item.prise).all()
    return render_template('index.html', data=items)


# страница с информацией про магазин
@app.route('/about')
def about():
    return render_template('about.html')


# страница для добавления товара
@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title=request.form['title']
        prise = request.form['prise']

        item=Item(title=title, prise=prise)

        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')
        except:
            return 'Получилась ошибка'
    else:
        return render_template('create.html')


if __name__ == "__main__":
    app.run(debug=True)
