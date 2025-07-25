├── alchem/ # Основные настройки Django
│ ├── settings.py # Конфигурация проекта
│ ├── urls.py # Маршрутизация
│ └── wsgi.py # WSGI-скрипт
├── App/ # Основное Django-приложение
│ ├── models.py # Модели данных
│ ├── views.py # Вьюхи
│ ├── admin.py # Админка
│ └── ...
├── manage.py # Django-менеджер
├── .gitignore # Игнорируемые файлы
└── README.md # Документация


---

## ⚡ Быстрый старт

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/Azarafel/Alchem.git
   cd Alchem
   ```
2. **Создайте виртуальное окружение и установите зависимости:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. **Примените миграции и запустите сервер:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

---

## 🛠️ Для разработчиков

- Код оформлен по PEP8
- Используйте ветки feature/ для новых фич
- Pull Request приветствуются!

---

## 🤝 Контрибьюторам

Будем рады вашим PR! Перед отправкой:
- Проверьте, что код проходит тесты
- Оформите коммиты понятно
- Описывайте изменения в PR

---

## 📄 Лицензия

Проект распространяется под лицензией MIT. Используйте свободно!

---

> Сделано с ❤️ на Python и Django
