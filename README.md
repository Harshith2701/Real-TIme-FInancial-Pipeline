# Real-Time Financial Market Data Pipeline

A robust data engineering pipeline that processes real-time stock market data using Apache Kafka for streaming and PostgreSQL for storage. This project demonstrates the implementation of a scalable, real-time data processing system with financial market data.

## Architecture Overview
```
Producer (Yahoo Finance) → Kafka → Consumer → PostgreSQL → Analytics
```

## Features
- Real-time stock data streaming from Yahoo Finance API
- Message queuing with Apache Kafka
- Persistent storage in PostgreSQL
- Real-time market analytics including:
  - Price tracking
  - Volume analysis
  - Moving averages
  - Market statistics

## Tech Stack
- **Python**: Primary programming language
- **Apache Kafka**: Message streaming platform
- **PostgreSQL**: Data storage
- **Docker**: Containerization
- **SQLAlchemy**: Database ORM

## Project Structure
```
.
├── docker/
│   ├── docker-compose.yml    # Docker services configuration
├── src/
│   ├── streaming/
│   │   ├── producer.py       # Data ingestion from Yahoo Finance
│   │   └── consumer.py       # Kafka consumer and data storage
│   └── utils/
│       └── database.py       # Database connection utilities
```

## Prerequisites
- Docker and Docker Compose
- Python 3.9+
- PostgreSQL
- Apache Kafka

## Setup and Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/Real-Time-Financial-Pipeline.git
cd Real-Time-Financial-Pipeline
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Start Docker containers
```bash
docker-compose -f docker/docker-compose.yml up -d
```

5. Initialize database
```sql
CREATE TABLE stock_prices (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(10) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    volume BIGINT NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    change_percent DECIMAL(10,2)
);
```

## Running the Pipeline

1. Start the producer:
```bash
python src/streaming/producer.py
```

2. Start the consumer:
```bash
python src/streaming/consumer.py
```

## Monitoring

You can monitor the pipeline through:
- Kafka messages using Kafka CLI tools
- PostgreSQL queries for stored data
- Real-time analytics output

## Data Flow
1. Producer fetches real-time stock data (AAPL, GOOGL, MSFT)
2. Data is streamed through Kafka topics
3. Consumer processes messages and stores in PostgreSQL
4. Analytics are computed on stored data

## Future Enhancements
- Add more stock symbols
- Implement advanced analytics
- Add real-time dashboarding
- Implement alerting system

## Contributing
Feel free to fork the project and submit PRs for any improvements.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
