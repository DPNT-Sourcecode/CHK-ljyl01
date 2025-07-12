from solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckout():
    def test_checkout(self):
        assert CheckoutSolution().checkout("") == -1
        assert CheckoutSolution().checkout("A") == 50
        assert CheckoutSolution().checkout("B") == 30

