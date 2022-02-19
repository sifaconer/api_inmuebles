class Status:
    """
    Clase de Status de referencia a la base de datos

    ...

    Attributes
    ----------
    name : str
        name del inmueble
    id : number
        id del inmueble
    label : str
        label del inmueble
    """
    def __init__(
        self,
        name,
        id,
        label
    ):
        self.name = name
        self.id = id
        self.label = label

    def to_json(self):
        return {'name': self.name, 'id': self.id, 'label': self.label}


class Inmuebles:
    """
    Clase de Inmuebles de referencia a la base de datos

    ...

    Attributes
    ----------
    address : str
        address del inmuebles 
    city : str
        city del inmueble
    price : number
        price del inmueble
    description : str
        description del inmueble
    status : str
        status del inmueble
    id_status : number
        id_status del inmueble
    label_status : str
        label_status del inmueble
    """

    def __init__(
        self,
        address,
        city,
        price,
        description,
        status,
        id_status,
        label_status,
    ):
        self.address = address
        self.city = city
        self.price = price
        self.description = description
        self.status = Status(status, id_status, label_status)

    def to_json(self):
        return {
            'address': self.address,
            'city': self.city,
            'price': self.price,
            'description': self.description,
            'status': self.status.to_json(),
            }


def query_builder(
    query,
    fyear,
    fcity,
    fstatus,
):
    """
    Construye el query sql con los parametros de filtro.

    Si los parametros son pasados en None no se agregan al query.

    Parameters
    ----------
    query : str
        consulta sql base
    fyear : int, optional
        año de consulta en el query
    fcity : str, optional
        ciudad de consulta en el query
    fstatus : int, optional
        código de status de consulta en el query

    Returns
    -------
    list
        [query, params], query sql y dict de parametros
    """

    params = {}

    if fyear is not None:
        query += ' AND hp.year = %(year)s '
        params['year'] = fyear
    if fcity is not None:
        query += ' AND hp.city = %(city)s '
        params['city'] = fcity
    if fstatus is not None:
        query += ' AND ss.id = %(status)s '
        params['status'] = fstatus

    return [query, params]


def get_inmuebles_by_filter(
    db,
    fyear,
    fcity,
    fstatus,
):
    """
    Listado de todos los inmuebles por filtro.

    Si los filtros son pasados en None se listan todos los inmuebles.

    Parameters
    ----------
    db : mysql, optional
        conexión de la base de datos
    fyear : int, optional
        año de consulta en el query
    fcity : str, optional
        ciudad de consulta en el query
    fstatus : int, optional
        código de status de consulta en el query

    Returns
    -------
    list
        [inmuebles], listado de inmuebles
    """

    cursor = db.cursor()

    sql = '''
    SELECT hp.address, hp.city, hp.price, 
    hp.description, ss.name status, 
    ss.id id_status,
    ss.label label_status
    FROM habi_db.property hp 
    left join habi_db.status_history sh 
    on hp.id = sh.property_id 
    INNER JOIN habi_db.status ss
    ON ss.id = sh.status_id
    WHERE ss.id IN (3, 4, 5) AND
    sh.update_date = (
    SELECT MAX(update_date) 
    FROM habi_db.status_history ssh
    WHERE ssh.property_id = sh.property_id  
    ) AND hp.address <> '' AND hp.city <> '' 
    '''
    (query, params) = query_builder(sql, fyear, fcity, fstatus)

    cursor.execute(query, params)

    inmuebles_list = []
    for (
        address,
        city,
        price,
        description,
        status,
        id_status,
        label_status,
    ) in cursor:
        item = Inmuebles(
            address,
            city,
            price,
            description,
            status,
            id_status,
            label_status,
            )
        inmuebles_list.append(item.to_json())

    cursor.close()
    return inmuebles_list


def get_status(db):
    """
    Listado de status.

    Parameters
    ----------
    db : mysql, optional
        conexión de la base de datos

    Returns
    -------
    list
        [status], listado de status 
    """

    cursor = db.cursor()

    query = '''
    SELECT  
    ss.name,
    ss.id,
    ss.label
    FROM habi_db.status ss
    WHERE ss.id IN (3, 4, 5)
    '''

    cursor.execute(query)

    status_list = []
    for (name, id, label) in cursor:
        item = Status(name, id, label)
        status_list.append(item.to_json())

    cursor.close()
    return status_list
