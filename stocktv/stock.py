from .utils import StockTVAPI

class StockAPI(StockTVAPI):
    def get_stock_list(self, country_id, page_size=10, page=1):
        endpoint = "stock/stocks"
        params = {
            "countryId": country_id,
            "pageSize": page_size,
            "page": page
        }
        return self._get(endpoint, params)

    def get_indices(self, country_id, flag=None):
        endpoint = "stock/indices"
        params = {
            "countryId": country_id,
            "flag": flag
        }
        return self._get(endpoint, params)

    def get_kline(self, pid, interval):
        endpoint = "stock/kline"
        params = {
            "pid": pid,
            "interval": interval
        }
        return self._get(endpoint, params)

    def get_ipo_calendar(self, country_id):
        endpoint = "stock/getIpo"
        params = {
            "countryId": country_id
        }
        return self._get(endpoint, params)

    def get_updown_list(self, country_id, type=1):
        endpoint = "stock/updownList"
        params = {
            "countryId": country_id,
            "type": type
        }
        return self._get(endpoint, params)

    def get_company_info(self, country_id, page_size=10, page=1):
        endpoint = "stock/companies"
        params = {
            "countryId": country_id,
            "pageSize": page_size,
            "page": page
        }
        return self._get(endpoint, params)

    def get_company_info_by_url(self, url):
        endpoint = "stock/companyUrl"
        params = {
            "url": url
        }
        return self._get(endpoint, params)

    def get_news(self, page_size=10, page=1):
        endpoint = "stock/news"
        params = {
            "pageSize": page_size,
            "page": page
        }
        return self._get(endpoint, params)

    def connect_websocket(self):
        return self._ws_connect("connect")