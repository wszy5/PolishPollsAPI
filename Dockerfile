FROM python:3.10
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
EXPOSE 30911
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "30911"]