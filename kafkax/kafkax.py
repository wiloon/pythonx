from kafka import KafkaProducer


def send_to_kafka(msg):
    print("sending")
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
    future = producer.send('topic0', key=b'key0', value=b'value0')
    print(future)
    result = future.get(timeout=10)
    print(result)

    return
