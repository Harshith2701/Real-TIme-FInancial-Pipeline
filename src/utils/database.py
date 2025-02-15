from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Create base class for declarative models
Base = declarative_base()

class StockPrice(Base):
    __tablename__ = 'stock_prices'
    
    id = Column(Integer, primary_key=True)
    symbol = Column(String)
    price = Column(Float)
    volume = Column(BigInteger)
    timestamp = Column(DateTime, default=datetime.utcnow)
    change_percent = Column(Float)

def init_db():
    # Create database connection
    DATABASE_URL = "postgresql://stockuser:stockpass@localhost:5432/stockdata"
    engine = create_engine(DATABASE_URL)
    
    # Create tables
    Base.metadata.create_all(engine)
    
    # Create session factory
    Session = sessionmaker(bind=engine)
    return Session()