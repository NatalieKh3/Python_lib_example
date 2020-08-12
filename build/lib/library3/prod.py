from kafka import KafkaProducer
import json
def send_kafka_message(c, topicName):
    servers=["localhost:9092"]
    topicName="topik11"
    producer=KafkaProducer(bootstrap_servers=servers)
    # d={
    #     "name":"Natalie",
    #     "message":"Hello! My name is Natalie!"
    }
    c={
        "first_name":"Natalie",
        "last_name":"Hwang",
        "email":"khvannatalie@gmail.com"
    }
    # arrJson=json.dumps(d)
    # arrBytes=bytearray(arrJson, 'utf-8')
    # producer.send(topicName, arrBytes)
    # producer.flush()
    lines=json.dumps(c)
    Bytes=bytearray(lines, 'utf-8')
    producer.send(topicName, Bytes)
    producer.flush()
    return "OK"