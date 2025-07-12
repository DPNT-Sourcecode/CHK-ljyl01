from lib.solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckout():
    def test_checkout(self):
        assert CheckoutSolution().checkout("") == 0
        assert CheckoutSolution().checkout("A") == 50
        assert CheckoutSolution().checkout("AA") == 100
        assert CheckoutSolution().checkout("AAA") == 130
        assert CheckoutSolution().checkout("AAAA") == 180
        assert CheckoutSolution().checkout("B") == 30
        assert CheckoutSolution().checkout("BB") == 45
        assert CheckoutSolution().checkout("BBB") == 75
        assert CheckoutSolution().checkout("C") == 20
        assert CheckoutSolution().checkout("D") == 15
        assert CheckoutSolution().checkout("AB") == 80
        assert CheckoutSolution().checkout("ABB") == 95
        assert CheckoutSolution().checkout("-") == -1
        assert CheckoutSolution().checkout("a") == -1
        assert CheckoutSolution().checkout("E") == 40
        assert CheckoutSolution().checkout("BEE") == 80
        assert CheckoutSolution().checkout("BEEE") == 120
        assert CheckoutSolution().checkout("BBEE") == 110
        assert CheckoutSolution().checkout("BBEEE") == 150
        assert CheckoutSolution().checkout("BBEEEE") == 160
        assert CheckoutSolution().checkout("BEEEE") == 160
        assert CheckoutSolution().checkout("ABEEEE") == 210
        assert CheckoutSolution().checkout("AAAAA") == 200
        assert CheckoutSolution().checkout("AAAAAA") == 250
        assert CheckoutSolution().checkout("AAAAAAA") == 300
        assert CheckoutSolution().checkout("F") == 10
        assert CheckoutSolution().checkout("FF") == 20
        assert CheckoutSolution().checkout("FFF") == 20
        assert CheckoutSolution().checkout("FFFF") == 30
        assert CheckoutSolution().checkout("FFFFF") == 40
        assert CheckoutSolution().checkout("FFFFFF") == 40
        assert CheckoutSolution().checkout("AFFFFFF") == 90
        assert CheckoutSolution().checkout("UUU") == 120
        assert CheckoutSolution().checkout("UUUU") == 120
        assert CheckoutSolution().checkout("HHHH") == 40
        assert CheckoutSolution().checkout("HHHHH") == 45
        assert CheckoutSolution().checkout("HHHHHHHHH") == 85
        assert CheckoutSolution().checkout("HHHHHHHHHH") == 80


