"""
Authors: TANZIM AHMED and NAYEMUL ISLAM MAJUMDER
Author Emails: tanzim.din@northsouth.edu and nayemul.majumder@northsouth.edu
Created on: 17th July 2020
For: readmearticles.com
"""


from flask import abort
from flask_login import current_user
from database.models import Audio
from database.connections import DigitalOcean
from .synthesizer import SpeechSynthesizer
from .exceptions import ArticleTooSmallException
from settings.settings import AWS_OUTPUT_FORMAT, TOKEN_LENGTH, TEST_RUN_WITHOUT_AWS
from botocore.exceptions import BotoCoreError, ClientError
from secrets import token_hex
from os import remove as remove_temp_file


class AudioManager:

    def __init__(self, url=None, audio_id=None):
        self.url = url
        self.user = current_user
        self.audio = None
        self.error_list = []

        if audio_id is not None:
            self.audio = self.user.get_audio(audio_id)

    def generate_and_save_audio(self):
        if not self.user.is_authenticated:
            abort(403)

        file_name = token_hex(TOKEN_LENGTH) + '.' + AWS_OUTPUT_FORMAT

        speech_synthesizer = SpeechSynthesizer(self.url, file_name)
        try:
            audio_file_path = speech_synthesizer.synthesize()
        except ArticleTooSmallException as error:
            self.error_list.append(error.message)
            return False
        except (BotoCoreError, ClientError):
            self.error_list.append('Error in Speech construction.')
            return False
        except IOError:
            self.error_list.append('Internal Server Error.')
            return False

        self.audio = Audio()
        self.audio.title = speech_synthesizer.article_title()
        self.audio.set_file_name(file_name)

        if not TEST_RUN_WITHOUT_AWS:
            response = DigitalOcean.get_instance().save_file(audio_file_path, file_name)
            if response['ResponseMetadata']['HTTPStatusCode'] != 200:
                self.error_list.append('Digital Ocean error.')
                return False
            remove_temp_file(audio_file_path)

        self.user.audios.append(self.audio)
        self.user.save()

        return True

    def update_current_position(self, current_position):
        self.audio.cursor_position = current_position
        self.audio.save()

    def mark_and_update_current_position(self, current_position):
        self.audio.cursor_position = current_position
        self.audio.is_listened = True
        self.audio.save()

    def mark_listened(self):
        self.audio.is_listened = True
        self.audio.save()

    def delete_audio(self):
        if not TEST_RUN_WITHOUT_AWS:
            response = DigitalOcean.get_instance().delete_file(self.audio.file_name)
            if response['ResponseMetadata']['HTTPStatusCode'] != 204:
                self.error_list.append('Digital Ocean error.')
                return False

        self.audio.delete()
        return True

    @classmethod
    def generate_dummy_audio_objects(cls, start=1, end=11):
        audios = []
        for i in range(start, end):
            audios.append(Audio(
                title=f'Audio_{i}',
                file_name=f'Audio_{i}',
                link=f'/static/demo_{i}.mp3'
            ))
        return audios

    @classmethod
    def mark_dummy_listened(cls, user, start=5, end=11):
        for i in range(start, end):
            audio = user.get_audio(i)
            audio.is_listened = True
            audio.save()
