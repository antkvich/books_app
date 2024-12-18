# API Документация

## Добавление новой книги

**POST /api/books**

Пример запроса:  
```json
{
    "title": "Book Title",
    "author": "Author Name",
    "publication_date": "2023-01-01",
    "page_count": 300
}
```

---

## Просмотр списка книг

**GET /api/books**

---

## Просмотр списка книг с ранжированием по количеству страниц за период публикации

**GET /api/rankedBooks/?start_date=2021-01-01&end_date=2027-12-31**

---

## Настройки переменных среды (.env)

```plaintext
TASK_INTERVAL         #minutes
EMAIL_RECIPIENT

EMAIL_HOST
EMAIL_PORT
EMAIL_HOST_USER
EMAIL_HOST_PASSWORD
EMAIL_USE_TLS

CELERY_BROKER_URL

DEBUG
DB_NAME
DB_USER
DB_PASSWORD
DB_HOST
DB_PORT
```

---

## SQL запрос для задания

```sql
WITH RankedBooks AS (
    SELECT 
        id,
        title,
        page_count,
        ROW_NUMBER() OVER (ORDER BY page_count DESC) AS rank
    FROM 
        books_book
    WHERE 
        publication_date BETWEEN '2021-01-01' AND '2027-12-31'
)
SELECT * FROM RankedBooks;
```
