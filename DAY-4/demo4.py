'''
CosTools Indus 

Products is bought from vendors, the there is vendor enrollment (once), billing process - product, Qty, Cost then maintain vendor records
using vendor_prods.log with updated date and time as well, vendor can be initialised with vendor name , gst, etc.
'''
from datetime import datetime

LOG_FILE = "vendor_prods.log"


class Vendor:
    def __init__(self, vName, vGst):
        self.vName = vName
        self.vGst = vGst
        print(f"Vendor initialized: {self.vName}, GST: {self.vGst}")

    def display(self):
        print(f"Vendor Name: {self.vName}")
        print(f"GST: {self.vGst}")

    def billing(self, pName, pQty, pCost):
        self.pName = pName
        self.pQty = pQty
        self.pCost = pCost
        self.tax = 0.18
        total = pQty * pCost
        total_with_tax = total * (1 + self.tax)
        print(f"Billing - Product: {pName}, Quantity: {pQty}, Cost: {pCost}, Total: {total}, Total with Tax: {total_with_tax}")

        with open(LOG_FILE, "a") as log_file:
            log_file.write(
                f"{datetime.now().ctime():<24} | {self.vName:<15} | {pName:<12} | "
                f"{pQty:>5} | {pCost:>10} | {total:>12} | {total_with_tax:>12.2f}\n"
            )


# Write table header once
with open(LOG_FILE, "w") as log_file:
    log_file.write(
        f"{'Date/Time':<24} | {'Vendor':<15} | {'Product':<12} | "
        f"{'Qty':>5} | {'Cost':>10} | {'Total':>12} | {'Total+Tax':>12}\n"
    )
    log_file.write("-" * 100 + "\n")

# Create vendors
vendor1 = Vendor("ABC Supplies", "GST1234")
vendor2 = Vendor("XYZ Traders", "GST5678")

vendor1.display()
vendor1.billing("Laptop", 2, 50000)

vendor2.display()
vendor2.billing("Mouse", 10, 500)

