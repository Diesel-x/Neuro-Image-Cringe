from icrawler.builtin import GoogleImageCrawler, GreedyImageCrawler, BaiduImageCrawler, BingImageCrawler

# Парсинг изображений для класса Sonic
bing_crawler = BingImageCrawler(downloader_threads=4,
                                storage={'root_dir': 'Sonic'})
bing_crawler.crawl(keyword='Sonic The Hedgehog', filters=None, offset=1, max_num=1000)

# Парсинг изображений для класса Shadow
bing_crawler = BingImageCrawler(downloader_threads=4,
                                storage={'root_dir': 'Shadow'})
bing_crawler.crawl(keyword='Shadow The Hedgehog', filters=None, offset=1, max_num=1000)

# Парсинг изображений для класса Non Sonic & Shadow
bing_crawler = BingImageCrawler(downloader_threads=6,
                                storage={'root_dir': 'Non Sonic and Shadow'})

bing_crawler.crawl(keyword='Amy Rose', filters=None, file_idx_offset=0, max_num=500)
bing_crawler.crawl(keyword='knuckles The Echidna', filters=None, file_idx_offset='auto', max_num=500)
bing_crawler.crawl(keyword='Goku', filters=None, file_idx_offset='auto', max_num=500)
bing_crawler.crawl(keyword='Super Sayan', filters=None, file_idx_offset='auto', max_num=500)
bing_crawler.crawl(keyword='Pokemons', filters=None, file_idx_offset='auto', max_num=500)
bing_crawler.crawl(keyword='Blue Pokemon', filters=None, file_idx_offset='auto', max_num=500)
bing_crawler.crawl(keyword='Black Pokemon', filters=None, file_idx_offset='auto', max_num=500)
bing_crawler.crawl(keyword='Silver The hedgehog', filters=None, file_idx_offset='auto', max_num=500)
bing_crawler.crawl(keyword='Tails The Fox', filters=None, file_idx_offset='auto', max_num=500)
bing_crawler.crawl(keyword='People', filters=None, file_idx_offset='auto', max_num=500)
bing_crawler.crawl(keyword='Man', filters=None, file_idx_offset='auto', max_num=500)