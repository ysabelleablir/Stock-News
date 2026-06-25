import sqlalchemy as db
import pandas as pd
from getstockapi import engine


def user_req(tick):
    with engine.connect() as connection:
        query_result = connection.execute(db.text(f"SELECT * FROM tickers where symbol='{tick}';")).fetchall()
        return pd.DataFrame(query_result).to_csv(index=False)

print(user_req('TSLA'))
