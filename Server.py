# coding=utf-8
import logging
from websocket_server import WebsocketServer
import sys
import imp

imp.reload(sys)

def new_client(client, server):
    print("Client(%d) has joined." % client['id'])


def client_left(client, server):
    print("Client(%d) disconnected" % client['id'])


def message_back(client, server, message):
    # The message parameter here is the content passed in by the client
    print("Client(%d) said: %s" % (client['id'], message))
    result = "The server has received the message..." + message
    # Return the processed data to the client
    server.send_message(client, result)


# Create a new websocketserver object
server = WebsocketServer(8080, host='127.0.0.1')
# Set actions when a new client accesses
server.set_fn_new_client(new_client)
# Set actions when a client is disconnected
server.set_fn_client_left(client_left)
# Set the operation after receiving a message sent by a client
server.set_fn_message_received(message_back)
# Set up service to run all the time
server.run_forever()
