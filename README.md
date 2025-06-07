# Telegram AI Bot

Этот проект представляет собой Telegram-бота с подключенной нейросетью на основе AI API.

## 📌 Функции
- Обрабатывает команду `/start`
- Отвечает на любые сообщения, используя AI API
- Развёртывается в **Google Cloud Run** или **Google App Engine**

## 🚀 Установка и запуск локально

### 1️⃣ Клонирование репозитория
```bash
git clone https://github.com/ТВОЙ_РЕПО/telegram-ai-bot.git
cd telegram-ai-bot
```

### 2️⃣ Установка зависимостей
```bash
pip install -r requirements.txt
```

### 3️⃣ Создание `config.py`
Создай файл `config.py` и добавь в него:
```python
TOKEN = "ТВОЙ_ТОКЕН_БОТА"
TOKEN_AI = "ТВОЙ_ТОКЕН_ИИ"
```

### 4️⃣ Запуск бота
```bash
python bot.py
```

## 📦 Деплой в Google Cloud Run

### 1️⃣ Установка Google Cloud SDK
```bash
gcloud auth login
gcloud config set project [ТВОЙ_ПРОЕКТ]
```

### 2️⃣ Сборка Docker-образа
```bash
docker build -t telegram-bot .
```

### 3️⃣ Публикация в Google Container Registry
```bash
gcloud builds submit --tag gcr.io/[ТВОЙ_ПРОЕКТ]/telegram-bot
```

### 4️⃣ Деплой в Google Cloud Run
```bash
gcloud run deploy telegram-bot --image gcr.io/[ТВОЙ_ПРОЕКТ]/telegram-bot --platform managed
```

## 📦 Деплой в Google App Engine
```bash
gcloud app deploy
```

## 📜 Структура проекта
```plaintext
/mybot
│── bot.py         # Основной файл запуска
│── config.py      # Конфигурация (токены)
│── handlers/      # Обработчики команд
│    ├── start.py  # Команда /start
│    ├── chat_ai.py # Обработчик сообщений с нейросетью
│── requirements.txt # Зависимости
│── Dockerfile     # (если деплоишь в контейнер)
│── app.yaml       # (если деплоишь в GCP App Engine)
```

## 💡 Контакты
Если у тебя есть вопросы — пиши мне в Telegram!

# estbot
