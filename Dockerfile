# Используем базовый образ Python
FROM python:3

# Устанавливаем рабочую директорию в контейнере
WORKDIR /code

# Копируем зависимости в контейнер
COPY ./requirements.txt /code/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r /code/requirements.txt

# Копируем код приложения в контейнер
COPY . .
