def is_blacklisted(key, text):
    words = text.split()
    limit = THRESHOLD * len(words)
    for w in words:
        if w in STOCK_SYMBOLS:
           limit -=1

        if limit == 0 or limit < 0:
            yield key
