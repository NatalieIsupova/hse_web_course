FROM alpine

RUN apk add --no-cache bash python3 \
	&& pip3 install --upgrade pip

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

CMD ["flask", "run"]
