FROM python:3.10-slim
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . .
CMD ["uvicorn", "system_monitor_deploy:sistem_app", "--host", "0.0.0.0", "--port", "7860"]
ENV PYTHONIOENCODING=utf-8
ENV LANG=C,UTF-8