"""
Starter code for Python Automation with CSV File I/O.

This script provides helper functions for reading and writing inventory data,
backing up files, and generating a summary report.
"""

import csv
import shutil
from pathlib import Path
from typing import List, Dict

DATA_DIR = Path(__file__).parent
INPUT_FILE = DATA_DIR / "inventory.csv"
BACKUP_FILE = DATA_DIR / "inventory_backup.csv"
UPDATED_FILE = DATA_DIR / "inventory_updated.csv"
REPORT_FILE = DATA_DIR / "inventory_report.txt"


def load_inventory(file_path: Path) -> List[Dict[str, str]]:
    """Load inventory rows from a CSV file."""
    with file_path.open("r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def save_inventory(file_path: Path, rows: List[Dict[str, str]], fieldnames: List[str]) -> None:
    """Save inventory rows to a CSV file."""
    with file_path.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def backup_file(source: Path, destination: Path) -> None:
    """Create a backup copy of the source file."""
    shutil.copy(source, destination)


def generate_report(rows: List[Dict[str, str]], report_path: Path) -> None:
    """Generate a text report from inventory data."""
    total_items = sum(int(row["quantity"]) for row in rows)
    total_value = sum(int(row["quantity"]) * float(row["price"]) for row in rows)
    low_stock = [row for row in rows if int(row["quantity"]) < 5]

    with report_path.open("w", encoding="utf-8") as report_file:
        report_file.write("Inventory Summary Report\n")
        report_file.write("========================\n")
        report_file.write(f"Total items in inventory: {total_items}\n")
        report_file.write(f"Total inventory value: ${total_value:.2f}\n")
        report_file.write("Low stock products:\n")
        for item in low_stock:
            report_file.write(f"- {item['name']} (quantity: {item['quantity']})\n")


def add_product(rows: List[Dict[str, str]], product: Dict[str, str]) -> None:
    """Add a new product row to the inventory."""
    rows.append(product)


def update_quantity(rows: List[Dict[str, str]], product_id: str, new_quantity: int) -> bool:
    """Update the quantity for a product by ID."""
    for row in rows:
        if row["id"] == product_id:
            row["quantity"] = str(new_quantity)
            return True
    return False


def main() -> None:
    inventory = load_inventory(INPUT_FILE)
    print(f"Loaded {len(inventory)} inventory records.")

    backup_file(INPUT_FILE, BACKUP_FILE)
    print(f"Backup created: {BACKUP_FILE.name}")

    new_product = {
        "id": "6",
        "name": "Desk Lamp",
        "category": "Office",
        "quantity": "10",
        "price": "22.50"
    }
    add_product(inventory, new_product)

    updated = update_quantity(inventory, "2", 8)
    if updated:
        print("Updated quantity for product ID 2.")
    else:
        print("Product ID 2 not found.")

    fieldnames = ["id", "name", "category", "quantity", "price"]
    save_inventory(UPDATED_FILE, inventory, fieldnames)
    print(f"Updated inventory saved: {UPDATED_FILE.name}")

    generate_report(inventory, REPORT_FILE)
    print(f"Report generated: {REPORT_FILE.name}")


if __name__ == "__main__":
    main()
