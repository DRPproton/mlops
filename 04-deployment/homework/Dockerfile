FROM agrigorev/zoomcamp-model:mlops-2024-3.10.13-slim

RUN pip install pipenv
RUN pip install pyarrow

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["script.py", "./"]

ENTRYPOINT [ "python", "script.py" ]