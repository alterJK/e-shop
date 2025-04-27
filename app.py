from flask import Flask, render_template, abort

from config import DEBUG
from test_data import PRODUCTS_LIST

app = Flask(__name__)


# декаратор главной страницы
@app.route("/")
def home():
    return render_template("home.html")


# декаратор страницы "О нас"
@app.route("/about")
def about():
    return render_template("about.html")


# декаратор страницы каталога
@app.route("/catalog")
def catalog():
    return render_template("catalog.html", products=PRODUCTS_LIST)


# декаратор страницы корзины товаров
@app.route("/cart")
def cart():
    return render_template("cart.html")


# декаратор страниы контактов
@app.route("/contacts")
def contacts():
    return render_template("contacts.html")


# декаратор страницы информации о доставке
@app.route("/delivery")
def delivery():
    return render_template("delivery.html")


# декаратор страницы продукта
@app.route("/product/<string:product_id>")
def product(product_id):
    # Поиск товара по его id
    PRODUCT = next(
        (product for product in PRODUCTS_LIST if product["id"] == product_id), None
    )
    if PRODUCT is None:
        abort(404)  # Если товар не найден, возвращаем ошибку 404
    return render_template("product.html", product=PRODUCT)


# старт приложения
if __name__ == "__main__":
    app.run(debug=DEBUG)
