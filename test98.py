# asd1 = [1, 2, 3]
# asd2 = [1, 2, 3]
# print(asd1 is asd2)
# asd3 = asd1
# print(asd1 is asd3)
# asd3[1] = "Klaus"
# print(asd3 is asd1)
# print(asd1)
# print(asd2)
# print(asd3)
# str1 = "monty"
# str3 = str1
# print(str1 is str3)
ist_klein = {"Felix", "Hanne", "Hörnchen", "Karin"}
ist_mittel = {"Anton", "Bonni", "Annabell", "Annaleena", "Kleo", "Franka", "Tom Nook"}
ist_gross = {"Adelheid", "Adrian", "Apollo", "Arthur", "Quetzal", "Sid", "Eli", "Arne", "Boris"}
ist_katze = {"Kleo", "Franka", "Gunnar", "Arne", "Boris"}

# 1. Bewohner der Art Katze, die auch in ist_mittel sind
# katzen_in_mittel = ist_katze & ist_mittel
# print(katzen_in_mittel)
# print(ist_katze.intersection(ist_mittel))
alle_bewohner = ist_klein | ist_mittel | ist_gross | ist_katze
print(alle_bewohner)