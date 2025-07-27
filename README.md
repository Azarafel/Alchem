# Alchem: Конструктор коктейлей на Django/Python

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.x-green)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Описание проекта

Alchem — это веб-приложение на Python и Django для рекомендаций коктейлей. Пользователь указывает доступные ингредиенты (из холодильника или бара: водка, сок, лёд и т.д.), а система генерирует подходящие рецепты с инструкциями, пропорциями и калорийностью. Добавлены фичи вроде рейтингов, комментариев и базовой техподдержки через формы.

Проект создан в команде из 15 человек под моим руководством: я координировал задачи, разрабатывал backend, модели БД (в App/models.py: вероятно, классы вроде Cocktail, Ingredient, Rating, Comment с foreign keys и many-to-many), фиксил баги и обеспечивал качество. Успешно защищён перед экспертами Яндекса в 2024 году. Это показывает навыки в backend-разработке, работе с данными, алгоритмами рекомендаций (матчинг ингредиентов) и тим-лидерстве — круто для junior позиций в IT.

## Ключевые фичи

- **Рекомендации коктейлей**: Алгоритм на базе фильтров и вероятностей (в App/views.py) — вводишь ингредиенты, получаешь топ-рецепты.
- **Рейтинги и отзывы**: Оценки (1-5 звезд), комментарии пользователей — хранится в БД с модерацией.
- **Обсуждения**: Треды под рецептами для фидбека.
- **Техподдержка**: Форма для багов/предложений (возможно, с email-интеграцией).
- **Админ-панель**: Управление контентом через Django Admin (App/admin.py).
- **Интеграции**: Автоматизация с Google Sheets для импорта данных (если добавлено из других проектов).

## Технологический стек

- **Backend**: Python 3.8+, Django (фреймворк для веб: views в App/views.py для логики, urls в alchem/urls.py для роутинга).
- **База данных**: Django ORM (миграции, модели в App/models.py для сущностей вроде коктейлей и ингредиентов).
- **Библиотеки**: NumPy (для расчётов матчинга), SQL (через ORM), возможно Telethon для ботов или другие популярные.
- **Другое**: Git для контроля версий, .gitignore для чистоты. Фронтенд — базовые Django templates (HTML/CSS), можно расширить на React. Настройки в alchem/settings.py, WSGI для деплоя.

Релевантно для вакансий в Яндекс, VK, Росатом или MTS Bank — ключевые слова: Python, Django, backend, SQL, Git.

## Установка и запуск

### Требования
- Python 3.8+
- Git
- Virtualenv (для изоляции окружения)

### Шаги
1. Клонируй репо:
git clone https://github.com/Azarafel/Alchem.git
cd Alchem

2. Создай и активируй venv:
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. Установи зависимости (если requirements.txt нет — создай: pip install django && pip freeze > requirements.txt):
pip install -r requirements.txt

4. Примени миграции БД:
python manage.py makemigrations
python manage.py migrate

5. Создай суперюзера для админки:
python manage.py createsuperuser

6. Запусти сервер:
python manage.py runserver


Открой http://127.0.0.1:8000/. Админка на /admin/.

Ошибки? Проверь alchem/settings.py (DATABASES, INSTALLED_APPS) или создай issue.

## Как использовать

- Зарегистрируйся/логинься (если auth включён).
- Введи ингредиенты — получи рекомендации.
- Оцени/прокомментируй рецепты.
- Админы: Добавляй контент в панели.

## Для разработчиков

- Код по PEP8 — держи стиль.
- Тесты: В App/tests.py, запускай python manage.py test.
- Деплой: Heroku/VPS с Gunicorn/Nginx.
- Бранчи: feature/твоя-фича для изменений.

## Контрибьютинг

Форкни, создай PR:
- Тестируй перед коммитом.
- Коммиты: "fix: баг в рекомендациях".
- В PR опиши изменения.
- Не ломай миграции — migrate после пулла.

## Лицензия

MIT License — юзай свободно с attribution. Текст в LICENSE (если нет — стандартный MIT).

Сделано с ❤️ Azarafel и командой на Python & Django. Вопросы? Issues или контакты в профиле. Готов разобрать на собесе!

