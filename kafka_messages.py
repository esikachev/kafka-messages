import threading, logging, time
import multiprocessing

import argparse
from kafka import KafkaConsumer, KafkaProducer


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--kafka-socket', '-k', default='', nargs='?',
                        help='Kafka host:port')
    parser.add_argument('--topic-name', '-t', default='', nargs='?',
                        help='Name of the Kafka topic for writing')
    
    args = parser.parse_args()
    print(args.kafka_socket, args.topic_name)
    return (args.kafka_socket, args.topic_name)


class Producer(threading.Thread):
    def __init__(self):
        super(Producer, self).__init__()
        self.kafka_host, self.topic_name = get_args()

    daemon = True

    def run(self):
        producer = KafkaProducer(bootstrap_servers=self.kafka_host)

        while True:
            producer.send(self.topic_name, b"test")
            time.sleep(1)


class Consumer(multiprocessing.Process):
    def __init__(self):
        super(Consumer, self).__init__()
        self.kafka_host, self.topic_name = get_args()

    daemon = True

    def run(self):
        consumer = KafkaConsumer(bootstrap_servers=self.kafka_host,
                                 auto_offset_reset='earliest')
        consumer.subscribe([self.topic_name])

        for message in consumer:
            print (message)


def main():
    tasks = [
        Producer(),
        Consumer()
    ]

    for task in tasks:
        task.start()

    time.sleep(10)

if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.DEBUG
        )
    main()
