from flask import abort, render_template
from flask_simplelogin import login_required

from edgar_news.models import Product

from edgar_news.ext.handlers.edgar_lastest_filing import get_lastest_filings


def index():
    products = Product.query.all()
    info = get_lastest_filings()
    return render_template("index.html", products=products, info=info)


def product(product_id):
    product = Product.query.filter_by(id=product_id).first() or abort(
        404, "produto nao encontrado"
    )
    return render_template("product.html", product=product)


@login_required
def secret():
    return "This can be seen only if user is logged in"


@login_required(username="admin")
def only_admin():
    return "only admin user can see this text"
