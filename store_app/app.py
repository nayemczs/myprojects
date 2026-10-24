from flask import Flask, render_template, request, redirect, url_for
from flask_login import current_user, logout_user
from flask_security import Security, login_required
from flask_wtf.csrf import CSRFProtect
from core.forms import ExtendedRegisterForm
from core.models import db as database, user_data_store, Product, User
from settings.settings import APP_CONFIGS, STRIPE_PUBLIC_KEY

app = Flask(__name__)
app.config.from_mapping(APP_CONFIGS)
database.init_app(app)
CSRFProtect(app)
database.init_app(app)
Security(app, user_data_store, register_form=ExtendedRegisterForm)


@app.route('/')
def index():
    database.create_all()
    Product.create_dummy_product()
    User.create_dummy_user()
    product = Product.query.first()
    return render_template('pages/index.html', product=product, stripe_public_key=STRIPE_PUBLIC_KEY)


@app.route('/checkout/create/', methods=['POST'])
def create_checkout_session():
    product_id = request.form.get('product_id')
    if not product_id:
        return redirect(url_for('index'))

    try:
        session_id = Product.create_checkout(product_id, current_user.email)
        return {'sessionId': session_id}
    except Exception as e:
        print(e)
        return {'error': {'message': str(e)}}, 400


@app.route('/checkout/success/<session_id>/<product_id>/')
@login_required
def checkout_success(session_id, product_id):
    Product.process_checkout(session_id, product_id, current_user.get_user_profile())
    return redirect(url_for('index'))


@app.route('/checkout/cancel/')
@login_required
def checkout_cancel():
    return redirect(url_for('index'))


@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
