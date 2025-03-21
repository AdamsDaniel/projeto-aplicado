# Use a imagem oficial do Python como base
FROM python:3.9-slim

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie os arquivos de requisitos para o container
COPY requirements.txt .

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o código do backend para o container
COPY . .

# Exponha a porta 5000
EXPOSE 5000

# Comando padrão para iniciar a aplicação Flask
CMD ["python", "app.py"]
