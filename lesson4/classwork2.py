def add_item(cart: list[dict], name: str, price: float, qty: int = 1) -> None:
	for item in cart:
		if item["name"] == name:
			item["qty"] += qty
			return
	cart.append({"name": name, "price": price, "qty": qty})

def cart_total(cart: list[dict]) -> float:
	return sum(item["price"] * item["qty"] for item in cart)

def apply_discount(total: float, percent: float = 0) -> float:
	if 0 <= percent <= 100:
		total = total * (1 - percent / 100)
	return round(total, 2)

def make_receipt(cart: list[dict], discount: float = 0, title: str = "Чек") -> str:
	total = cart_total(cart)
	final_total = apply_discount(total, discount)
	discount_amount = round(total - final_total, 2)
	lines = [f"======== {title} ========"]
	for item in cart:
		name = item["name"]
		qty = item["qty"]
		price = item["price"]
		lines.append(f"{name:<15} {qty} x {price:.2f}")
	lines.append("-" * 25)
	lines.append(f"Сумма: {total:>18.2f}")
	if discount > 0:
		lines.append(f"Скидка: {discount:>3.0f}%: {discount_amount:>14.2f}")
	lines.append(f"Итого: {final_total:>18.2f}")
	lines.append("=" * 25)
	return "\n".join(lines)

def cheapest(*prices: float) -> float | None:
	if not prices:
		return None
	return min(prices)

def item_card(**fields) -> str:
	parts = [f"{key}: {value}" for key, value in fields.items()]
	return ", ".join(parts)

cart = []
add_item(cart, "Хлеб", 45.0)
add_item(cart, "Молоко", 89.9, qty = 2)
add_item(cart, "Сыр", 350.0)

print(make_receipt(cart, discount = 10))
print()
print("Самая дешёвая цена:", cheapest(45, 89.9, 350))
print("Карточка товарв:", item_card(name = "Сыр", price = 350))