# Discord-bot-ping-forward
  Forwards pings to the user

# Discord bot ping forwarder

This is a python (designed in 3.11) bot that forwards messages that reply to the user or mention the user to the specified user.

This project was designed to improve productivity within my companies work server among. It is designed in sprints whenever I'm taking a break and thus do not expect the code to be peer reviewed and expect less production quality due to the urgency my work places vs the reduced importance of this project. 

There are two main branches of this project:
- Main - for local deployment
- Server - for CI/CD deployment with a server

You are currently on the `server` branch

This part of the project I am going to be brushing up on my CI/CD skills.
The development will start by assuming deployment on a raspberry pi
## Features

To forward messages to your own DM's:
```!add-forward```

To forward messages that mention you to another user:
```!add-forward {users id}```

When a user on the forward list is mentioned, the bot will dm the following to the forwarding address's dms:
- The user who sent the message
- a jump url to that message
- The content of that message
- Any attchments in that message
- Any embeds in that message

Here is an example dm forward:
![Sample dm forward](https://imgur.com/a/QAvqDo0)

When a user replies to that forwarded message, the bot forwards only the content of that message back to the original poster as a reply to that post.

Managment of the initial forwarding is stateful as it saves a config of who's pings to listen to and who that users wishes they are forwarded to. 

Managment of the reply to the dm is stateless as it disects the jump link from the initial forward to retrieve the original message to reply to. 

## Installation

Comming with future dev