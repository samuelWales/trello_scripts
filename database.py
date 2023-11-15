import random
import string  # импортирую для генерации пароля
import json


def generate_password():
    characters = string.ascii_letters + string.digits + '!"#$%&()*+,-./:;<=>?@[\]^_{|}~'
    password = ''.join(random.choice(characters) for _ in range(random.randint(1, 60)))
    
    return password

def generate_login():
    login = random.choice(LOGIN_LIST)
    
    return login

def generate_mail():
    characters = string.ascii_letters + string.digits + '.'
    mail_name = ''.join(random.choice(characters) for _ in range(random.randint(1, 45)))
    mail_server = random.choice(MAIL_SERVER_LIST)
    mail = mail_name + '@' + mail_server
    
    return mail

def generate_personality():
    personality = random.choice(PERSONALITY_LIST)
    
    return personality
    
    
    
LOGIN_LIST = [
    "Starlight12345",
    "GreenTechMaster",
    "SilverDragon789",
    "OceanExplorer22",
    "CrimsonTiger007",
    "GoldenEagle2023",
    "RubyRainbow12345",
    "BlueberryPancake",
    "GalacticGadgeteer",
    "FireflyWhisperer",
    "JadeJourneyer123",
    "EmeraldEnigma17",
    "FrostyMountain11",
    "NeonNebulaExplorer"
    "SolarSystemSailor",
    "MidnightRider2023",
    "AuroraBorealis99",
    "PixelPioneer2023",
    "SunriseSurfer456",
    "DeepSpaceDiver111",
    "CosmicAdventurer",
    "WildernessWalker",
    "SapphireSeeker22",
    "ThunderTech007",
    "DreamyGalaxy123",
    "LunarLandscape22",
    "TechSavvyTraveler",
    "StarryNightSky88",
    "RainbowDreamer123",
    "AstralVoyager2023"
]
    
MAIL_SERVER_LIST = [
    "gmail.com", "yandex.ru", "outlook.com", "mail.ru"
]

PERSONALITY_LIST = [
    "Я человек с творческим уклоном, постоянно стремлюсь к саморазвитию и новым знаниям.",
    "Я — человек с бесконечным стремлением к изучению и расширению горизонтов.",
    "Я — творческий человек с горячим сердцем и стремлением к постоянному развитию.",
    "Я - человек, ценящий исследование и креативный подход ко всему, что делаю.",
    "С непреодолимым любопытством и страстью к обучению я стремлюсь к постоянному росту."
]

WORKPLACE_NAME_LIST = [
    "Оптимизация Работы",
    "Эффективная Команда",
    "Задачи Прогресса",
    "Коллективная Гармония",
    "Творческий Офис",
    "Процессы В Действии"
]

WORKPLACE_TYPE_LIST = [
    "Малый бизнес",
    "Маркетинг",
    "Управление персоналом",
    "Образование",
    "Инженерия/IT",
    "Продажи CRM"
]

WORKPLACE_DESCRIPTION_LIST = [
    "Создание эффективной системы управления задачами для повышения производительности.",
    "Структурирование пространства для более ясного обмена идеями и информацией между членами команды.",
    "Развитие гибкого графика задач для легкой адаптации к изменениям в проекте.",
    "Создание системы отслеживания, чтобы члены команды могли следить за прогрессом задач и достижением целей.",
    "Использование пространства для разработки и отслеживания стратегических целей и шагов к их достижению.",
    "Содействование развитию навыков членов команды через ясные задачи и обучающие материалы.",
    "Создание системы отчетности для анализа результатов и выявления областей для улучшения.",
    "Поддержание активного участия каждого члена команды в планировании и выполнении задач.",
    "Обеспечивание согласованности между личными и командными целями через единое пространство.",
    "Помощь членам команды определять и придерживаться приоритетных задач для более эффективного временного управления."
]

DESK_NAME_LIST = [
    "Стратегические Цели 2023",
    "Проект: Инновационные Решения",
    "Маркетинговые Кампании Q4",
    "IT Инфраструктура: Обновление и Поддержка",
    "Обучение и Развитие Команды",
    "План Мероприятий Корпоративной Культуры",
    "Проект: Зеленое Офисное Пространство",
    "Оптимизация Производственных Процессов",
    "IT Безопасность: Мониторинг Инцидентов",
    "Продуктовая Доска: Новые Возможности"
]

DESK_ACCESS_LIST = [
    "Приватная",
    "Рабочее пространство",
    "Публичная"
]

DESK_BACKGROUND_LIST = [
    "Green",
    "Red",
    "Yellow",
    "White",
    "Brown",
    "Blue",
    "Pink",
    "Orange",
    "Violet"
]

GROUP_NAME_LIST = [
    "Доски по Проектам",
    "Тематические Планы",
    "Задачи и Цели",
    "Разделение Обязанностей",
    "Контроль и Отчетность",
    "Протоны и Нейтроны",
    "Ядерная Структура",
    "Экологические Стратегии",
    "Устойчивое Развитие",
    "Здоровый Образ Жизни",
    "Путешествия и Приключения"
]