FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN pip install .
RUN edgar_news create-db
RUN edgar_news populate-db
RUN edgar_news add-user -u admin -p admin
EXPOSE 5000
CMD ["edgar_news", "run"]
