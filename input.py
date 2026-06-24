from news import Search

choice = '0'
while choice != 'q':
    choice = input("Please enter search preference by number or 'q' to quit.\n" +
        "(1) Search by ticker\n" +
        "Enter choice: ").strip()
    match choice:
        case '1':
            ticker = input("Enter the stock ticker: ").upper().strip()
            # TODO: obtain information from database
            urls = Search.obtain_urls("ticker", ticker)
        case 'q':
            print("Exiting program.")
            exit()
        case _:
            print(f"Invalid input of \"{choice}\". Please try again.")
            continue
    
    # TODO: print response from Gemini