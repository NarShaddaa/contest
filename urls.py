import random
import string


class MarsURLEncoder:
    def __init__(self):
        self.url_map = {}  # Хранилище: ключ - хеш значение - исходная ссылка
        self.base_url = "https://ma.rs/"
        self.hash_length = 7
        self.characters = string.ascii_letters + \
            string.digits  # Все возможные символы для хеша

    def _generate_hash(self):
        """Генерирует уникальный хеш."""
        while True:
            hash_code = ''.join(random.choices(
                self.characters, k=self.hash_length))
            if hash_code not in self.url_map:
                return hash_code

    def encode(self, long_url):
        """Шифрует ссылку и возвращает короткую ссылку."""
        hash_code = self._generate_hash()
        self.url_map[hash_code] = long_url
        return self.base_url + hash_code

    def decode(self, short_url):
        """Расшифровывает короткую ссылку и возвращает оригинальную."""
        hash_code = short_url.replace(self.base_url, '')
        return self.url_map.get(hash_code, None)
