from datetime import datetime
from flask import Blueprint, jsonify


time_bp = Blueprint('time_routes', __name__, url_prefix='/api/v1')

@time_bp.route('/dt', methods=['GET'])
def current_time():
    dt = datetime.now()

    formatted_dt = dt.strftime("%Y-%m-%d %H:%M:%S")
    
    return jsonify({"current_date_time": formatted_dt})
