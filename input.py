from news import Search
from GeminiAPI import Gemini
from query import user_req
banner = """********   **                    **           ****     **                           
 **//////   /**                   /**          /**/**   /**                           
/**        ******  ******   ***** /**  **      /**//**  /**  *****  ***     **  ******
/*********///**/  **////** **///**/** **  *****/** //** /** **///**//**  * /** **//// 
////////**  /**  /**   /**/**  // /****  ///// /**  //**/**/******* /** ***/**//***** 
       /**  /**  /**   /**/**   **/**/**       /**   //****/**////  /****/**** /////**
 ********   //** //****** //***** /**//**      /**    //***//****** ***/ ///** ****** 
////////     //   //////   /////  //  //       //      ///  ////// ///    /// //////  """

choice = '0'
while choice != 'q':
    print(banner)
    choice = input("Please enter search preference by number or 'q' to quit.\n" +
        "(1) Get semantic stock analysis by inputting ticker symbol\n" +
        "(2) Input ticker symbol to get OHLCV for that ticker\n"
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
            statement = []
            if len(urls) != 0:
                for num, title in enumerate(titles, start=1):
                    statement.append(f"{num}. {title} - {urls[num - 1]}\n")
                statement = "\n".join(statement)
            else:
                statement = "None found."
            print(statement)

            response = Gemini.ask_gemini(ticker_data, statement)
        case '2':
            ticker = input("Enter the stock ticker: ").upper().strip()
            print(f"Getting OHLCV market data on {ticker}...")
            ticker_data = user_req(ticker)
            print(ticker_data)
            response = "Ticker data displayed above."
        case 'q':
            print("Exiting program.")
            exit()
        case _:
            print(f"Invalid input of \"{choice}\". Please try again.")
            continue
    
    print("Prediction:")
    print(response)