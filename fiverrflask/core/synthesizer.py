import requests
from contextlib import closing
from database.connections import AWSPolly
from .text_processor import TextProcessor
from settings.settings import BASE_DIR, TEMP_DIR, TEST_RUN_WITHOUT_AWS
import os


class SpeechSynthesizer:

    def __init__(self, url, file_name):
        self.url = url
        self.file_name = file_name
        self.temp_dir = os.path.join(BASE_DIR, TEMP_DIR)
        self.text_processor = None

        if not os.path.exists(self.temp_dir):
            os.mkdir(self.temp_dir)

    def synthesize(self):
        """
        Makes repeated AWS call with the text partitions and stitches together the audio file.
        The audio stream is written to temporary folder.

        :return: path to temporary audio file.
        """

        response_streams = []
        audio_file_path = os.path.join(self.temp_dir, self.file_name)
        response = requests.get(self.url)

        self.text_processor = TextProcessor(response.text)
        text_partitions = self.text_processor.get_text_partitions()

        if not TEST_RUN_WITHOUT_AWS:
            for text in text_partitions:
                response = AWSPolly.get_instance().synthesize(text)
                response_streams.append(response['AudioStream'])

            with open(audio_file_path, 'wb') as demo_sound:
                for response_stream in response_streams:
                    with closing(response_stream) as stream:
                        demo_sound.write(stream.read())

        return audio_file_path

    def article_title(self):
        return self.text_processor.title

    def test_html_output(self, text_partitions):
        """
        Call this function to map the text output after extraction from source HTML.
        The file is stored in the temp directory.

        :param text_partitions: list of text partitions.
        """
        with open(
                os.path.join(self.temp_dir, 'partitioned_article.html'),
                'w',
                encoding='utf-8'
        ) as sample_text:
            for text in text_partitions:
                sample_text.write(text)
                sample_text.write('<br><br>')
