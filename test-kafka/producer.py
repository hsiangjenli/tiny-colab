from kafka import KafkaProducer
import time

producer = KafkaProducer(
    bootstrap_servers=["localhost:29093", "localhost:39093", "localhost:49093"]
)
for i in range(10):
    print(f"Sending message {i}")
    producer.send("DEMO", b"some_message_bytes")
    time.sleep(0.3)
