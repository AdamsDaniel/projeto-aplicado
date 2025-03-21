# Use imagem oficial Python como base
FROM python:3.9-slim

# Define diretório de trabalho no container
WORKDIR /app

# Copia arquivos de requisitos para o container
COPY requirements.txt .

# Instala dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia código backend para container
COPY . .

# Expoe porta 5000
EXPOSE 5000

# Comando padrão iniciar Flask
CMD ["python", "app.py"]
