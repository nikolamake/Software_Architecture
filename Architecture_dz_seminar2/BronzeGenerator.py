import ItemGenerator
import BronzeReward

class BronzeGenerator(ItemGenerator.ItemGenerator):
    def create_item(self, l_border, r_border):
        return BronzeReward.BronzeReward(l_border, r_border)