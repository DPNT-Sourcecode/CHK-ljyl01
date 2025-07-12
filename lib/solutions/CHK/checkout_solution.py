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

    # skus = unicode string
    def checkout(self, skus):
        special_offers = {
            "A": [(5, 200), (3, 130)],
            "B": [(2, 45)],
            "H": [(10, 80), (5, 45)],
            "K": [(2, 150)],
            "P": [(5, 200)],
            "Q": [(3, 80)],
            "V": [(3, 130), (2, 90)],
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
            if sku not in PRICES:
                return -1
            item_counts[sku] += 1

        num_E = item_counts["E"]
        num_free_B = num_E // 2
        num_B = max(item_counts["B"] - num_free_B, 0)

        num_A = item_counts["A"]
        num_5A = num_A // 5
        remainder_A = num_A % 5
        total_A_price = num_5A * 200 + remainder_A // 3 * 130 + (remainder_A % 3) * PRICES["A"]

        total_B_price = (num_B // special_offers["B"][0]) * special_offers["B"][1] + (num_B % special_offers["B"][0]) * PRICES["B"]

        total_C_price = item_counts["C"] * PRICES["C"]
        total_D_price = item_counts["D"] * PRICES["D"]
        total_E_price = item_counts["E"] * PRICES["E"]

        num_F = item_counts["F"]
        total_F_price = (num_F // 3) * 2 * PRICES["F"] + (num_F % 3) * PRICES["F"]

        return total_A_price + total_B_price + total_C_price + total_D_price + total_E_price + total_F_price



