# PCY‑Algo

**PCY‑Algo** is an efficient, lightweight Python implementation of the **PCY (Park–Chen–Yu)** algorithm for **association rule mining**.

![PyPI - Version](https://img.shields.io/pypi/v/pcy-algo)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pcy-algo)
![License](https://img.shields.io/pypi/l/pcy-algo)

---

## 🚀 Features

- Implements the **PCY algorithm** to mine frequent itemsets from transaction data efficiently.
- Optimized with hashing and bitmap techniques to reduce memory usage.
- Compatible with **Python ≥ 3.6**.
- Lightweight and easy to integrate.

---

## 📦 Installation

Install the latest stable version via PyPI:

```bash
pip install pcy-algo
```
```bash
from pcy_algo import pcy_algo

# Sample transactions
num_transactions = [
    [12, 1, 2, 3, 4],
    [2, 3, 49, 45, 12],
    [12, 98, 45, 22]
]

# All unique items
unique_items = (12, 1, 2, 3, 4, 49, 45, 98, 22)

# Define parameters
bucket_size = 40
support = 500
confidence = 30

# Run PCY
basket = pcy_algo(num_transactions, unique_items, bucket_size, support, confidence)
result = basket.mine_data()

print(result)
```
# Usage Overview
- num_transactions: A list of baskets, where each basket is a list of item IDs (integers).

- unique_items: A tuple of all distinct item IDs.

- bucket_size: Number of buckets for hashing item pairs.

- support: Minimum support threshold (absolute count).

- confidence: Minimum confidence threshold (percentage).
