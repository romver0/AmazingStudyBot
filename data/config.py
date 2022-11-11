import os

from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
BIG_ADMINS = env.list("BIG_ADMINS")
IP = env.str("ip")

DB_USER = str(os.getenv("DB_USER"))
DB_PASS = str(os.getenv("DB_PASS"))
DB_NAME = str(os.getenv("DB_NAME"))
DB_HOST = str(os.getenv("DB_HOST"))
print(DB_USER)

aiogram_redis = {
    'host': IP
}
# redis = {
#     'address': (IP, 5432),
#     'encoding': 'utf8'
# }

# POSTGRES_URI = f"posqresql://{DB_USER}:{DB_PASS}@{IP}/{DB_NAME}"

# переписить для инлайн-кнопок
section_of_mathematics = [
    {'topic': 'Всё о фракталах'},
    {'topic': 'Инф-ые технологии поддержки принятия решений'},
    {'topic': 'Задача о Хайнойской башне'},
    {'topic': 'Математические игры'},
    {'topic': 'Алгоритм Флёри'},
    {'topic': 'Неразгаданные шифры'},
    {'topic': 'Кардинальные числа'},
    {'topic': 'Анализ непрерывных потоков платежей'},
    {'topic': 'Влияние музыки на псих-ий фон обу-ся при изучении математики'},
    {'topic': 'Счётные и несчётные мн-ва'},
    {'topic': 'Проблема Коллатца'},
]
