# Use uma imagem base oficial do Python
FROM python:3.8-slim

# Defina o diretório de trabalho
WORKDIR /app


# Instale as dependências
RUN pip install colorama
RUN pip install flask
# Copie o restante do código do aplicativo para o diretório de trabalho
COPY . .

# Informe ao Docker qual porta o aplicativo estará disponível
EXPOSE 8080

# Comando para executar o aplicativo usando Gunicorn, por exemplo
CMD ["cd python_flask  ", "python nivistealer.py"]