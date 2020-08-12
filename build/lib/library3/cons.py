from kafka import KafkaConsumer
import json
def consume_kafka_message(topikName,group_id):
    servers=["localhost:9092"]
    topicName="topik11"
    consumer=KafkaConsumer(topicName, group_id="user5", bootstrap_servers=servers, auto_offset_reset="earliest"
    )
    for msg in consumer:
        data=json.loads(msg.value)
        return data["first_name"]+data["last_name"]