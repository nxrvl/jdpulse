# Build stage
FROM node:19 AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Production stage
FROM node:19-alpine
WORKDIR /app
COPY --from=build /app/package*.json /app/
COPY --from=build /app/dist /app
COPY --from=build /app/node_modules /app/node_modules
EXPOSE 5173
CMD [ "yarn", "dev"]
