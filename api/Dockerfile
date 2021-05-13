# ---- Base python ----
FROM python:3.8 AS base
# Create app directory
WORKDIR /app

# ---- Dependencies ----
FROM base AS dependencies
COPY requirements.txt ./
# install app dependencies
RUN pip install -r requirements.txt

# ---- Copy Files/Build ----
FROM dependencies AS build
WORKDIR /app
COPY src /app
# Build / Compile if required

# --- Release with Alpine ----
FROM python:3.8-alpine3.12 AS release

WORKDIR /app

COPY --from=dependencies /app/requirements.txt ./
COPY --from=dependencies /root/.cache /root/.cache

EXPOSE 5000
# Install app dependencies
RUN pip install -r requirements.txt
COPY --from=build /app/ ./
CMD ["gunicorn", "-w 4", "-b 0.0.0.0:5000", "app:app"]
