from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
import ml_model
from ml_model import rec_dig
app = Flask(__name__)
app.secret_key = "hello"
app.config['UPLOAD_FOLDER'] = 'static/files'
class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/', methods=['GET',"POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
        print(file.filename)
        image_path = os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            'static',
            'files',
            secure_filename(file.filename)
        )
        result = (ml_model.rec_dig(image_path)).tolist()[0]

        print("result: ", result)
        return render_template('reveal.html', result=result, image_path=file.filename, form=form)
    
    return render_template('home.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)