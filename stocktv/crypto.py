from .utils import StockTVAPI

class CryptoAPI(StockTVAPI):
    def get_coin_info(self):
        endpoint = "crypto/getCoinInfo"
        return self._get(endpoint)

    def get_coin_list(self, start=1, limit=1000):
        endpoint = "crypto/getCoinList"
        params = {
            "start": start,
            "limit": limit
        }
        return self._get(endpoint, params)

    def get_ticker_price(self, symbols):
        endpoint = "crypto/tickerPrice"
        params = {
            "symbols": symbols
        }
        return self._get(endpoint, params)

    def get_last_price(self, symbols):
        endpoint = "crypto/lastPrice"
        params = {
            "symbols": symbols
        }
        return self._get(endpoint, params)

    def get_klines(self, symbol, interval):
        endpoint = "crypto/getKlines"
        params = {
            "symbol": symbol,
            "interval": interval
        }
        return self._get(endpoint, params)

    def get_trades(self, symbol):
        endpoint = "crypto/getTrades"
        params = {
            "symbol": symbol
        }
        return self._get(endpoint, params)