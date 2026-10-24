from settings import settings
import boto3


class AWSPolly:

    __instance = None

    def __init__(self):
        if AWSPolly.__instance is not None:
            raise Exception("Illegal Usage. Please use the get_instance to obtain an instance.")

        self.__client = boto3.client(
            'polly',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_REGION
        )

    @classmethod
    def get_instance(cls):
        """
        Get AWSPolly instance through this class method.

        :return: AWSPolly instance.
        """
        if AWSPolly.__instance is None:
            AWSPolly.__instance = AWSPolly()
        return AWSPolly.__instance

    def get_client(self):
        """
        :return: AWSPolly client.
        """
        return self.__client

    def synthesize(self, text):
        """
        Synthesize text.

        :param text: string
        :return: API response
        """
        return self.__client.synthesize_speech(
            Text=text,
            OutputFormat=settings.AWS_OUTPUT_FORMAT,
            VoiceId=settings.AWS_VOICE_ID
        )


class DigitalOcean:

    __instance = None

    def __init__(self):
        if DigitalOcean.__instance is not None:
            raise Exception("Illegal Usage. Please use the get_instance to obtain an instance.")

        self.__client = boto3.client(
            's3',
            endpoint_url=settings.SPACES_ENDPOINT_URL,
            aws_access_key_id=settings.SPACES_KEY,
            aws_secret_access_key=settings.SPACES_SECRET,
            region_name=settings.SPACES_REGION
        )

    @classmethod
    def get_instance(cls):
        """
        Get DigitalOcean instance through this class method.

        :return: DigitalOcean instance.
        """
        if DigitalOcean.__instance is None:
            DigitalOcean.__instance = DigitalOcean()
        return DigitalOcean.__instance

    def get_client(self):
        """
        :return: DigitalOcean client.
        """
        return self.__client

    def save_file(self, file_source, key):
        """
        Save new file into storage.

        :param file_source: link to file.
        :param key: file unique key.
        :return: API response.
        """
        with open(file_source, 'rb') as source_file:
            file_content = source_file.read()
            return self.__client.put_object(
                Bucket=settings.SPACES_STORAGE_NAME,
                Key=key,
                Body=file_content,
                ACL=settings.SPACES_ACL
            )

    def delete_file(self, file_key):
        """
        Delete file from storage.

        :param file_key: unique file key.
        :return: API response.
        """
        return self.__client.delete_object(
            Bucket=settings.SPACES_STORAGE_NAME,
            Key=file_key
        )

    def add_media_space(self):
        """
        Create Storage space.

        :return: API response.
        """
        return self.__client.create_bucket(Bucket=settings.SPACES_STORAGE_NAME)

    def drop_media_space(self):
        """
        Delete Storage space.

        :return: API response.
        """
        return self.__client.delete_bucket(Bucket=settings.SPACES_STORAGE_NAME)
