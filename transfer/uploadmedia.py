import requests


URL = 'https://kc.kobotoolbox.org/api/v1/metadata.json'
TOKEN = '16a1eee1a0e9a6fa18c084e7e0447175d16f0620'
FILE_PATH = '/Users/dyaqub/git/kobo-transfer/attachments/testmedia'
FILENAME = 'income.jpg'
MIME = 'text/csv'
XFORM = 'a8ztSSBCpCUa4Sk5m59uuQ'

headers = {'Authorization': f'Token {TOKEN}'}
files = {'data_file': (FILENAME, open(f'{FILE_PATH}{FILENAME}', 'rb').read(), MIME)}
data = {
    'data_value': FILENAME,
    'xform': XFORM,
    'data_type': 'media',
    'data_file_type': MIME,
}
response = requests.post(URL, data=data, files=files, headers=headers)