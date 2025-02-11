from .utils import StockTVAPI

class ForexAPI(StockTVAPI):
    def get_currency_list(self):
        endpoint = "market/currencyList"
        return self._get(endpoint)

    def get_real_time_rates(self, country_type=None):
        endpoint = "market/currency"
        params = {
            "countryType": country_type
        }
        return self._get(endpoint, params)

    def get_today_market(self, symbol):
        endpoint = "market/todayMarket"
        params = {
            "symbol": symbol
        }
        return self._get(endpoint, params)

    def get_spark_data(self, symbol, interval="5m"):
        endpoint = "market/spark"
        params = {
            "symbol": symbol,
            "interval": interval
        }
        return self._get(endpoint, params)

    def get_chart_data(self, symbol, interval="5m", start_time=None, end_time=None):
        endpoint = "market/chart"
        params = {
            "symbol": symbol,
            "interval": interval,
            "startTime": start_time,
            "endTime": end_time
        }
        return self._get(endpoint, params)