# Lav et veksleprogram fra DKK til euro. Det skal påregne en kommission på 2%, dog mindst 0,5 euro.
dkkStr = input("Amount in DKK: ")
dkk = float(dkkStr)

# DKK per EURO
rate = 100 / 750 
euro = dkk * rate
commission_pct = 2.0

commission_euro = euro * commission_pct/100.0

minimum_commission_euro = 0.5 

if commission_euro < minimum_commission_euro:
  commission_euro = minimum_commission_euro
  
payout_euro = euro - commission_euro

print(f"Payout in euro: {payout_euro}")
