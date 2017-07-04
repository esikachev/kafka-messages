Kafka-messages
==============


How to use
----------

1. Install requirements form `requirements.txt`

.. sourcecode:: console

    $ pip install -r requirements.txt
..

2. Add to /etc/hosts maping of nodes, like

.. sourcecode:: console
   111.111.111.111 machine1
   222.222.222.222 machine2
..

3. Run script like

.. sourcecode:: console

    $ python kafka_messages.py -k localhost:9092 -t test
..
