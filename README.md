# reasleMail
This code searches multiple websites, compares item prices, and sends us an email to purchase it.


0. Resister URLs of websites for purchasing stores and reselling stores.
1. Ask users to enter item names.
2. Search the item in all of the websites.
3. Collect the price data of the item from each websites.
   → Difficulties :
     ・It is difficult to accurately specify the price display position, as it varies depending on the product, the website and maybe the time.
   　　　　・The searching function of the websites doesn't work well when you enter an abbreviated name. (for example: × iphone16pro max　→　○ iphone 16 　　      pro max)
４. Compare them.
５. If the price in one of the reselling stores is higher than the price in one of the purchasing stores (or its 0.99 times), this code sends us an e-mail.
