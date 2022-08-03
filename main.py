from requests_html import HTMLSession


s = HTMLSession()

city = ('london').capitalize()
url = f'https://www.google.com/search?q=google+weather+{city}'


response = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 '
                                             '(KHTML, like Gecko) Version/15.5 Safari/605.1.15'})

temperature = response.html.find('span#wob_tm', first=True).text
description = response.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text

print(f'The temperature in {city} is: {temperature} °Celsius - {description}')
