FROM node:23-slim AS build

WORKDIR /app

COPY . .

RUN npm install && npm run build

FROM nginx:alpine

COPY --from=build /app/dist /usr/share/nginx/html

# Remove a configuração padrão do NGINX
RUN rm /etc/nginx/conf.d/default.conf

# Adiciona nova configuração
COPY nginx.conf /etc/nginx/conf.d

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
