# Torn Discord Bot Framework
This is an example Torn.com for beginners to use as a baseline to build off. Find an installation guide on how to get started and more.

# Prerequisites
- Code Editor (IDE) such as [Pycharm Community](https://www.jetbrains.com/products/compare/?product=pycharm&product=pycharm-ce) or [VSCode](https://code.visualstudio.com/download)
- [Python3.10](https://www.python.org/downloads/) or newer
- [Py-Cord](https://pypi.org/project/py-cord/) or [Discord.py](https://pypi.org/project/discord.py/) (Install using CMD / Terminal)
- [Limited Access API Key](https://www.torn.com/preferences.php#tab=api)

  ## Bot Application
  Create a new [Discord Application](https://discordapp.com/developers/applications/)  [IMG](https://cdn.no1irishstig.co.uk/9kmu3.png)
   1. Go to the Bot tab, and enable: Presence Intent, Server Members Intent, Message Content Intent and Save Changes  [IMG](https://cdn.no1irishstig.co.uk/d0o2e.png)
   2. Then click 'Reset Token' which will generate a bot Token, copy this into a notepad for now - **Do not share your Bot Token with ANYONE**
 
# Installation

1. Download the [Bot Files](https://github.com/No1IrishStig/Torn-Example/archive/refs/heads/main.zip)
2. Unzip the folder and open in your IDE of choice
3. Paste your Bot Token & API Key inside quotations inside the `Utilities/config.json` file
4. Using terminal, navigate to the folder and execute the bot script `(python3 main.py, py main.py, py3 main.py)`
5. Alternatively, you can run the file by double clicking main.py on Windows

# Further Development
- For Python support, use [LearnPython](https://www.learnpython.org/), [W3Schools](https://www.w3schools.com/python/), [ChatGPT](https://chat.openai.com/), [Python Discord](https://discord.com/invite/python), or message me on Torn
- You can use the Pycord [API Reference](https://docs.pycord.dev/en/stable/api/events.html) for Pycord help, they also have a [Discord Server](https://discord.com/invite/pycord)
- For Torn API Support, use the [Community made TornAPI Documentation]() or the [TornAPI Discord]()

# Hosting
- I'd recommend self hosting, whether that be on your own computer, or by renting out a linux server for a few $$ a month.
- I personally use [Hetzner](https://www.hetzner.com/cloud/) and host my own bots by creating servers with them
- I use [GNU Screen](https://www.gnu.org/software/screen/manual/screen.html) with [MySQL](https://www.mysql.com/) and [MongoDB](https://www.mongodb.com/) Databases for persistent storage
