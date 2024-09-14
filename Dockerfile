############################################################
# Setup sveltekit w/ node
############################################################
FROM node:bullseye-slim AS build-svelte

WORKDIR /app

COPY ./frontend/package*.json ./
RUN npm install

COPY ./frontend ./

RUN npm run build

############################################################
# Setup fastapi
############################################################
# see https://github.com/astral-sh/uv-docker-example/blob/main/multistage.Dockerfile
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS build-fastapi
ENV UV_COMPILE_BYTECODE=1 
ENV UV_LINK_MODE=copy

WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=./backend/uv.lock,target=uv.lock \
    --mount=type=bind,source=./backend/pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

ADD ./backend ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

############################################################
# Final image w/ node & fastapi
############################################################
FROM node:bullseye-slim AS node
FROM python:3.12-slim-bookworm

WORKDIR /app

# Copy binaries from official Node image
COPY --from=node /usr/lib /usr/lib
COPY --from=node /usr/local/share /usr/local/share
COPY --from=node /usr/local/lib /usr/local/lib
COPY --from=node /usr/local/include /usr/local/include
COPY --from=node /usr/local/bin /usr/local/bin

# COPY --from=build-svelte /app/build .
# COPY --from=build-svelte /app/package.json .
# COPY --from=build-svelte /app/package-lock.json .

COPY --from=build-svelte /app/build ./client/build
COPY --from=build-svelte /app/main.js ./client
COPY --from=build-svelte /app/package.json ./client
COPY --from=build-svelte /app/package-lock.json ./client

RUN cd ./client && npm ci --omit dev && cd ..

COPY --from=build-fastapi --chown=app:app ./app ./
ENV PATH="/app/.venv/bin:$PATH"

# RUN apk update
# RUN apk add nginx

# CMD fastapi run quizapp/main.py && node .

# RUN pip install supervisor
# RUN mkdir -p /var/log/supervisor
# COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# CMD ["~/usr/local/lib/python3.12/site-packages/supervisord"]
# CMD ["echo"]
# ENTRYPOINT ["tail", "-f", "/dev/null"]

EXPOSE 3000

COPY ./start.sh ./
# ENTRYPOINT ["./start.sh"]
ENTRYPOINT ["echo", "hello world"]