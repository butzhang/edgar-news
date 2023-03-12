from flask import abort, render_template
from flask_simplelogin import login_required

from edgar_news.models import Product

from edgar_news.ext.handlers.edgar_lastest_filing import get_first_post_summarize
from edgar_news.ext.handlers.edgar_lastest_filing import get_first_post


def index():
    a = get_first_post_summarize()
    products = []
    info = get_first_post()

    return render_template("index.html", products=products, info=a)


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
