# D'Eagle

![DiscEagleGitHubBanner copy](https://user-images.githubusercontent.com/56032914/129584197-e56424dd-5d61-4ee9-bb98-1092d4d31fe6.png)

**The Discord Eagle (D'Eagle) is a Python (Scrapy + Discord.py) Amazon price checker that sends you a discord direct message when price decreases.**

The idea for this script came as I was avoiding to setup a SMTP server in order to get price warnings, so I decided to try to do it with a discord bot instead.

---
## Installation/Usage

1-  I suggest you create a new discord bot just for this script. You will have to allow "SERVER MEMBERS INTENT" for the bot to work.

> If you don't know how to do it / are interested in using my bot, feel free to contact me.

2-  Select the three specific variables before running the script:

> discordID - Discord id (from dev mode) that you want the bot to send the price drop warning;
>
> bot_token - Token required to log into your discord bot;
> 
> item_url - Amazon URL for the item you want to follow.

3- Run it with Python3.

> The bot will check the price every 12 hours if left permanently running. You will get a DM if the price has decreased and the bot will be disconnected.


## Citation

If, for some reason, you need/want to cite this software, please do it as per CITATION.cff:

> Martins, Frederico F. *D'Eagle*, v1.0.0, 2021, https://github.com/Frederico-F-Martins/D-Eagle, DOI: Zenodo

---
## Suggestions/Doubts

If you have any doubts/suggestions, you can reach me at fred.martins94@gmail.com.

## License

D'Eagle is available for free via a [MIT](https://choosealicense.com/licenses/mit/) license.
