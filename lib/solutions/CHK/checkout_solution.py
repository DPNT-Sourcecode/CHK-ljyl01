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
        "S": 20,
        "T": 20,
        "U": 40,
        "V": 50,
        "W": 20,
        "X": 17,
        "Y": 20,
        "Z": 21,
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
        "F": (3, "F"),
        "N": (3, "M"),
        "R": (3, "Q"),
        "U": (4, "U")
    }

    GROUP_DISCOUNT_OFFERS = {
        ("S", "T", "X", "Y", "Z"): (3, 45)
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

        total_price = 0

        for sku_group, offer in self.GROUP_DISCOUNT_OFFERS.items():
            total_num_of_skus_in_group = sum(item_counts[sku] for sku in sku_group)
            num_times_to_apply_discount = total_num_of_skus_in_group // offer[0]
            total_price += offer[1] * num_times_to_apply_discount
            order_from_most_expensive = sorted(sku_group, key=lambda x: self.PRICES[x], reverse=True)
            times_applied_discount = 0
            while times_applied_discount < num_times_to_apply_discount * offer[0]:
                if len(order_from_most_expensive) == 0:
                    break
                free_sku = order_from_most_expensive[0]
                if item_counts[free_sku] > 0:
                    item_counts[free_sku] -= 1
                else:
                    order_from_most_expensive.remove(free_sku)

        for sku, offer in self.BUY_GET_X_FREE_OFFERS.items():
            num_free_items = item_counts[sku] // offer[0]
            free_item = offer[1]
            item_counts[free_item] = max(item_counts[free_item] - num_free_items, 0)

        for sku, special_offers in self.SPECIAL_OFFERS.items():
            for special_offer in special_offers:
                item_prices[sku] += (item_counts[sku] // special_offer[0]) * special_offer[1]
                item_counts[sku] %= special_offer[0]

        for sku, item_price in item_prices.items():
            item_prices[sku] += item_counts[sku] * self.PRICES[sku]

        return total_price + sum(item_prices.values())






