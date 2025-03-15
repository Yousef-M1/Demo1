FROM python:3.9-alpine3.13
LABEL maintainer="YousefMusleh.com"

# Ensure Python output is sent straight to the terminal
ENV PYTHONUNBUFFERED=1

# Copy the requirements and app files
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app

# Set working directory
WORKDIR /app

# Expose the default port for Django
EXPOSE 8000

ARG DEV=false

# Install dependencies and create a virtual environment
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
         django-user

# Set environment variables and switch to the new user
ENV PATH="/py/bin:$PATH"
USER django-user
