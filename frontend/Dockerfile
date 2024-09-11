FROM node:bullseye-slim
# see https://docs.docker.com/compose/file-watch/#prerequisites
RUN useradd -ms /bin/sh -u 1001 app
USER app

WORKDIR /app/frontend
EXPOSE 8001
COPY --chown=app:app package*.json ./
RUN npm install
COPY --chown=app:app . .
CMD ["npm", "run", "dev-docker"]