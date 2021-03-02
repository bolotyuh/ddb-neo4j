# UCU Distributed database course

## Робота з базовими функціями граф-орієнтованої БД на прикладі Neo4j

### [Завдання](https://docs.google.com/document/d/13ZX8VeyXt_JZGGzFLQRC063aGzDWsA9H2e9JsPMTxAY/edit)

### Запустити docker-compose

```bash
$ docker-compose up --build -d
```

### Скрипт для завантаження даних

```bash
$ docker-compose exec app python -m app.generate_data.py
```

#### Neo4j Browser
```javascript
http://localhost:7474/browser/
```


### [Виконане завдання](REPORT.md)