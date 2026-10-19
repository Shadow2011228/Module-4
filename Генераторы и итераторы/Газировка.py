class Sparky:
    warehouse = True

    def create(self):
        while self.warehouse:
            yield "Газировка течёт!"



spark = Sparky()
water_on_main_square = spark.create()

print(next(water_on_main_square))

spark.warehouse = False
print(next(water_on_main_square))

spark.warehouse = True
print(next(water_on_main_square))
