#!/usr/bin/env python3
import yaml
from confluent_kafka import Consumer
from utils.utils import CONFIG, upload_to_s3

if __name__ == '__main__':
    config = {
        'bootstrap.servers': CONFIG.kafka['socket'],
        'group.id':          'kafka-rahul-test',
        'auto.offset.reset': 'earliest'
    }

    consumer = Consumer(config)
    consumer.subscribe([CONFIG.kafka['topic']])
    bucket = CONFIG.s3_bucket['name']
    folder = CONFIG.s3_bucket['folder']
    
    try:
        suffix = 0
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                print("Waiting...")
            elif msg.error():
                print(f"ERROR: {msg.error()}")
            else:
                print(f"Consumed event from topic {msg.topic()}: key = {msg.key()} value = {msg.value()}")
                print(f'uploading data to s3 bucket: {bucket}')
                upload_to_s3(msg.value(), bucket, f"{folder}/test_{suffix}.json")
                suffix += 1
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()