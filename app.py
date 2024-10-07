from flask import Flask
from routes.product_routes import product_routes
from routes.order_routes import order_routes
from routes.order_product_routes import order_product_routes

app = Flask(__name__)

# Registrar Blueprints para las rutas
app.register_blueprint(product_routes)
app.register_blueprint(order_routes)
app.register_blueprint(order_product_routes)

if __name__ == '__main__':
    app.run(debug=True)
