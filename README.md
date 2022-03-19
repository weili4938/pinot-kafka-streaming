# pinot-kafka-streaming

In this project, I set up pinot, kafka and streamlit end-to-end pipeline in a single docker container.  In pinot database, there are two tables, one is off-line batch table, and one is online streaming table. Online streaming table connected with kafka (fully integrated with pinot already).  wikievent_listener.js is a nodejs client that subsbribe to wiki public change events and push the events to kafka.  The events will be streamed to pinot database.  The front end Streamlit (app.py) will do the real-time ploting for the treaming data.

Please refer to my docker image: https://hub.docker.com/r/weili99/pinot-kafka-cluster to pull the image. The readme on docker hub gives insruction how to start the service.
