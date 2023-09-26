from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from plaza.items import PlazaItem, PlazaItem2 #add interpreter path (plaza folder)


class CplazaSpider(CrawlSpider):
    name = "cplaza"
    allowed_domains = ["gooshiplaza.com"]
    start_urls = ["https://gooshiplaza.com"]

    rules = [
        #rule for products' feature except existent
        Rule(LinkExtractor(allow=('product/')), callback='parse_items', follow=True, cb_kwargs={'type': '-Existent'}),
        # rule for products' feature include existent
        Rule(LinkExtractor(allow=('product-category/')), callback='parse_category', follow=True,
             cb_kwargs={'type': 'Existent'})
    ]

    def parse_items(self, response, type):
        '''
        crawl product page for finding products features except existent
        :param response:
        :return: items
        '''

        title = response.xpath("//h1//text()").get()
        price = response.xpath("//p[@class='price']/span/bdi//text()").get()
        # previousPrice = response.xpath()#there was no product with previous price
        originalImage = response.xpath("//div[@class='product-image-wrap']//a/@href").get()
        galleryImage = response.xpath("//div[@class='product-image-wrap']//a/@href").getall()
        description = response.xpath("//div[@id='tab-description']//text()").getall()
        url = response.url
        guaranty = response.xpath("//select[@id='pa_guarantee']//option//text()").getall()[1:]
        # same as guaranty in field guaranty some options has register in their text but independently there was no register field
        register = response.xpath("//select[@id='pa_guarantee']//option//text()").getall()[1:]

        # specifications that has some tables
        table_data = []
        rows = response.xpath('//table[@class="woocommerce-product-attributes shop_attributes"]/tr')
        for row in rows:
            cell1 = row.xpath('th/span//text()').get()
            if cell1 is not None:
                cell1 = cell1.replace('\n', '').replace('\t', '')
            cell2 = row.xpath('td/p//text()').get()
            if cell2 is not None:
                cell2 = cell2.replace('\n', '').replace('\t', '')
            table_data.append({cell1: cell2})
        # Create a JSON object for specifications
        specifications = {'table_data': table_data}

        #define items
        items = PlazaItem()

        items['title'] = title
        items['price'] = price
        items['originalImage'] = originalImage
        items['galleryImage'] = galleryImage
        items['description'] = description
        items['url'] = url
        items['register'] = register
        items['guaranty'] = guaranty
        items['specifications'] = specifications


        return items

    def parse_category(self, response):
        '''
        crawl category pages for finding existent
        :param response:
        :return: items
        '''
        existent = response.xpath('//div[@class="product-wrapper"]/div[2]/p//text()').get()

        #define items
        items = PlazaItem2()

        items['existent'] = existent

        return items

