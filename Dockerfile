# 
FROM python:3.10-slim

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN python3 -m pip install --no-cache-dir --user -r requirements.txt

# 
COPY ./app /code/app

# 
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "80"]
