import requests

class StockTVAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.stocktv.top"

    def _get(self, endpoint, params=None):
        if params is None:
            params = {}
        params['key'] = self.api_key
        response = requests.get(f"{self.base_url}/{endpoint}", params=params)
        response.raise_for_status()
        return response.json()

    def _ws_connect(self, endpoint):
        import websocket
        ws_url = f"wss://ws-api.stocktv.top/{endpoint}?key={self.api_key}"
        ws = websocket.create_connection(ws_url)
        return ws