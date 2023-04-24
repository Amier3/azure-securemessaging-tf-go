import asyncio
from azure.servicebus.aio import ServiceBusClient

NAMESPACE_CONNECTION_STR = ""
SUBSCRIPTION_NAME = "tutorial-subscription"
TOPIC_NAME = "tutorial-topic"


async def run():
    async with ServiceBusClient.from_connection_string(
        conn_str=NAMESPACE_CONNECTION_STR,
        logging_enable=True) as servicebus_client:

        async with servicebus_client:
            receiver = servicebus_client.get_subscription_receiver(topic_name=TOPIC_NAME, 
            subscription_name=SUBSCRIPTION_NAME, max_wait_time=5)
            async with receiver:
                received_msgs = await receiver.receive_messages(max_wait_time=5, max_message_count=20)
                for msg in received_msgs:
                    print("Received: " + str(msg))
                    receiver.complete_message(msg)
asyncio.run(run())
