# Dockerfile

FROM python:3.9-slim

WORKDIR /app

COPY ./api/ /app/api/
COPY ./streamlit_app/ /app/streamlit_app/
COPY ./utils/ /app/utils/
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
