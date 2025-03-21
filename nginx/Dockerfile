# Use a imagem oficial do Nginx como base
FROM nginx:latest

# Copie a configuração personalizada do Nginx para dentro do container
COPY nginx.conf /etc/nginx/nginx.conf

# Exponha as portas 80 e 443 (HTTP e HTTPS)
EXPOSE 80 443

# O Nginx já inicia automaticamente como comando padrão da imagem base.
