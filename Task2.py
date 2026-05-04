stocks = {
    "APPLE": 180,
    "TATA": 250,
    "GOOGLE": 140,
    "JIO": 300
}

total = 0

print("Enter stock details (type 'done' to finish):")

while True:
    name = input("Stock name: ").upper()
    if name == "DONE":
        break

    if name not in stocks:
        print("Stock not found!")
        continue

    qty = int(input("Quantity: "))
    value = stocks[name] * qty
    total += value

    print(f"{name} added. Value = {value}")

print("\nTotal Investment Value =", total)