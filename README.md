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

## Getting Started:
Requirements: 
- [discord.py](https://discordpy.readthedocs.io/en/latest/)
- [Pillow](https://pillow.readthedocs.io/en/stable/)

Installation:
1. Install the required libraries shown above
2. Create the file `config.json` in the same directory as `main.py`
3. In `config.json` create values for `discordToken`, `youtubeToken` and `starboardID`: the ID of the channel you want the bot to repost pinned images. For example:
```
{
    "discordToken" : "token goes here!",
    "youtubeToken" : "token goes here!",
    "starboardId"  : "ID goes here!"
}
```
4. Run `main.py`

## TODO:
- Use URLs for image manip as well as content
- Random septapus comic posting
- Fix cry functionality from [original source](https://github.com/dead-bird/apcry/blob/master/api/cry.js) - just needs the math tweaking and adding swapping characters
- More dumb joke features
- Implement logging (only if needed)
