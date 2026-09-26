# Gas Leakage Detector using Python

def gas_leakage_detector(gas_level):
print("\n===== GAS LEAKAGE DETECTOR =====")
print(f"Gas Sensor Level: {gas_level}")

```
if gas_level >= 70:
    print("⚠️ GAS LEAKAGE DETECTED!")
    print("Alarm: ON")
    print("Status: DANGER")

elif gas_level >= 40:
    print("Warning: Gas level is increasing.")
    print("Status: CHECK IMMEDIATELY")

else:
    print("Status: SAFE")
    print("No gas leakage detected.")
```

while True:
print("\n1. Check Gas Level")
print("2. Exit")

```
choice = input("Enter your choice: ")

if choice == "1":
    try:
        gas_level = float(
            input("Enter gas sensor level (0-100): ")
        )

        if 0 <= gas_level <= 100:
            gas_leakage_detector(gas_level)
        else:
            print("Please enter a value between 0 and 100.")

    except ValueError:
        print("Invalid input! Enter a number.")

elif choice == "2":
    print("Gas Leakage Detector Closed.")
    break

else:
    print("Invalid choice! Please try again.")
```
