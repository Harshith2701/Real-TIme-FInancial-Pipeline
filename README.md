# Real-Time Financial Data Pipeline

A real-time data engineering pipeline that processes live stock market data using Apache Kafka and PostgreSQL.

## Architecture
![Architecture Diagram](docs/architecture.png)

## Components
- **Data Producer**: Fetches real-time stock data
- **Apache Kafka**: Handles message queuing and streaming
- **Data Consumer**: Processes and stores data in PostgreSQL
- **Analytics**: Real-time market analysis and statistics

## Tech Stack
- Python
- Apache Kafka
- PostgreSQL
- Docker
- SQLAlchemy

## Setup and Installation
1. Clone the repository
```bash
git clone [your-repo-url]