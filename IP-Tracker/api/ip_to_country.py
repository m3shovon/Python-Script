import json
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

class IPToCountry:
    IP2COUNTRY_API_URL = 'https://api.ip2country.info/'

    def get_country_basic_info_from_ip(self, ip):
        """
        Returns the ISO country codes, name and emoji for the given IP
        """
        request_url = IPToCountry.IP2COUNTRY_API_URL + 'ip?' + ip
        try:
            response = urlopen(request_url)
            country_basic_info = json.loads(response.read())
            return country_basic_info
        except URLError as e:
            raise e
