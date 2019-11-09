from apyori import apriori

#from apyori import load_transactions

transactions = [
    ['1', '2','3','4','5','6'],
    ['beer', 'cheese'],
]
result = list(apriori(transactions,
        min_support=0.02,
        min_confidence=0.80,
        min_lift=1.0,
        max_length=None))


