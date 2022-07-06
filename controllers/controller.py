from app import app
from flask import render_template
from models.list_order import orders

@app.route('/orders')
def index():
    return render_template('index.html', all_orders=orders)

@app.route('/orders/<order>')
def order_individual(order):
    for i in orders:
        if i.name == order:
          return render_template('order.html', customer_name=i.name, game_name=i.title, quantities=i.quantity)