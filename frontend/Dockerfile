# Usa imagem oficial Node.js como base
FROM node:16

# Define diretório de trabalho no container
WORKDIR /app

# Copie os arquivos package.json e package-lock.json para o container
COPY package*.json ./

# Instala dependências
RUN npm install

# Copy todo código frontend para o container
COPY . .

# Construe aplicação React para produção
RUN npm run build

# Expõe a porta 3000
EXPOSE 3000

# Comando padrão iniciar servidor desenvolvimento
CMD ["npm", "start"]
