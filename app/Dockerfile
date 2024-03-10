FROM python:3.12
WORKDIR /app
RUN pip install --no-cache-dir uvicorn blacksheep
COPY index.html .
COPY server.py .
EXPOSE 80
CMD ["uvicorn", "server:app", "--host=0.0.0.0", "--port=80"]
