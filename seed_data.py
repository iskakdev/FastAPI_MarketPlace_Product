import requests

AUTH_URL = 'http://127.0.0.1:8000/auth/login/'
PRODUCT_URL = 'http://127.0.0.1:8001'

USERNAME = 'testuser'
PASSWORD = '12345678'


def get_token():
    response = requests.post(AUTH_URL, json={'username': USERNAME, 'password': PASSWORD})
    response.raise_for_status()
    return response.json()['access_token']


def print_result(name, response):
    try:
        print(name, '->', response.status_code, response.json())
    except requests.exceptions.JSONDecodeError:
        print(name, '->', response.status_code, 'RAW:', response.text)


def create_categories(token):
    headers = {'Authorization': f'Bearer {token}'}
    categories = [
        {'category_name': 'Смартфоны', 'category_image': 'https://example.com/images/smartphones.jpg'},
        {'category_name': 'Ноутбуки', 'category_image': 'https://example.com/images/laptops.jpg'},
        {'category_name': 'Наушники', 'category_image': 'https://example.com/images/headphones.jpg'},
        {'category_name': 'Умные часы', 'category_image': 'https://example.com/images/smartwatches.jpg'},
        {'category_name': 'Бытовая техника', 'category_image': 'https://example.com/images/appliances.jpg'},
    ]
    for category in categories:
        response = requests.post(f'{PRODUCT_URL}/categories/', json=category, headers=headers)
        print_result(category['category_name'], response)


def create_products(token):
    headers = {'Authorization': f'Bearer {token}'}
    products = [
        {'product_name': 'iPhone 15 Pro', 'price': 999, 'article_number': 100001,
         'description': 'Флагманский смартфон Apple с чипом A17 Pro и титановым корпусом',
         'is_official': True, 'video': 'https://example.com/videos/iphone15pro.mp4', 'category_id': 1},
        {'product_name': 'Samsung Galaxy S24 Ultra', 'price': 1199, 'article_number': 100002,
         'description': 'Смартфон с S Pen, дисплеем 6.8 дюйма и камерой 200 Мп',
         'is_official': True, 'video': 'https://example.com/videos/galaxys24ultra.mp4', 'category_id': 1},
        {'product_name': 'MacBook Air M3', 'price': 1099, 'article_number': 100003,
         'description': 'Ультратонкий ноутбук Apple с чипом M3 и временем работы до 18 часов',
         'is_official': True, 'video': 'https://example.com/videos/macbookairm3.mp4', 'category_id': 2},
        {'product_name': 'Dell XPS 13', 'price': 999, 'article_number': 100004,
         'description': 'Компактный премиальный ноутбук с экраном InfinityEdge',
         'is_official': True, 'video': 'https://example.com/videos/dellxps13.mp4', 'category_id': 2},
        {'product_name': 'Sony WH-1000XM5', 'price': 349, 'article_number': 100005,
         'description': 'Беспроводные наушники с лучшим в классе шумоподавлением',
         'is_official': True, 'video': 'https://example.com/videos/sonywh1000xm5.mp4', 'category_id': 3},
        {'product_name': 'AirPods Pro 2', 'price': 249, 'article_number': 100006,
         'description': 'Беспроводные наушники Apple с активным шумоподавлением',
         'is_official': True, 'video': 'https://example.com/videos/airpodspro2.mp4', 'category_id': 3},
        {'product_name': 'Apple Watch Series 9', 'price': 399, 'article_number': 100007,
         'description': 'Умные часы с датчиком кислорода в крови и всегда включённым дисплеем',
         'is_official': True, 'video': 'https://example.com/videos/applewatch9.mp4', 'category_id': 4},
        {'product_name': 'Samsung Galaxy Watch 6', 'price': 329, 'article_number': 100008,
         'description': 'Умные часы с отслеживанием сна и тренировок',
         'is_official': True, 'video': 'https://example.com/videos/galaxywatch6.mp4', 'category_id': 4},
        {'product_name': 'Dyson V15 Detect', 'price': 749, 'article_number': 100009,
         'description': 'Беспроводной пылесос с лазерной подсветкой пыли',
         'is_official': True, 'video': 'https://example.com/videos/dysonv15.mp4', 'category_id': 5},
        {'product_name': 'Philips Hue Starter Kit', 'price': 199, 'article_number': 100010,
         'description': 'Комплект умного освещения с управлением через приложение',
         'is_official': True, 'video': 'https://example.com/videos/philipshue.mp4', 'category_id': 5},
    ]
    for product in products:
        response = requests.post(f'{PRODUCT_URL}/products/', json=product, headers=headers)
        print_result(product['product_name'], response)


if __name__ == '__main__':
    token = get_token()
    print('Токен получен')
    create_categories(token)  # раскомментировано, чтобы досоздать недостающие категории
    create_products(token)
    print('Готово!')