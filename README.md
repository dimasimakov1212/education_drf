# Образовательная платформа

Проект разработки LMS-системы, в которой каждый желающий может размещать свои 
полезные материалы или курсы.

Ранее в проектах мы могли сразу видеть визуальное отображение результата разработки, 
теперь работа будет над SPA-приложением и результатом создания проекта будет бэкенд-сервер, 
который возвращает клиенту JSON-структуры.

## Модели

- Пользователи
- Курсы
- Уроки
- Платежи
- Оплата через платежную систему

## Дополнительный функционал

Для разграничения прав доступа используются настройки, 
которые в DRF предоставляет пакет permissions
Добавлена валидация данных, пагинация вывода данных. Написаны тесты.

## Документация

Создана документация для фронтенд разработчиков в сервисах
swagger и redoc

## Отложенные задачи

Созданы отложенные и фоновые задачи, чтобы сокращать время обработки запроса пользователя 
и отдавать информацию как можно оперативнее.

## Контейнеризация

Контейнеризация осуществлена на базе Docker, что позволяет упаковать приложение 
и все его зависимости в единый контейнер, который можно легко переносить 
и запускать на любой совместимой с Docker системе.

Запустить проект на докере команды в терминале.

**собрать проект**
```commandline
docker compose build
```

**запустить проект**
```commandline
   docker-compose build
```

