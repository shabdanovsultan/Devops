# Используем базовый образ Ubuntu
FROM ubuntu:latest

# Обновляем систему и устанавливаем необходимые пакеты
RUN apt-get update -qy
RUN apt-get install -qy python3 python3-pip python3-dev

# Создаем рабочую директорию для приложения
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python3", "app.py"

