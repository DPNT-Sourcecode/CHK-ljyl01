from email.utils import specialsre


class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        prices = {
            "A": 50,
            "B": 30,
            "C": 20,
            "D": 15,
            "E": 40,
            "F": 10,
        }
        special_offers = {
            "A": (3, 130),
            "B": (2, 45),
        }
        item_counts = {
            "A": 0,
            "B": 0,
            "C": 0,
            "D": 0,
            "E": 0,
            "F": 0,
        }

        for sku in skus:
            if sku not in prices:
                return -1
            item_counts[sku] += 1

        num_E = item_counts["E"]
        num_free_B = num_E // 2
        num_B = max(item_counts["B"] - num_free_B, 0)

        num_A = item_counts["A"]
        num_5A = num_A // 5
        remainder_A = num_A % 5
        total_A_price = num_5A * 200 + remainder_A // 3 * 130 + (remainder_A % 3) * prices["A"]

        total_B_price = (num_B // special_offers["B"][0]) * special_offers["B"][1] + (num_B % special_offers["B"][0]) * prices["B"]

        total_C_price = item_counts["C"] * prices["C"]
        total_D_price = item_counts["D"] * prices["D"]
        total_E_price = item_counts["E"] * prices["E"]

        num_F = item_counts["F"]
        total_F_price = (num_F // 3) * 2 * prices["F"] + (num_F % 3) * prices["F"]

        return total_A_price + total_B_price + total_C_price + total_D_price + total_E_price + total_F_price
