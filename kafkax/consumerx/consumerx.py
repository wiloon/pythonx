from kafka import KafkaConsumer


def consume_topic0():
    consumer = KafkaConsumer('topic0', group_id='group0', bootstrap_servers=['localhost:9092'])
    for msg in consumer:
        print(msg)
