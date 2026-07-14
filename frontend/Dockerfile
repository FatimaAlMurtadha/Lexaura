# Frontend Dockerfile
# Installs dependencies, builds the Next.js app, and runs it.

FROM node:20-alpine

WORKDIR /app
COPY package*.json ./
RUN npm install --legacy-peer-deps

COPY . .
RUN npm run build

EXPOSE 3000
CMD ["npm", "run", "start"]