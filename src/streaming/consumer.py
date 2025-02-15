from kafka import KafkaConsumer
import json
from datetime import datetime
from src.utils.database import StockPrice, init_db

class StockDataConsumer:
    def __init__(self):
        self.consumer = KafkaConsumer(
            'stock_data',
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='latest',
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
        self.db_session = init_db()

    def store_stock_data(self, symbol, price, volume, change_percent):
        """Store stock data in PostgreSQL"""
        stock_data = StockPrice(
            symbol=symbol,
            price=price,
            volume=volume,
            change_percent=change_percent
        )
        self.db_session.add(stock_data)
        try:
            self.db_session.commit()
            print(f"Data stored in database for {symbol}")
        except Exception as e:
            self.db_session.rollback()
            print(f"Error storing data: {str(e)}")

    def start_consuming(self):
        print("Starting to consume stock data...")
        try:
            for message in self.consumer:
                data = message.value
                symbol = data['symbol']
                quote = data['data']
                timestamp = datetime.fromtimestamp(data['timestamp'])
                
                # Extract values from new Yahoo Finance format
                current_price = float(quote['price'])
                volume = int(quote['volume'])
                change_percent = float(quote['change'])
                
                # Store in database
                self.store_stock_data(symbol, current_price, volume, change_percent)
                
                # Print analysis
                print(f"\n{'='*50}")
                print(f"Stock Update at {timestamp}")
                print(f"Symbol: {symbol}")
                print(f"Current Price: ${current_price:.2f}")
                print(f"Change: {change_percent:.2f}%")
                print(f"Volume: {volume:,}")
                print(f"{'='*50}")

        except KeyboardInterrupt:
            print("\nStopping consumer...")
            self.db_session.close()
            self.consumer.close()

if __name__ == "__main__":
    consumer = StockDataConsumer()
    consumer.start_consuming()