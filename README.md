# minecraft-uptime-slackbot

A simple Minecraft server uptime Slack bot that utilizes [Dinnerbone's mcstatus](https://github.com/Dinnerbone/mcstatus)

## Requirements

`SLACK_BOT_TOKEN` environment variable must be set. This is the Slack Bot's OAuth token. The token must have permission to post messages

## Wishlist

Features I would like to add:

- React to Slack "slash commands" to report server status, player count, MOTD
- Track amount of downtime
- Calculate server total uptime given start date and amount of downtime tracked
