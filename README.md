# My Django Project — Deployed on Render

## 🚀 Deployment

Deployed via [Render.com](https://render.com)

- Web: `gunicorn myproject.wsgi`
- Worker: `celery -A myproject worker`

## 🔧 Environment Variables (Set in Render Dashboard)

- `SECRET_KEY`
- `DATABASE_URL` (PostgreSQL)
- `CELERY_BROKER_URL` (CloudAMQP)
- `EMAIL_*` for SMTP

## 📚 API Docs

Swagger UI: `https://your-app.onrender.com/swagger/`

## 🧪 Test

Register a user → should trigger welcome email via Celery.
