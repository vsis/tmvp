from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
from img import proc_image

app = Flask(__name__)

UPLOAD_FOLDER = '/tmp/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

@app.route("/", methods=['GET'])
def index():
    return jsonify({'message': 'hello world! This is my Tesseract MVP'})


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
        filename = UPLOAD_FOLDER + filename
        lang = request.args.get('lang') or 'spa'
        if allowed(filename):
            file.save(filename)
            str_data = proc_image(filename, lang)
            returned_data = {'message': 'File OK', 'data': str_data, 'lang': lang}
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

