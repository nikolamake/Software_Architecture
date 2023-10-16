import ItemGenerator
import WoodenReward

class WoodenGenerator(ItemGenerator.ItemGenerator):
    def create_item(self, l_border, r_border):
        return WoodenReward.WoodenReward(l_border, r_border)