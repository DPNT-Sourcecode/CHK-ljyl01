
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        prices = {
            "A": 50,
            "B": 30,
            "C": 20,
            "D": 15,
        }
        item_counts = {
            "A": 0,
            "B": 0,
            "C": 0,
            "D": 0,
        }

        for sku in skus:
            if sku not in prices:
                return -1
            item_counts[sku] += 1

        num_A = item_counts["A"]
        total_A_price = math.floor(num_A)






