"""
Authors: TANZIM AHMED and NAYEMUL ISLAM MAJUMDER
Author Emails: tanzim.din@northsouth.edu and nayemul.majumder@northsouth.edu
Created on: 17th July 2020
For: readmearticles.com
"""


from .exceptions import ArticleTooSmallException
from settings.settings import BASE_DIR, TEMP_DIR, MIN_ARTICLE_LENGTH
from bs4 import BeautifulSoup
from readability import Document
from re import compile as re_compile
import os


class TextProcessor:

    partition_length = 2750

    def __init__(self, text):
        self.text = text
        self.cleaned_text = None
        self.text_partitions = None
        self.title = None

    def get_text_partitions(self):
        """
        Partition Text into AWS per request allowed characters.

        :raises: ArticleTooSmall Exception.
        :return: list of text partitions.
        """

        self.extract_article()
        self.text_partitions = []
        text_length = len(self.cleaned_text)

        if text_length < MIN_ARTICLE_LENGTH:
            raise ArticleTooSmallException

        if text_length <= self.partition_length:
            self.text_partitions.append(self.cleaned_text)
            return self.text_partitions

        start_index = 0
        end_index = start_index + self.partition_length
        while end_index <= text_length:
            if end_index < text_length:
                while self.cleaned_text[end_index] != ' ':
                    end_index -= 1
                text_partition = self.cleaned_text[start_index:end_index]
            else:
                text_partition = self.cleaned_text[start_index:]

            start_index = end_index
            end_index = start_index + self.partition_length
            self.text_partitions.append(text_partition)

        # Compensating for the remaining index
        if start_index < text_length:
            self.text_partitions.append(self.cleaned_text[start_index:])

        return self.text_partitions

    def extract_article(self):
        """
        Extract cleaned readable text from HTML.

        :return: plain text.
        """
        cleaned_html = Document(self.text)
        self.title = cleaned_html.title()
        cleaned_html = cleaned_html.title() + '. ' + cleaned_html.summary()

        cleaned_text = BeautifulSoup(cleaned_html, 'html.parser').get_text()
        self.cleaned_text = re_compile(r'([.?])([A-Z])').sub(r'. \2', cleaned_text)

        return self.cleaned_text

    def test_html_output(self):
        """
        Call this function to map the cleaned html file before partitioning.
        The file is stored in the temp directory.
        """
        with open(os.path.join(BASE_DIR, TEMP_DIR, 'sample_article.html'), 'w', encoding='utf-8') as sample_text:
            sample_text.write(self.cleaned_text)
