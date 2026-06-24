from news import Search
from GeminiAPI import Gemini

choice = '0'
while choice != 'q':
    choice = input("Please enter search preference by number or 'q' to quit.\n" +
        "(1) Search by ticker\n" +
        "Enter choice: ").strip()
    match choice:
        case '1':
            ticker = input("Enter the stock ticker: ").upper().strip()
            # TODO: obtain information from database
            titles, urls = Search.obtain_articles("ticker", ticker)
        case 'q':
            print("Exiting program.")
            exit()
        case _:
            print(f"Invalid input of \"{choice}\". Please try again.")
            continue
    
    
    # TODO: print response from Gemini
    response = Gemini.ask_gemini(ticker, articles)
    print (response)