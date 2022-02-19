from flask import Blueprint, current_app, jsonify, request

from inmuebles.inmuebles import get_inmuebles_by_filter, get_status

inmuebles_bp = Blueprint(
    'inmuebles_bp',
    __name__
)

CONN = current_app.config["CONN"]


@inmuebles_bp.route('/api/v1/inmuebles')
def inmuebles():
    year = None if request.args.get(
        'year') is None else int(request.args.get('year'))
    city = request.args.get('city')
    status = None if request.args.get(
        'status') is None else int(request.args.get('status'))
    model = get_inmuebles_by_filter(
        db=CONN, fyear=year, fcity=city, fstatus=status)
    return jsonify(model)


@inmuebles_bp.route('/api/v1/status')
def status():
    model = get_status(db=CONN)
    return jsonify(model)
