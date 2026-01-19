FROM python:3.12.12-slim-bookworm

# set the working directory
WORKDIR /terrys6

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=/terrys6

# copy requirements first and install
COPY requirements.txt /terrys6/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /terrys6/requirements.txt

# copy the entire backend into a folder named backend
# COPY . /terrys6/backend


EXPOSE 8000

# start the app
CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]