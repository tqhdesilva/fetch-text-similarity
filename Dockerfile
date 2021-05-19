FROM python:3.9
WORKDIR /app
COPY requirements.txt text_similarity.py app.py ./
RUN pip install -r requirements.txt
ENTRYPOINT ["uvicorn", "app:app"]
CMD ["--host", "0.0.0.0", "--port", "80"]