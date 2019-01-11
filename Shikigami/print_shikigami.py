# read another python file in the same folder

from shikigami import Shikigami

name = list(Shikigami.keys())
print("Name:       {:>12}{:>12}{:>12}{:>12}{:>12}{:>12}{:>12}{:>12}".format(*name))

attribute = []
for name in Shikigami.keys():
    attribute.append(Shikigami[name]["attribute"])
print("Attribute:  {:>12}{:>12}{:>12}{:>12}{:>12}{:>12}{:>12}{:>12}".format(*attribute))

age = []
for name in Shikigami.keys():
    age.append(Shikigami[name]["age"])
print("Age:        {:>12}{:>12}{:>12}{:>12}{:>12}{:>12}{:>12}{:>12}".format(*age))

lev = []
for name in Shikigami.keys():
    lev.append(Shikigami[name]["lev"])
print("Level:      {:>12}{:>12}{:>12}{:>12}{:>12}{:>12}{:>12}{:>12}".format(*lev))

skill = []
for name in Shikigami.keys():
    skill.append(Shikigami[name]["skill"])
print("Skill:      {:>10}{:>9}{:>10}{:>9}{:>10}{:>9}{:>10}{:>9}".format(*skill))






