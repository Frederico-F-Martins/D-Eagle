# D'Eagle

![DiscEagleGitHubBanner copy](https://user-images.githubusercontent.com/56032914/129584197-e56424dd-5d61-4ee9-bb98-1092d4d31fe6.png)

![GitHub release (latest by date)](https://img.shields.io/github/v/release/Frederico-F-Martins/D-Eagle)
![GitHub](https://img.shields.io/github/license/Frederico-F-Martins/D-Eagle)
[![DOI](https://zenodo.org/badge/396712984.svg)](https://zenodo.org/badge/latestdoi/396712984)


**The Discord Eagle (D'Eagle) is a Python (Scrapy + Discord.py) Amazon price checker that sends you a discord direct message when price decreases.**

The idea for this script came as I was avoiding to setup a SMTP server in order to get price warnings, so I decided to try to do it with a discord bot instead.


---
## Installation/Usage

1-  I suggest you create a new discord bot just for this script. You will have to allow "SERVER MEMBERS INTENT" for the bot to work.

> If you don't know how to do it / are interested in using my bot, feel free to contact me.

2-  Install the Scrapy and Discord.py libraries

> pip install scrapy
> 
> pip install discord.py

3-  Edit the script to input the three specific variables before running the script:

> discordID - Discord id (from dev mode) that you want the bot to send the price drop warning to;
>
> bot_token - Token required to log into your discord bot;
> 
> item_url - Amazon URL for the item you want to follow.

4- Run it with Python3.

> The bot will check the price every 12 hours if left permanently running. You will get a DM if the price has decreased and the bot will be disconnected.



## Citation

If, for some reason, you need/want to cite this software, please do it as per CITATION.cff:

> Martins, Frederico F. *D'Eagle - Discord Bot Amazon Price Checker*, v1.0.0, 2021, https://github.com/Frederico-F-Martins/D-Eagle, DOI: 10.5281/zenodo.5206819


---
## Suggestions/Doubts

If you have any doubts/suggestions, please open an issue in this repository.


## License

D'Eagle is available for free via a [MIT](https://choosealicense.com/licenses/mit/) license.
