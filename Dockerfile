FROM python:3.7-slim
COPY ./Pipfile /deploy/
COPY ./src/app.py /deploy/src/
COPY ./src/split_time_predictor.py /deploy/src/
COPY ./models/main_model_5.pkl /deploy/models/
COPY ./models/main_model_10.pkl /deploy/models/
COPY ./models/main_model_15.pkl /deploy/models/
COPY ./models/main_model_20.pkl /deploy/models/
COPY ./models/main_model_25.pkl /deploy/models/
COPY ./models/main_model_30.pkl /deploy/models/
COPY ./models/main_model_35.pkl /deploy/models/
COPY ./models/main_model_40.pkl /deploy/models/
WORKDIR /deploy/
RUN pip install pipenv
RUN pipenv install --skip-lock
WORKDIR /deploy/src/
EXPOSE 80
ENTRYPOINT ["pipenv", "run", "python", "app.py"]