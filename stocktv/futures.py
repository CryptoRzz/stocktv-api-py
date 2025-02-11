from .utils import StockTVAPI

class FuturesAPI(StockTVAPI):
    def get_futures_list(self):
        endpoint = "futures/list"
        return self._get(endpoint)

    def get_futures_market(self, symbol):
        endpoint = "futures/querySymbol"
        params = {
            "symbol": symbol
        }
        return self._get(endpoint, params)

    def get_futures_kline(self, symbol, interval):
        endpoint = "futures/kline"
        params = {
            "symbol": symbol,
            "interval": interval
        }
        return self._get(endpoint, params)