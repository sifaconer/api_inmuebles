from os import environ


class Config:
    """
    Clase de configurarion de flask

    ...

    Attributes
    ----------
    FLASK_ENV : str
        entorno de ejecución de flask
    CONNFIG_DB : dict
        configuración de conexión mysql
    """
    FLASK_ENV = environ.get('FLASK_ENV')

    CONNFIG_DB = {
        'user': environ.get('MYSQL_DATABASE_USER'),
        'password': environ.get('MYSQL_DATABASE_PASSWORD'),
        'host': environ.get('MYSQL_DATABASE_HOST'),
        'port': environ.get('MYSQL_DATABASE_PORT'),
        'database': environ.get('MYSQL_DATABASE_SCHEMA')
    }
