# Use a imagem oficial do Node.js como base
FROM node:16

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie os arquivos package.json e package-lock.json para o container
COPY package*.json ./

# Instale as dependências do projeto
RUN npm install

# Copie todo o código do frontend para o container
COPY . .

# Construa a aplicação React para produção
RUN npm run build

# Exponha a porta 3000
EXPOSE 3000

# Comando padrão para iniciar o servidor de desenvolvimento
CMD ["npm", "start"]
