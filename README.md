# kafka_project
This project uses stock market data with the help of Kafka to simulate the real time data.

# Prerequisite
1. AWS account
2. Python
3. Libraries needed - confluent_kafka, boto3 and pandas, 
# Steps to run the code
1. SSH into EC2 instance.
2. Install kafka in the EC2 instance.
4. Change directory to your kafka folder in EC2 and update the "config/server.properties" file for ADVERTISED_LISTENERS to public ip of the EC2 instance using the command "sudo nano config/server.properties"
5. Start zoo keeper using command "bin/zookeeper-server-start.sh config/zookeeper.properties"
6. Open another SSH session to EC2 and change your directory to kafka folder
7. Use command " export KAFKA_HEAP_OPTS = '-Xmx256M -Xms128M' " to increase kafka server memory
8. Start Kafka Server using "bin/kafka-server-start.sh config/server.properties"
9. Open another SSH session to EC2 and change your directory to kafka folder.  <br />
Use command "bin/kafka-topics.sh --create --topic {your topic name} --bootstrap-server {EC2 public IP}:9092 --replication-factor 1 --partitions 1"
10. Make you kafka_consumer.py executable using "chmod u+x" command. Run your producer script then run your consumer script
11. Create AWS Glue crawler to create a table from your S3 location.
12. Use Amazon Athena to query the data.
