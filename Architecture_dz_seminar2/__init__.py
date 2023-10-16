import random

import BronzeGenerator, CopperGenerator, GoldGenerator, PlatinumGenerator, WoodenGenerator

generators_list = []

def create_generators_list(l_border: int, r_border: int):

    generators_list.append(BronzeGenerator.BronzeGenerator(l_border, r_border))
    generators_list.append(CopperGenerator.CopperGenerator(l_border, r_border))
    generators_list.append(GoldGenerator.GoldGenerator(l_border, r_border))
    generators_list.append(PlatinumGenerator.PlatinumGenerator(l_border, r_border))
    generators_list.append(WoodenGenerator.WoodenGenerator(l_border, r_border))


create_generators_list(1, 50 )


for i in range(10):
    k = random.randint(0, 4)
    generators_list[k].open_reward()

# print(dir('Architecture_dz.Architecture_dz_seminar2'))