from news import Search
from GeminiAPI import Gemini
from query import user_req

choice = '0'
while choice != 'q':
    choice = input("Please enter search preference by number or 'q' to quit.\n" +
        "(1) Search by ticker\n" +
        "Enter choice: ").strip()
    titles = []
    urls = []
    match choice:
        case '1':
            ticker = input("Enter the stock ticker: ").upper().strip()

            print(f"Getting OHLCV market data on {ticker}...")
            ticker_data = user_req(ticker)

            print("Obtaining articles...")
            titles, urls = Search.obtain_articles("ticker", ticker)
            for num, title in enumerate(titles, start=1):
                print(f"{num}. {title} - {urls[num - 1]}")

            print("Generating response...")
            response = Gemini.ask_gemini(ticker_data, urls)
        case 'q':
            print("Exiting program.")
            exit()
        case _:
            print(f"Invalid input of \"{choice}\". Please try again.")
            continue
    
    print("Prediction:")
    print(response)