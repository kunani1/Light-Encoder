FROM colserra/light-encoder:anime
WORKDIR /bot
COPY requirements.txt .
RUN pip install --upgrade -r requirements.txt
COPY . .
CMD ["bash", "start.sh"]
