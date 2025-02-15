import yfinance as yf
import json
import time
from kafka import KafkaProducer

class StockDataProducer:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=['localhost:9092'],
            value_serializer=lambda x: json.dumps(x).encode('utf-8')
        )

    def get_stock_data(self, symbol):
        """Fetch real-time stock data from Yahoo Finance"""
        try:
            stock = yf.Ticker(symbol)
            # Get real-time data using history
            hist = stock.history(period='1d')
            if not hist.empty:
                last_quote = hist.iloc[-1]
                data = {
                    'symbol': symbol,
                    'data': {
                        'price': float(last_quote['Close']),
                        'volume': int(last_quote['Volume']),
                        'change': float((last_quote['Close'] - hist.iloc[0]['Open']) / hist.iloc[0]['Open'] * 100)
                    },
                    'timestamp': time.time()
                }
                print(f"Fetched data for {symbol}: {data}")  # Debug print
                return data
                
        except Exception as e:
            print(f"Error fetching data for {symbol}: {str(e)}")
            return None

    def start_streaming(self, symbols=['AAPL', 'GOOGL', 'MSFT']):
        """Start streaming data for given symbols"""
        print("Starting stock data stream...")
        while True:
            for symbol in symbols:
                data = self.get_stock_data(symbol)
                if data:
                    try:
                        self.producer.send('stock_data', value=data)
                        print(f"Sent data for {symbol}")
                    except Exception as e:
                        print(f"Error sending data to Kafka: {str(e)}")
                time.sleep(2)  # Delay between symbols

if __name__ == "__main__":
    producer = StockDataProducer()
    producer.start_streaming()