import requests
from agents import function_tool

@function_tool()
def get_crypto_price(symbol: str) -> str:
    """
    Get current market price of a cryptocurrency from Binance.
    Example: symbol='BTCUSDT'
    """
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol.upper()}"
    response = requests.get(url)

    try:
    
        if response.status_code == 200:
            data = response.json()
            return f"The current price of {symbol.upper()} is {data['price']} USD"
        else:
            return f"Failed to fetch price for {symbol.upper()}."
    except Exception as e:  
        return f"Error fetching price for {symbol.upper()}: {str(e)}"
    
# import aiohttp
# import asyncio
# from agents import function_tool

# @function_tool()
# async def get_crypto_price(symbol: str) -> str:
#     """
#     Get current market price of a cryptocurrency from Binance.
#     Example: symbol='BTCUSDT'
#     """
#     url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol.upper()}"
    
#     async with aiohttp.ClientSession() as session:
#         try:
#             async with session.get(url) as response:
#                 if response.status == 200:
#                     data = await response.json()
#                     return f"The current price of {symbol.upper()} is {data['price']} USD"
#                 else:
#                     return f"Failed to fetch price for {symbol.upper()}. Status: {response.status}"
#         except Exception as e:
#             return f"Error fetching price for {symbol.upper()}: {str(e)}"