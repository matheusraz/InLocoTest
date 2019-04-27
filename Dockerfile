FROM python:3.5
ADD . /code
WORKDIR /code
CMD ["python", "exec.py"]