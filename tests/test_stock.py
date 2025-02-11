from stocktv.stock import StockAPI

api_key = "your_api_key_here"
stock_api = StockAPI(api_key)

# Get stock list
stock_list = stock_api.get_stock_list(country_id=14)
print(stock_list)