def convert_currency(amount_idr, exchange_rates):
    usd_rate, euro_rate, yen_rate = exchange_rates
    usd = amount_idr / usd_rate
    euro = amount_idr / euro_rate
    yen = amount_idr / yen_rate
    return usd, euro, yen

exchange_rates = (15000, 16000, 120)

while True:
    try:
        amount_idr = float(input("Enter the amount in Indonesian Rupiah (IDR): "))
        usd, euro, yen = convert_currency(amount_idr, exchange_rates)
        print(f"{amount_idr} IDR is approximately:")
        print(f"{usd} USD")
        print(f"{euro} EUR")
        print(f"{yen} JPY")
        break
    except ValueError:
        print("Invalid input. Please enter a valid number for the amount.")
