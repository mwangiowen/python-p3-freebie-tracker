#!/usr/bin/env python3
import ipdb
from sqlalchemy import create_engine

from models import Company, Dev

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    ipdb.set_trace()

    # session = Session()
    # session.query(Company).all()
    # session.query(Dev).all()
    # session.close()