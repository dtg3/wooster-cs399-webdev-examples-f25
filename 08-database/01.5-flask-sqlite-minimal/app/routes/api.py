from flask import Blueprint, jsonify, request
from ..models.database import get_tasks, insert_task, delete_task, update_task

# Create the Blueprint, setting the base URL for these routes
api_bp = Blueprint('api_bp', __name__, url_prefix='/api/v1/tasks')

@api_bp.route('/', methods=['GET', 'POST'])
@api_bp.route('/<int:task_id>', methods=['GET', 'PATCH', 'DELETE'])
def list_tasks(task_id=None):

    print(task_id)
    if request.method == 'GET':

        try:
            tasks_list = get_tasks(task_id)
            return jsonify(tasks_list)
            
        except Exception as e:
            return jsonify({'error': 'Could not query database', 'details': str(e)}), 500


    elif request.method == 'POST':
        try:
            json_data = request.get_json()
            if not json_data:
                return jsonify({'error': 'NO/INVALID JSON DATA'}), 400
            new_task_id = insert_task(json_data.get('description'))
            return jsonify({'success': f'Task {new_task_id} added!'})
        except Exception as e:
            return jsonify({'error': 'Could not query database', 'details': str(e)}), 500

    
    if not task_id:
        return jsonify({'error': 'No task id supplied'}), 400

    if request.method == 'DELETE':
        try:
            delete_task(task_id)
            return jsonify({'success': f'Task {task_id} deleted'})
        except Exception as e:
            return jsonify({'error': 'Could not query database', 'details': str(e)}), 500
            
        
    elif request.method == 'PATCH':
        try:
            json_data = request.get_json()
            if not json_data:
                return jsonify({'error': 'NO/INVALID JSON DATA'}), 400
            
            updated_row_count = update_task(task_id, 
                                           json_data.get('description', None),
                                           json_data.get('completed', None))
            return jsonify({'success': f'Updated {updated_row_count} row(s)!'})

        except Exception as e:
            return jsonify({'error': 'Could not query database', 'details': str(e)}), 500
    