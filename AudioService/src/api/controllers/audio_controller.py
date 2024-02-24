from flask import Flask, request,jsonify
from src.api.models.audio import Audio, db
from src.api.schemas.audio_schema import AudioSchema
from flask_cors import CORS

app = Flask(__name__ )
CORS(app)
URI = "/api/v1.0/audios"

audio_schema = AudioSchema()


class AudioController:

    @staticmethod
    @app.route(URI, methods=['GET'])
    def get_audios():
        try:
            all_audios = Audio.query.all()
            print(all_audios)  # Check the console/logs for debugging

            if not all_audios:
                return jsonify({"message": "No audio records found"}), 404

            return audio_schema.dump(all_audios, many=True)
        except Exception as e:
            print(f"Error: {str(e)}")
            return jsonify({"message": "Internal Server Error"}), 500

    @staticmethod
    @app.route(URI+"/<int:id>", methods=["GET"])
    def get_audio(id):
        try:
            single_audio = Audio.query.get(id)
            if not single_audio:
                return jsonify({"message": "No audio records found"}), 404

            return audio_schema.dump(single_audio)

        except Exception as e:
            return jsonify({"message": "Internal Server Error"}), 500

    @staticmethod
    @app.route(URI, methods=['POST'])
    def post_audio():
        data = request.get_json()
        new_audio = Audio(
            name=data['name'],
            bpm=data['bpm'],
            file_path="testfilepath",
            length=10000
        )
        db.session.add(new_audio)
        db.session.commit()
        return audio_schema.dump(new_audio)

    @staticmethod
    @app.route(URI+"/<int:id>", methods=['PUT'])
    def put_audio(id):
        try:
            single_audio = Audio.query.get(id)

            if not single_audio:
                return jsonify({"message": "Audio not found"}), 404

            data = request.get_json()

            single_audio.name = data['name']
            single_audio.bpm = data['bpm']
            single_audio.file_path = 'testfile_path'
            single_audio.length = 10000


            # Update other fields as needed

            db.session.commit()

            return audio_schema.dump(single_audio)

        except Exception as e:
            return jsonify({"message": "Internal Server Error"}), 500

    @staticmethod
    @app.route(URI+"/<int:id>",methods=['DELETE'])
    def delete_audio(id):
        try:
            audio_to_delete = Audio.query.get(id)

            if not audio_to_delete:
                return jsonify({"message": "Audio not found"}), 404

            db.session.delete(audio_to_delete)
            db.session.commit()

            return jsonify({"message": "Audio deleted successfully"})
        except Exception as e:
            return jsonify({"message": "Internal Server Error"}), 500
