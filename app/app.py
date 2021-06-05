from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

@app.route("/", methods=['GET'])
def index():
    return jsonify({message: 'hello world! This is my Tesseract MVP'})


@app.route("/img", methods=['POST'])
def img():
    def allowed(filename):
        try:
            return filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS
        except IndexError:
            return false
    returned_data = {'message': ''}
    status = 200
    try:
        file = request.files['file']
        filename = secure_filename(file.filename)
        if allowed(filename):
            file.save(filename)
            returned_data = {'message': 'file ok'}
        else:
            returned_data = {'message': 'file not allowed'}
            status = 400
    except KeyError:
        returned_data = {'message': "didn't you give a file?"}
        status = 400
    except Exception as error:
        returned_data = {'message': 'I have no idea what happened', 'error': str(error)}
        status = 500
    return jsonify(returned_data), status

