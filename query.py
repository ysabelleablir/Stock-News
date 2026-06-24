import sqlalchemy as db
import pandas as pd
from getstockapi import df



def user_req(tick):
    engine = db.create_engine('sqlite:///data_base_name.db')

    df.to_sql('tickers',con=engine,if_exists='replace',index=False)
    
    with engine.connect() as connection:
        query_result = connection.execute(db.text(f"SELECT * FROM tickers where symbol='{tick}';")).fetchall()
        return pd.DataFrame(query_result)

print(user_req('NOK'))