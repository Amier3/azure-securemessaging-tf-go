import asyncio
from azure.servicebus.aio import ServiceBusClient
from azure.servicebus import ServiceBusMessage

NAMESPACE_CONNECTION_STR = ""
TOPIC_NAME = "tutorial-topic"

async def send_message(sender):
    message = ServiceBusMessage("You can use Azure Service Bus to send any piece of data that needs to be recieved")
    await sender.send_messages(message)
    print("Secure Message Successfully sent")

async def run():
    async with ServiceBusClient.from_connection_string(
        conn_str=NAMESPACE_CONNECTION_STR,
        logging_enable=True) as servicebus_client:
        sender = servicebus_client.get_topic_sender(topic_name=TOPIC_NAME)
        async with sender:
            await send_message(sender)

asyncio.run(run())
print("-----------------------")