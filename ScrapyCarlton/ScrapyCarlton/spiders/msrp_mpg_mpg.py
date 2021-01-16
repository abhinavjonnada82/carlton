import scrapy

class AutomotiveSpider(scrapy.Spider):
    name = "spider1"
    start_urls = [
        'https://www.toyota.com/camry/',
        # 'https://automobiles.honda.com/tools/build-and-price-result?model=&modelseries=accord-sedan&modelyear=2021&ef_id=1:1:1&CID=SEARCH_HRM_GOOGLE_EVERGREEN_MY21ACD_BRD&gclsrc=aw.ds&ds_rl=1062082&gclid=Cj0KCQiA0fr_BRDaARIsAABw4EvV986qMk069B-I_58wgOyqCmPKJVZ46VzedI7CdkqtxIiZbWFsliYaAufsEALw_wcB#section=Powertrain&group=Powertrain&view=Exterior&angle=0&state=TTpDVjFGMU1FVyRFQzpOSC03OTdNJEhDOnVuZGVmaW5lZCRJQzpCSyRPOiRGOkZJRlMkRUNDOkdZJEVDWDo=&payment=&paymentType=',
        # 'https://www.mazdausa.com/shopping-tools/build-and-price/2021-mazda6?semid=67732090549&providertag=MazdaSEM&servicetag=67732090549&k_keyword=mazda%206%20msrp&k_matchtype=e&gclsrc=aw.ds&&gclid=Cj0KCQiA0fr_BRDaARIsAABw4EvQ1AR9lwSzMkoqbF1sS23rlnH2U2PEkynIWSVTPCEvg3UcK0RJmpUaAqr5EALw_wcB#s=1&tr=Automatic&d=FWD&f=Gasoline&t=21M6GSP%7C21M6GSPA&ex=41W&in=C_GT7&p=&ip=&o=&io=',
        # 'https://',
        # 'https://',
        # 'https://',
        # 'https://',
    ]

    def parse(self, response):
        page = response.url.split('/')[-1]
        filename = 'spider1-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)





