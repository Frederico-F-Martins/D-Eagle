########################################################
##                                                    ##
##                    D'Eagle v1.0                    ##
##     Copyright (c) 2021 Frederico F. Martins        ##
##                    -------------                   ##
##                    @FredFMartins                   ##
##                    -------------                   ##
##                                                    ##
########################################################

from discord import user, utils, client
import scrapy
from scrapy.crawler import CrawlerProcess
import discord
import time

#Input required
discordID = 'Your Discord ID here'
bot_token = 'Your bot token here'
item_url = 'URL for the item you want to follow'

#### ~~~ Scrapy Spidey gets info from Amazon ~~~ ####

class AmazonSpider (scrapy.Spider):
    name = 'AmazonSpider'
    start_urls = [item_url]

    def parse(self, response):
        product_title = response.xpath('.//*[@id="productTitle"]/text()').get()
        starting_price = response.xpath('.//*[@id="priceblock_ourprice"]/text()').get()
        starting_price = starting_price.replace(",", ".")
        sprice=float(starting_price[:-2])
        time.sleep(3)
        latest_price = response.xpath('.//*[@id="priceblock_ourprice"]/text()').get()
        latest_price = starting_price.replace(",", ".")
        lprice=float(latest_price[:-2])

#### ~~~ Check if the price has changed every 12h and maintain loop if it hasn't ~~~ ####

        while lprice >= sprice:
            time.sleep(43200)
            latest_price = response.xpath('.//*[@id="priceblock_ourprice"]/text()').get()
            latest_price = latest_price.replace(",", ".")
            lprice=float(latest_price[:-2])
        else:

#### ~~~ Connect to discord to send message ~~~ ####

            intents = discord.Intents.default()
            intents.members = True

            client = discord.Client(intents=intents)

            @client.event

            async def on_ready():
                print('We have logged in as {0.user}'.format(client))
                user = client.get_user(int(discordID))
                await user.send("Your item: **{pt}**\n is currently priced at **{price}**\n\n Please restart me if you want to keep tracking the price.".format(pt = product_title, price = latest_price))
                await client.logout()

            client.run(bot_token)


if __name__ == "__main__":
  process = CrawlerProcess()
  process.crawl(AmazonSpider)
  process.start()