from flask import jsonify, request, Blueprint
from flask_cors import CORS
import os



file_bp = Blueprint('files', __name__)
CORS(file_bp)
URI = "/api/v1.0/upload"
class FileController():
    @staticmethod
    @file_bp.route(URI, methods=['POST'])    
    def upload_file():
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})

        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No selected file'})

        if file:
            filename = os.path.join("filesystem", file.filename)
            file.save(filename)
            return jsonify({'success': 'File uploaded successfully'})