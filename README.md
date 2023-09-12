# Gilbert

Gilbert is a multipurpose General use moderation and server management bot created by @thereallonelee, written in Python using the Pycord API wrapper.

The Key purpose of this bot is to be as straightforward and easy to use for the end user as much as possible. As well as being packed with features that are commonly locked behind a pay wall on other bots.

On the backend the bot shall contain an easy to navigate file structure and "commands handler" allowing the easy implementation of new commands, as well as disabling of unwanted/unnecessary features on a per-server basis. For the time being the bot will need to be hosted individually per server. However, in the future there are plans to create a dashboard site which allows the configuration of bot settings per server with only one instance of the bot needing to be hosted.

At the time of writing Gilbert is planned to be deployed solely for assisting in the management of The Haunted Housemates Discord server. (A server for V tubers and their communities). As such there are specific commands relevant only to this use case that will be added in the current version. Should the bot ever reach a stage where it is viable to release to the public, these commands may or may not make it in the "final" version.

***

# Roadmap & Planned Features

*(In order of prioritisation, the following is planned to be added)* *(Note that a ~~Strikethrough~~ = Completed)*

- ✅ ~~Commands handler directory with each command having its own file to be called upon only when needed.~~

- ✅ ~~/ping command to show uptime and responsiveness of the bot for development and management purposes.~~

-  /set-notify command to specify which channel to send notifications to. (currently still under development)

-  /notify command to link a users discord to their twitch account allowing the bot to send a notification to
a set role once the channel is detected as live (Still work in progress)

- moderation commands such as kick, ban, warn etc. potential auto mod with a filtered list of bad words.

- Logging of moderation actions and other events to a channel of choice.

- /schedule command to allow the scheduling of events and reminders via the bot using trello as a backend for saving the information. (Potential for this command to integrate with twitches schedule api also to set 
twitch schedules automatically via discord.)

- /poll command to allow the creation of polls with multiple options and a set time limit.

- /giveaway command to allow the creation of giveaways with multiple options and a set time limit.

- /music command to allow the playing of music from YouTube and other sources.

- /level command to allow the creation of a levelling system for users.

- /role command to allow the creation of roles that can be self-assigned by users.

- /verify command to allow the creation of a verification system for users.

- And much more!

***

# Dependencies and credits! 

- [Python 3.11](https://www.python.org/downloads/)
- [PIP python package manager](https://pip.pypa.io/en/stable/installation/)
- [Pycord Discord Python API Wrapper](https://www.pycord.dev/)
- [Aiohttp](https://docs.aiohttp.org/en/stable/)
- [Twitch Api](https://dev.twitch.tv/docs/api/)
- [Trello Api](https://developer.atlassian.com/cloud/trello/rest/api-group-actions/)
- [discord Api](https://discord.com/developers/docs/intro)
- [Sparked Host VPS](https://billing.sparkedhost.com/aff.php?aff=2191)

And finally, @TheRealLoneLee for creating the bot and all of its features.
- Youtube: https://www.youtube.com/@thereallonelee
- Twitch: https://www.twitch.tv/thareallonelee
- Github: https://www.github.com/thereallonelee


Wish to support me and this project directly?:heart:

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/M4M0CE3M6)
