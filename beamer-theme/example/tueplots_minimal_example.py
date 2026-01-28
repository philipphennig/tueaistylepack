import matplotlib.pyplot as plt
from tueplots import bundles
from tueplots.constants.color import rgb

plt.rcParams.update(bundles.beamer_tueai(rel_width=0.6))
fig, ax = plt.subplots()  # no `figsize` here!

# your plotting code goes here

plt.savefig("plotname.pdf")  # no `bbox_inches` etc. here!
