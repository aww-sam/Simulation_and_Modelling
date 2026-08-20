import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

observed = np.array([[30, 0],
                      [20, 30]])
chi2, p, dof, expected = st.chi2_contingency(observed)

categories = ["Male-1", "Male-2", "Female-1", "Female-2"]
x = np.arange(len(categories))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x - width/2, observed.flatten(), width, alpha=0.7, label="Observed", color="black")
ax.bar(x + width/2, expected.flatten(), width, alpha=0.7, label="Expected", color="grey")

ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.set_ylabel("Frequency")
ax.set_title(
    f"Chi-Square Test\n"
    f"Chi-square: {round(chi2,4)}   dof: {dof}   P-value: {round(p,4)}\n"
    f"Expected: {expected.round(2).tolist()}",
    fontsize=10
)
ax.legend(loc="upper left", bbox_to_anchor=(1.0, 1.0))
ax.grid(True)

plt.tight_layout()
plt.show()