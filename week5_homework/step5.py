#!/usr/bin/env python3

import numpy as np
from bdg_loader import *
import matplotlib.pyplot as plt


python scale_bdg.py R1_treat_pileup.bdg scaled_bdg.bdg
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' scaled_bdg.bdg > cropped_R1.bdg


python scale_bdg.py D2_Klf4_treat.bdg scaled_Klf4.bdg
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' scaled_Klf4.bdg > cropped_Klf4.bdg

python scale_bdg.py D0_H3K27ac_treat.bdg scaled_D0.bdg
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' scaled_D0.bdg > cropped_D0.bdg

 python scale_bdg.py D2_H3K27ac_treat.bdg scaled_D2.bdg
 awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' scaled_D2.bdg > cropped_D2.bdg


traces = ['Sox2', 'Klf4', 'H3K27ac_D0', 'H3K27ac_D2']
fig, ax = plt.subplots(nrows=4)
for i, trace in enumerate(traces):
    file_name = f"cropped_{trace}.bdg"
    data = load_data(file_name)
    ax[i].plot(data['X'], data['Y'])
    ax[i].set_ylabel(trace)
fig.tight_layout(pad=1.0)
#plt.show()
plt.savefig("step5_plot.png")



