from flask import Flask
import mysql.connector
from mysql.connector import errorcode


def init_db(config):
    """
    Conexión a base de datos Mysql.

    Parameters
    ----------
    config : dict
        valores de configuración de conexión a la base de datos

    Returns
    -------
    mysql.connector
        conexión a base de datos mysql

    Raises
    ------
    mysql.connector.Error
        error de mysql.
    """
    try:
        cnx = mysql.connector.connect(**config)
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ERROR: ER_ACCESS_DENIED_ERROR")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("ERROR: ER_BAD_DB_ERROR")
        else:
            print(err)
        cnx.close()


def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    app.config["CONN"] = init_db(app.config.get("CONNFIG_DB"))

    with app.app_context():
        from inmuebles import routes

        app.register_blueprint(routes.inmuebles_bp)

        return app
