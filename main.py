import yfinance as yf
import requests
import os
import random

def send_telegram_msg(message):
    token = os.getenv("TG_TOKEN")
    chat_id = os.getenv("TG_CHAT_ID")
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url)

# 隨機挑選一個想監控的台股代碼 (例如：台積電、聯發科、長榮)
stock_list = ["2330.TW", "2454.TW", "2603.TW", "0050.TW"]
target_stock = random.choice(stock_list)

try:
    stock = yf.Ticker(target_stock)
    # 取得最新成交價
    price = stock.fast_info['last_price']
    stock_name = stock.info.get('shortName', target_stock)
    
    msg = f"📈 股票通報\n個股：{stock_name} ({target_stock})\n現價：{price:.2f}"
    send_telegram_msg(msg)
    print(f"Success: {target_stock} price sent.")
except Exception as e:
    print(f"Error: {e}")
