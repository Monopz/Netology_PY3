import requests
import sys

api_key = 'trnsl.1.1.20170403T105419Z.41a2ec13de050095.e6c03e87c393ffc1b2c0c25bfbfc876cf399b831'
url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate(text_path, result_path, from_lang, to_lang='ru'):
    with open(text_path, 'r') as text_file, open(result_path, 'w') as result:
        text = text_file.read()
        params = {
                'key': api_key,
            'text': text,
            'lang': '{}-{}' .format(from_lang, to_lang)
        }

        response = requests.post(url, params=params)
        json = response.json()
        result_text = ''.join(json['text'])

        result.write(result_text)

    print('DONE')
    return True


if __name__ == '__main__':
    text_path_input = input('Введите путь к файлу, который хотите перевести: \n')

    from_lang_input = input('С какого языка Вы хотите перевести? \n')

    result_path_input = input('Введите путь для файла с переведенным текстом: \n')

    translate(text_path_input, result_path_input, from_lang_input)

    print('Файл успешно переведен')
