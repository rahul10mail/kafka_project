import pandas as pd
from time import sleep
import json
from confluent_kafka import Producer
from kafka import KafkaProducer
import yaml
from utils.utils import CONFIG
import socket

conf = {
	'bootstrap.servers': CONFIG.kafka['socket'],
	'client.id': socket.gethostname()
}

producer = Producer(conf)
df = pd.read_csv(CONFIG.dataset['stock'])

while True:
	stock_value = df.sample(1).to_dict(orient = 'records')[0]
	print('producing data')
	producer.produce(CONFIG.kafka['topic'], key="key", value=json.dumps(stock_value).encode('utf-8'))
	sleep(2)

producer.flush()
