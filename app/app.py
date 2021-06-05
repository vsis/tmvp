from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = '/tmp/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

@app.route("/", methods=['GET'])
def index():
    return jsonify({message: 'hello world! This is my Tesseract MVP'})


@app.route("/img", methods=['POST'])
def img():

    # Check if filename has an allowed extension
    def allowed(filename):
        try:
            return filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS
        # This exception will happen if filename has no dot
        except IndexError:
            return False

    returned_data = {'message': ''}
    status = 200
    try:
        file = request.files['file']
        filename = secure_filename(file.filename)
        if allowed(filename):
            file.save(UPLOAD_FOLDER + filename)
            returned_data = {'message': 'File OK'}
        else:
            returned_data = {'message': 'File not allowed. Use one of these extensions: ' + str(ALLOWED_EXTENSIONS)}
            status = 400
    except KeyError:
        returned_data = {'message': "No file was given."}
        status = 400
    except Exception as error:
        returned_data = {'message': 'There was a server error =(', 'error': str(error)}
        status = 500
    return jsonify(returned_data), status

