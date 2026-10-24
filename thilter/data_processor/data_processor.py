from csv import reader as csv_reader
from os import scandir, rename as rename_file
from json import dumps as json_dumps
from thilter.interfaces import URLKeyInterface


class DataProcessor:
    data_folder = 'data'

    def __init__(self, watches_file='watches.csv', specs_folder='specs', image_folder='watches_images'):
        self.watches_file = f'{self.data_folder}/{watches_file}'
        self.specs_folder = f'{self.data_folder}/{specs_folder}'
        self.specs_files = self.get_specs_files_list()
        self.output_file = f'{self.data_folder}/data.json'
        self.images_folder = f'{self.data_folder}/{image_folder}'
        self.data = {}

    @property
    def fields(self):
        return [
            'brand', 'model_name', 'name', 'device_type', 'gender', 'price', 'currency', 'category', 'hardware',
            'material', 'diameter', 'thickness', 'colour', 'analogous_colours', 'dial_colour', 'strap_type',
            'strap_material', 'strap_colour', 'crystal_material', 'stone_set', 'case_shape', 'water_resistance', 'time',
            'calendar', 'timers', 'notifications', 'fitness_tracker', 'memory', 'outdoor', 'lighting', 'movement_type',
            'movement_origin', 'style', 'display', 'connectivity', 'markers', 'sports', 'delivery', 'warranty',
            'image_source', 'source_link', 'extra_fields'
        ]

    def get_specs_files_list(self):
        files = set()
        with scandir(self.specs_folder) as entries:
            for entry in entries:
                if entry.is_file() and entry.name.endswith('.csv'):
                    files.add(entry.name)
        return list(files)

    def extract_unique_fields(self):
        fields = set()

        for file_name in self.specs_files:
            with open(f'{self.specs_folder}/{file_name}', 'r') as csv_file:
                reader = csv_reader(csv_file)
                next(reader)

                for line in reader:
                    if line[0].startswith('http'):
                        continue
                    fields.add(line[0])

        fields = list(fields)
        fields.sort()
        self.data.update({
            'unique_fields': fields,
            'unique_fields_count': len(fields)
        })
        return self.data['unique_fields']

    def process_data(self):
        print('Starting data processing..')
        self.extract_unique_fields()
        self.__process_data()
        self.output_json()
        print('Data Processed.')

    def __process_data(self):
        watches = []

        with open(self.watches_file, 'r') as watches_file:
            reader = csv_reader(watches_file)
            next(reader)

            for line in reader:
                file_name = f'{line[0].upper()}'

                data = {
                    'name': line[0],
                    'price': line[1].strip('Â£').strip('£'),
                    'delivery': line[2],
                    'source_link': line[3],
                    'currency': 'GBP',
                    'image_source': '/static/watches/' + file_name + '.jpeg'
                }

                file_name += '.csv'
                if file_name in self.specs_files:
                    data.update(self.__extract_watch_data(file_name))
                watches.append(data)

        self.data.update({
            'watches': watches,
            'watches_count': len(watches)
        })

    def __extract_watch_data(self, file_name):
        data = {}
        extra_fields = {}

        with open(f'{self.specs_folder}/{file_name}', 'r') as watch_file:
            reader = csv_reader(watch_file)
            next(reader)

            for line in reader:
                key = line[0].lower().replace(' ', '_')
                value = line[1]

                if key.startswith('http'):
                    continue

                if key == 'analogue/digital':
                    key = 'device_type'
                elif key == 'gender':
                    value = self.map_gender(value)
                elif key == 'movement':
                    key = 'movement_type'
                elif key == 'extra_fields':
                    extra_fields.update({
                        key: value
                    })

                if key in self.fields:
                    data.update({
                        key: value
                    })
                else:
                    extra_fields.update({
                        key: value
                    })

        data.update({
            'extra_fields': extra_fields
        })
        return data

    @classmethod
    def map_gender(cls, value):
        genders = {
            'Gents': 'male',
            'Ladies': 'female',
            'Unisex': 'unisex'
        }
        return genders[value]

    def rename_images(self):
        with scandir(self.images_folder) as entries:
            for entry in entries:
                if entry.is_file() and entry.name.endswith('.jpeg'):
                    filename = entry.name.strip('.jpeg')
                    filename = URLKeyInterface.generate_url_key(filename, validate_unique=False)
                    try:
                        rename_file(f'{self.images_folder}/{entry.name}', f'{self.images_folder}/{filename}.jpeg')
                    except FileExistsError as e:
                        print(e)

    def output_json(self):
        with open(self.output_file, 'w') as output_file:
            output_file.write(json_dumps(self.data, sort_keys=True, indent=2))


if __name__ == '__main__':
    processor = DataProcessor()
    processor.rename_images()
