import pandas as pd
import random

# Lists of possible app names
safe_apps = ["SBI Official", "HDFC Official", "PayTM", "GooglePay", "MyBankApp", "Axis Bank", "ICICI Bank"]
fake_apps = ["PaySafe", "QuickLoan", "FakeWallet", "LoanScam", "FraudPay", "MoneyFast", "MiniPay"]

data = []

# Generate 50 safe apps
for i in range(50):
    app_name = random.choice(safe_apps)
    package_name = "com." + app_name.lower().replace(" ", ".")
    has_bank_keyword = 1 if any(k in app_name.lower() for k in ["bank", "pay"]) else 0
    permissions_count = random.randint(10, 30)
    file_size_kb = random.randint(3000, 8000)
    has_sms_permission = 0
    has_camera_permission = random.choice([0, 1])
    label = "safe"
    data.append([app_name, package_name, has_bank_keyword, permissions_count,
                 file_size_kb, has_sms_permission, has_camera_permission, label])

# Generate 50 fake apps
for i in range(50):
    app_name = random.choice(fake_apps)
    package_name = "com." + app_name.lower().replace(" ", ".")
    has_bank_keyword = 1
    permissions_count = random.randint(35, 70)
    file_size_kb = random.randint(4000, 6000)
    has_sms_permission = 1
    has_camera_permission = 1
    label = "fake"
    data.append([app_name, package_name, has_bank_keyword, permissions_count,
                 file_size_kb, has_sms_permission, has_camera_permission, label])

# Shuffle data
random.shuffle(data)

# Columns
columns = ["app_name", "package_name", "has_bank_keyword", "permissions_count",
           "file_size_kb", "has_sms_permission", "has_camera_permission", "label"]

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Save CSV
df.to_csv("dataset.csv", index=False)
print("50 safe + 50 fake dummy dataset.csv created successfully!")
