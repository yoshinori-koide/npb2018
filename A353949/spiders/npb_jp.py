from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem


class NpbJp(BasePortiaSpider):
    name = "npb.jp"
    allowed_domains = [u'npb.jp']
    start_urls = [u'http://npb.jp/games/2018/schedule_03_detail.html']
    rules = [
        Rule(
            LinkExtractor(
                allow=(
                    u'/scores/2018/\\d+/\\w\\-\\w\\-\\d\\d/$',
                    u'.*/schedule_\\d+_detail.html'),
                deny=()),
            callback='parse_item',
            follow=True)]
    items = [
        [
            Item(
                PortiaItem,
                None,
                u'#game_stats',
                [
                    Field(
                        u'GameDay',
                        '.game_tit > time *::text',
                        [],
                        True),
                    Field(
                        u'VisitorTeam',
                        '.line-score > div > table > .top > th > span *::text, .line-score > div > table > tbody > .top > th > span *::text',
                        []),
                    Field(
                        u'VisitorScore',
                        '.line-score > div > table > .top > .total-1 *::text, .line-score > div > table > tbody > .top > .total-1 *::text',
                        []),
                    Field(
                        u'HomeTeam',
                        '.line-score > div > table > .bottom > th > span *::text, .line-score > div > table > tbody > .bottom > th > span *::text',
                        []),
                    Field(
                        u'HomeScore',
                        '.line-score > div > table > .bottom > .total-1 *::text, .line-score > div > table > tbody > .bottom > .total-1 *::text',
                        [])])]]
