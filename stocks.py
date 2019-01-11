# A block of publicly traded stock has a variety of attributes. Let's look at a few of them. A stock has a ticker symbol and a company name. Create a simple dictionary with ticker symbols and company names.

stockDictionary = {"AZ": "Austin Corp",
 "BB": "Big Buisness",
  "TLG": "The Little Guys",
  "GE": "General Electric"}

# Create a simple list of blocks of stock. These could be tuples with ticker symbols, number of shares, dates and price.

purchases = [ ("AZ", 52, "29-jul-1992", 26), 
("BB", 110, "1-sep-2015", 500), 
("TLG", 75, "18-nov-2017", 100),
('GE', 100, '10-sep-2001', 48),
('GE', 200, '1-jul-1998', 56)
]

# Create a purchase history report that computes the full purchase price (shares times dollars) for each block of stock and uses the stockDict to look up the full company name. This is the basic relational database join algorithm between two tables.
# for stocks in stockDictionary:


# my way
for purchase in purchases:
  for initial, name in stockDictionary.items():
    purchase_int = purchase[0]
    price = purchase[1]*purchase[3]
    if initial == purchase_int:
      print(("I purchased {0} stock for ${1}").format(name, price))

# class way
report = {}
for purchase in purchases:
  purchase_abrev = purchase[0]
  full_name = stockDictionary[purchase_abrev]
  no_of_shares = purchase[1]
  purch_date = purchase[2]
  purch_price = purchase[3]
  full_price = no_of_shares*purch_price
  print(f"I purchased {full_name} stock on {purch_date} for ${full_price}")


# Create a second purchase summary that which accumulates total investment by ticker symbol. In the above sample data, there are two blocks of GE. These can easily be combined by creating a dict where the key is the ticker and the value is the list of blocks purchased. The program makes one pass through the data to create the dict. A pass through the dict can then create a report showing each ticker symbol and all blocks of stock.
  
  try: 
   report[purchase_abrev].append(purchase)
  except KeyError:
   report[purchase_abrev] = list()
   report[purchase_abrev].append(purchase)

for abbrev, purchases_list in report.items():
  print(f"               ------{abbrev}-------")
  total_port_stock_val = 0
  for purchase in purchases_list:
    total_port_stock_val += purchase[1] * purchase[3]
    print(f"         {purchase}")
  print(f"     Total Value of Stock in porfolio: ${total_port_stock_val}\n\n")
      