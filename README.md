# Mailbot

<img src='https://github.com/tekofu/Mailbot/raw/master/Assets/Circle-Icon.png'>

**A bad Discord bot written in Python**

## Some features it has includes:
- Echo text back with string manipulation
- Play Rock paper scissors with the bot
- Search for YouTube videos / Wikipedia articles / Urban Dictionary slang
- Magic 8-Ball responses
- Random bonequest comics
- Self pinning to a dedicated channel
- Image mirroring
- Searching the FFXIV marketboards

## Getting Started:
Requirements: 
- [discord.py](https://discordpy.readthedocs.io/en/latest/)
- [Pillow](https://pillow.readthedocs.io/en/stable/)

Installation:
1. Install the required libraries with `python -m pip install -r requirements.txt`
2. Create the file `config.json` in the same directory as `main.py`
3. In `config.json` create a value for `discordToken` (Required Discord bot token). And optionally: `youtubeToken` (YouTube API token), `xivToken` (XIVAPI token) and `starboardID` (The ID of the channel you want the bot to repost pinned posts). For example:
```
{
    "discordToken" : "token goes here!",
    "youtubeToken" : "token goes here!",
    "xivToken"     : "token goes here!",
    "starboardId"  : { 
        "Guild ID for Server 1" : "Starboard ID for Server 1",
        "Guild ID for Server 2" : "Starboard ID for Server 2",
        ...
    }
}
```
4. Run `main.py`

## TODO:
- Use URLs for image manip as well as content
- Random septapus comic posting
- Fix cry functionality from [original source](https://github.com/dead-bird/apcry/blob/master/api/cry.js) - just needs the math tweaking and adding swapping characters
- More dumb joke features
- Add bot posts when people in the server go live on twitch.tv (possible automatically or need a list?)
- Add poll functionality with categories/running "scores"

