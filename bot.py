
import os
import slack
from mcstatus import MinecraftServer

slack_client = slack.WebClient(token=os.environ['SLACK_BOT_TOKEN'])

channel = "#braveworld"
server_ip = "braveboi.com:25565"

try:
    server = MinecraftServer.lookup(server_ip)
    ping = server.ping()
except Exception as ex:
    response = slack_client.chat_postMessage(
        channel=channel,
        text='<!here> Server "' + server_ip + '" is down!')
