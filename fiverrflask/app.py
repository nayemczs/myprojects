from flask import Flask, render_template, request, redirect, abort, flash
from database.models import db as database, User, Role, Audio
from database.forms import URLForm, DeleteAudioForm
from flask_wtf.csrf import CSRFProtect
from flask_security import Security, SQLAlchemyUserDatastore, login_required
from flask_login import current_user
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from core.audio_manager import AudioManager
from settings import settings
import json


app = Flask(__name__)

for key, value in settings.APP_CONFIGS.items():
    app.config[key] = value

CSRFProtect(app)
database.init_app(app)
user_data_store = SQLAlchemyUserDatastore(database, User, Role)
security = Security(app, user_data_store)
mail = Mail(app)
Bootstrap(app)


@app.route("/")
def index():
    # database.create_all()
    return render_template('index.html')


@app.route("/home/", methods=['GET', 'POST'])
@login_required
def home():
    listened_audios = current_user.audios.filter_by(is_listened=True).order_by(Audio.date_added).all()
    remaining_audios = current_user.audios.filter_by(is_listened=False).order_by(Audio.date_added).all()
    recent_audio = None
    errors = None
    form = URLForm()
    delete_form = DeleteAudioForm()

    if form.validate_on_submit():
        audio_manager = AudioManager(url=form.url.data)
        if audio_manager.generate_and_save_audio():
            recent_audio = audio_manager.audio
            flash(u'Audio Generated.', category='success')
        else:
            errors = audio_manager.error_list
            flash(errors, category='error')

    return render_template(
        'home.html',
        listened_audios=listened_audios,
        remaining_audios=remaining_audios,
        form=form,
        delete_form=delete_form,
        recent_audio=recent_audio,
        errors=errors
    )


@app.route('/store/audio_position/', methods=['POST'])
@login_required
def store_audio_position():
    if not current_user.is_authenticated:
        return 'Unauthorized request.', 403

    if 'data' in request.form:
        data = request.form['data']
        data = json.loads(data)

        AudioManager(audio_id=data['player_id']).update_current_position(
            data['current_position']
        )
        return 'Playback position recorded.', 200
    else:
        return 'Bad request.', 400


@app.route('/listened/audio/', methods=['POST'])
@login_required
def mark_listened():
    if not current_user.is_authenticated:
        return 'Unauthorized request.', 403

    if 'data' in request.form:
        data = request.form['data']
        data = json.loads(data)

        AudioManager(audio_id=data['player_id']).mark_and_update_current_position(
            data['current_position']
        )
        return 'Audio marked.', 200
    else:
        return 'Bad request.', 400


@app.route('/delete/audio/', methods=['POST'])
@login_required
def delete_audio():
    if not current_user.is_authenticated:
        abort(403, description='Unauthorized request.')
        return 'Unauthorized request.', 403

    form = DeleteAudioForm()

    if form.validate_on_submit():
        audio_manager = AudioManager(audio_id=form.player_id.data)
        if audio_manager.delete_audio():
            flash(u'Audio Deleted.', category='success')
            return redirect('/home/')
        else:
            abort(400, description='Bad request.')
            return audio_manager.error_list, 400

    # if 'data' in request.form:
    #     data = request.form['data']
    #     data = json.loads(data)
    #
    #     audio_manager = AudioManager()
    #     if audio_manager.delete_audio(data['player_id']):
    #         return redirect('/home/')
    #     else:
    #         abort(400, description='Bad request.')
    #         return audio_manager.error_list, 400
    else:
        abort(400, description='Bad request.')
        return 'Bad request.', 400


@app.route("/about/")
@login_required
def about():
    return render_template('about.html', title='About')


@app.route('/test/')
@login_required
def test():
    url = 'https://www.sciencealert.com/physicists-think-they-ve-figured-out-a-way-to-save-schroedinger-s-cat'
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
