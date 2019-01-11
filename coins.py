import random


class Coin:
    def __init__(self,rare=False,clean=True, heads=True,**kwargs):
        # pack it down into another dictionary called kwargs

        for key,value in kwargs.items():
            setattr(self,key,value)
            # it's gonna loop thru all of the items
            
        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value*1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color

    def rust(self):
        self.color = self.rusty_color
    def clean(self):
        self.color = self.clean_color

    def __del__(self):                        # spent the coin
        print("Coin Spent!")

    def flip(self):
        heads_options = [True,False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __str__(self):
        if self.original_value >= 1:
            return "${} Coin".format(int(self.original_value))
        else:
            return "{} Coin".format(int(self.original_value * 100))

            
class Quarter(Coin):
    def __init__(self):
        data = {"original_value":0.25,
                "clean_color":"silver",
                "rusty_color":None,
                "num_edges":1,
                "diameter":24.26,
                "thickness":1.75,
                "mass":6.25
                }
        super().__init__(**data)       # unpack the data

class Dime(Coin):
    def __init__(self):
        data = {"original_value":0.10,
                "clean_color":"silver & bronze",
                "rusty_color":"greenish",
                "num_edges":1,
                "diameter":17.91,
                "thickness":1.35,
                "mass":2.268
                }
        super().__init__(**data)

class Nickel(Coin):
    def __init__(self):
        data = {"original_value":0.05,
                "clean_color":"silver",
                "rusty_color":"greenish",
                "num_edges":1,
                "diameter":21.21,
                "thickness":1.95,
                "mass":5.00
                }
        super().__init__(**data)

class Penny(Coin):
    def __init__(self):
        data = {"original_value":0.01,
                "clean_color":"bronze",
                "rusty_color":"brownish",
                "num_edges":1,
                "diameter":19.05,
                "thickness":1.52,
                "mass":2.5
                }
        super().__init__(**data)


coins = [Quarter(), Dime(), Nickel(), Penny()]

for coin in coins:
    arguments = [coin, coin.color, coin.value, coin.diameter, coin.thickness, coin.num_edges, coin.mass]
    string = "{} - color:{}， value:{}, diameter(mm):{}, thickness(mm):{}, number of edges:{}, mass(g):{}".format(*arguments)
    print(string)
