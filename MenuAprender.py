
import random
class Item(object):
    def __init__(self, name, ingredients, price):
        self.name = name
        self.ingredients = ingredients
        self.price = price
    def getName(self):
        return self.name
    def getIngredients(self):
        return self.ingredients
    def getPrice(self):
        return self.price

menu = [Item("Sampler","2Huevos/Salchicha/Tocino/2Pancakes/Papas",139),Item("Any Way","2Huevos/Salchicha|Jamon|Tocino/Papas/Pan",119),Item("Huevos Rancheros","2HuevosEstrellados/Frijol/Queso/SalsaRanchera/Papas",139),
        Item("OmeletteCC","Salchicha/Hongo/Morron/Queso/SalsaJalapenio/Pan/Papas",129),Item("OmeletteMeat","Jamon/Tocino/Salchicha/SalsaRanchera/Papas/Pan",139),
        Item("OmeletteVeggie","Morron/Cebolla/Hongo/SalsaEspinaca/Papa/Pan",119),Item("CCSandwich","PanCasa/Salchicha/TortaHuevo/SpicyCheddar/Papas",129),
        Item("PanelaPesto","PanCasa/Panela/Tomate/Espinacas/Pesto/Papas",99),Item("Benedict","EnglishMuffin/Jamon/2HuevosPochados/SalsaMantequillaHuevo/Papas",159),
        Item("CountryFried","BistecEmpanizado/Gravy/Huevo/Papas",179),Item("ChickenWaffles","Waffle/2PiernasEmpanizado/HoneyMustard",149),Item("Divorciados","RojosyVerdes/Huevo/Pollo|Carne/Frijoles",149),
        Item("PancakeOriginal","3Pancakes/CremaBatida",69),Item("Tiramisu","3PancakesCafe/QuesoCremaDulce/Cocoa/CremaBatida",119),Item("SeasonalPancakes","3Pancakes/Platano/Fresa/MielCasa/CremaBatida",99),
        Item("WaffleChocolate","WaffleChocolate/Nieve/CremaBatida/ChispasChocolate",99),Item("AppleCobbler","Waffle/Manzana/Granola/Nieve/Cacahuate",99),
        Item("WaffleOriginal","WaffleVainilla/Platano/Fresa/Nieve/Nuez",99),Item("FrancesOriginal","PanFrances/Fresas/Platano/CremaBatida",79),
        Item("FrancesChocolate","PanFrances/Fresas/ChispasChocolate/CremaBatida",99),Item("GrilledHam","Jamon/QuesoAmericano/PapasFritas",70),
        Item("JrPancakes","3MiniPancakes/Fruta/CremaBatida",70),Item("ChikisWaffles","TirasPolloEmpanizado/2TriangulosWaffles",80),
        Item("JrSampler","Huevo/Tocino/Salchicha/Pancake/CremaBatida",70),Item("PlatoFruta","Papaya/Fresa/Sandia/Pina/Melon/Cottage|Yogurt",85),
        Item("Te","Verde|Negro|Manzanilla",35),Item("JVerde","Pina/Pepino/Apio/Miel",50),Item("JCitrico","Toronja/Espinaca/Naranja/Papaya/Pina",50),
        Item("JRojo","Fresas/Pina/Limon/Miel",50)]
item = menu[random.randint(0,len(menu)-1)]
while True:
    x = input("Press Enter")
    if x == "":
        print(item.getName())
        x = input("See answer? (Y)")
        if x == "y" or x == "Y":
            print(item.getIngredients()+" "+str(item.getPrice()))
        item = menu[random.randint(0,len(menu)-1)]
            
            


