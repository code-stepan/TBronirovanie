# TBronirovanie - система бронирования билетов

Проект реализует архитектуру в 3 слоя:
- `src/domian` - доменная логика (модели, сервисы, паттерны Builder/Factory)
- `src/interface` - интерфейсный слой (заготовка для чекпоинта 2)
- `src/infrastructure` - инфраструктура (JSON-репозиторий, вспомогательные компоненты)

## Чекпоинт 1 (доменное ядро)

Реализовано:
- доменные сущности: `User`, `Event`, `Ticket`, `Booking`
- `UserBuilder` для поэтапной сборки пользователя
- `TicketFactory` для создания билетов по типу (`Standard`, `VIP`, `EarlyBird`)
- `BookingService` для создания/отмены брони и проверки доступности мест
- `JSONRepository` как простое хранилище бронирований

## Установка

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Запуск демо-сценария

```bash
python main.py
```

После запуска создаётся пользователь, билет, бронь и запись сохраняется в `data/bookings.json`.

## Документация чекпоинта 1

- Архитектурное описание: `docs/architecture_checkpoint_1.md`
- UML Domain слоя (PlantUML): `docs/domain_uml_checkpoint_1.puml`
