from email.utils import specialsre


class CheckoutSolution:
    PRICES = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
        "F": 10,
        "G": 20,
        "H": 10,
        "I": 35,
        "J": 60,
        "K": 80,
        "L": 90,
        "M": 15,
        "N": 40,
        "O": 10,
        "P": 50,
        "Q": 30,
        "R": 50,
        "S": 30,
        "T": 20,
        "U": 40,
        "V": 50,
        "W": 20,
        "X": 90,
        "Y": 10,
        "Z": 50,
    }

    SPECIAL_OFFERS = {
        "A": [(5, 200), (3, 130)],
        "B": [(2, 45)],
        "H": [(10, 80), (5, 45)],
        "K": [(2, 150)],
        "P": [(5, 200)],
        "Q": [(3, 80)],
        "V": [(3, 130), (2, 90)],
    }

    BUY_GET_X_FREE_OFFERS = {
        "E": (2, "B"),
        "F": (2, "F"),
        "N": (3, "M"),
        "R": (3, "Q"),
        "U": (3, "U")
    }

    # skus = unicode string
    def checkout(self, skus):
        item_counts = {
            sku: 0 for sku in self.PRICES.keys()
        }

        item_prices = {
            sku: 0 for sku in self.PRICES.keys()
        }

        for sku in skus:
            if sku not in self.PRICES:
                return -1
            item_counts[sku] += 1

        for sku, offer in self.BUY_GET_X_FREE_OFFERS.items():
            num_free_items = item_counts[sku] // offer[0]
            free_item = offer[1]
            item_counts[free_item] = max(item_counts[free_item] - num_free_items, 0)

        for sku, special_offers in self.SPECIAL_OFFERS.items():
            for special_offer in special_offers:
                item_prices[sku] += (item_counts[sku] // special_offer[0]) * special_offer[1]
                item_counts[sku] %= special_offer[0]

        num_E = item_counts["E"]
        num_free_B = num_E // 2
        num_B = max(item_counts["B"] - num_free_B, 0)

        num_A = item_counts["A"]
        num_5A = num_A // 5
        remainder_A = num_A % 5
        total_A_price = num_5A * 200 + remainder_A // 3 * 130 + (remainder_A % 3) * self.PRICES["A"]

        total_B_price = (num_B // self.SPECIAL_OFFERS["B"][0]) * self.SPECIAL_OFFERS["B"][1] + (num_B % self.SPECIAL_OFFERS["B"][0]) * self.PRICES["B"]

        total_C_price = item_counts["C"] * self.PRICES["C"]
        total_D_price = item_counts["D"] * self.PRICES["D"]
        total_E_price = item_counts["E"] * self.PRICES["E"]

        num_F = item_counts["F"]
        total_F_price = (num_F // 3) * 2 * self.PRICES["F"] + (num_F % 3) * self.PRICES["F"]

        return total_A_price + total_B_price + total_C_price + total_D_price + total_E_price + total_F_price







