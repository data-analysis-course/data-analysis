import numpy as np

daily_orders = np.array([120, 135, 98, 160, 142, 110, 175], dtype=np.int32)

daily_revenue = np.array(
    [2400.50, 2700.00, 1960.75, 3200.25, 2840.00, 2200.50, 3500.00],
    dtype=np.float64
)

product_sales = np.array(
    [
        [25, 18, 31],
        [20, 24, 15],
        [32, 19, 27],
        [28, 22, 35]
    ],
    dtype=np.int32
)

print("Daily orders:", daily_orders)
print("Daily revenue:", daily_revenue)
print("Product sales:\n", product_sales)

# First arrays: 1D, 2D, 3D
one_dimensional = np.array([10, 20, 30, 40], dtype=np.int32)

two_dimensional = np.array(
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    dtype=np.int32
)

three_dimensional = np.zeros((2, 3, 4), dtype=np.float64)

print("\n1D array:", one_dimensional)
print("1D shape:", one_dimensional.shape)
print("1D dimensions:", one_dimensional.ndim)

print("\n2D array:\n", two_dimensional)
print("2D shape:", two_dimensional.shape)
print("2D dimensions:", two_dimensional.ndim)

print("\n3D shape:", three_dimensional.shape)
print("3D dimensions:", three_dimensional.ndim)

# Mini demo: vectorized operations
orders = np.array([120, 135, 98, 160, 142], dtype=np.int32)

print("\nOrders:", orders)
print("ndim:", orders.ndim)
print("shape:", orders.shape)
print("size:", orders.size)
print("dtype:", orders.dtype)
print("itemsize:", orders.itemsize)
print("nbytes:", orders.nbytes)

orders_with_growth = orders * 1.10

print("\nOrders with 10% growth:", orders_with_growth)
print("New dtype:", orders_with_growth.dtype)

high_order_days = orders[orders > 130]
print("Days above 130 orders:", high_order_days)

print("\nTotal orders:", orders.sum())
print("Average orders:", orders.mean())
print("Minimum:", orders.min())
print("Maximum:", orders.max())
