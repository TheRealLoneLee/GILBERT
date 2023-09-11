# Gilbert

Gilbert is a multipurpose General use moderation and server management bot created by @thereallonelee, written in Python using the Discordia API wrapper.

The Key purpose of this bot is to be as straightforward and easy to use for the end user as much as possible. Aswell as being packed with features that are commonly locked behind a pay wall on other bots.

On the backend the bot shall contain an easy to navigate file structure and "commands handler" allowing the easy implementation of new commands, aswell as disabling of unwanted/unnecessary features on a per server basis. For the time being the bot will need to be hosted individually per server. However in the future there are plans to create a dashboard site which allows the configuration of bot settings per server with only one instance of the bot needing to be hosted.

At the time of writing Gilber is planned to be deployed solely for assisting in the management of The Haunted Housemates Discord server. (A server for Vtubers and their communities). As such there are specific commands relevant only to this use case that will be added in the current version. Should the bot ever reach a stage where it is viable to release to the public, these commands may or may not make it in the "final" version.

***

# Roadmap & Planned Features

*(In order of prioritisation, the following is planned to be added)*

- ~~Commands handler directory with each command having its own file to be called upon only when needed.~~

- Logging in channels, a command to setup logging will be made that allows defining which actions are to be logged in which channels, this will then be saved to a configuration file which the bot will read upon startup in the main bot.Py file.

- Moderation commands such as timeout, ban, kick etc.

- Role selection (fairly straight forward)

- Rule verification

- Ticket system (fairly straight forward)

- Automatic ping/message in specified channels on video uploads to tiktok, youtube, and live streams on Twitch, with appropriate links.

- Embed creator* (this may require the use of an external dashboard)

***

# Dependencies and credits! 

- [Discordia Python Wrapper](https://github.com/SinisterRectus/Discordia)
- [discordia-slash application commands](https://github.com/GitSparTV/discordia-slash)
- [discordia-interactions](https://github.com/Bilal2453/discordia-interactions)
- [Sparked Host VPS](https://billing.sparkedhost.com/aff.php?aff=2191)

Wish to support me and this project directly?:heart:

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/M4M0CE3M6)
