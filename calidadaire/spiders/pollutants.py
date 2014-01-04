from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from calidadaire.items import PollutantsMeasure
import re


class PollutantsSpider(BaseSpider):
    name = "pollutants"
    allowed_domains = ["www.nl.gob.mx"]
    start_urls = [
        "http://www.nl.gob.mx/?P=sima_metropolitano&url=SistemaGubernamentales/sima/ReporteCrossPorHora.aspx&param1=st=1&param3=tp=1",
        "http://www.nl.gob.mx/?P=sima_metropolitano&url=SistemaGubernamentales/sima/ReporteCrossPorHora.aspx&param1=st=2&param3=tp=1",
        "http://www.nl.gob.mx/?P=sima_metropolitano&url=SistemaGubernamentales/sima/ReporteCrossPorHora.aspx&param1=st=3&param3=tp=1",
        "http://www.nl.gob.mx/?P=sima_metropolitano&url=SistemaGubernamentales/sima/ReporteCrossPorHora.aspx&param1=st=4&param3=tp=1",
        "http://www.nl.gob.mx/?P=sima_metropolitano&url=SistemaGubernamentales/sima/ReporteCrossPorHora.aspx&param1=st=5&param3=tp=1",
        "http://www.nl.gob.mx/?P=sima_metropolitano&url=SistemaGubernamentales/sima/ReporteCrossPorHora.aspx&param1=st=6&param3=tp=1",
        "http://www.nl.gob.mx/?P=sima_metropolitano&url=SistemaGubernamentales/sima/ReporteCrossPorHora.aspx&param1=st=7&param3=tp=1",
        "http://www.nl.gob.mx/?P=sima_metropolitano&url=SistemaGubernamentales/sima/ReporteCrossPorHora.aspx&param1=st=8&param3=tp=1",
        "http://www.nl.gob.mx/?P=sima_metropolitano&url=SistemaGubernamentales/sima/ReporteCrossPorHora.aspx&param1=st=11&param3=tp=1"
    ]

    def parse(self, response):
        sel = Selector(response)
        str_selector = '//table[@class="TablaDatos"]/tr[contains(@class, "itemStyle")]'
        def serialize(measure):
            item            = PollutantsMeasure()
            item['HOUR']    = measure.xpath('td[1]/text()').extract()[0]
            item['PM10']    = measure.xpath('td[2]/text()').extract()[0]
            item['O3']      = measure.xpath('td[3]/text()').extract()[0]
            item['NO2']     = measure.xpath('td[4]/text()').extract()[0]
            item['SO2']     = measure.xpath('td[5]/text()').extract()[0]
            item['CO']      = measure.xpath('td[6]/text()').extract()[0]
            item['PM25']    = measure.xpath('td[7]/text()').extract()[0]
            item['STATION'] = re.search('param1=st[^&]*',
                response.url).group()[10:]
            return item
        return map(serialize, sel.xpath(str_selector))
