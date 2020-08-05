class ValidateProduct:
    def __init__(self, product):
        self.errors = []
        self.product = product

    def validate_name(self):
        if not all(
            (
                isinstance(self.product.name, str),
                3 <= len(self.product.name) < 56,
            )
        ):
            self.errors.append("Invalid product name")

    def validate_value(self):
        if not 0 < self.product.value < 99999.9:
            self.errors.append("Invalid value")

    def validate_discount_value(self):
        if not self.product.discount_value < self.product.value:
            self.errors.append("Invalid discount value")

    def validate_stock(self):
        if not self.product.stock > -1:
            self.errors.append("Invalid stock value")


def get_product_error(product):
    validate = ValidateProduct(product)
    validate.validate_name()
    validate.validate_value()
    validate.validate_discount_value()
    validate.validate_stock()

    return validate.errors
