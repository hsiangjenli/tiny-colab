from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "DEMO", bootstrap_servers=["localhost:29093", "localhost:39093", "localhost:49093"]
)
for msg in consumer:
    print(f"Received message: {msg.value}")
