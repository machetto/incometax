import matplotlib.pyplot as plt
import numpy as np
from bisect import bisect

from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Calibri']
rcParams['font.size'] = 10

max_income = 500000

sections = 100

rates = [0, 19, 32.5, 37, 45]

brackets = [18201, 37001, 90001, 180001]

base_tax = [0, 3572, 20797, 54097] 

def tax(income):
    i = bisect(brackets, income)
    if not i:
        return 0
    rate = rates[i]
    bracket = brackets[i-1]
    income_in_bracket = income - bracket
    tax_in_bracket = income_in_bracket * rate / 100
    total_tax = base_tax[i-1] + tax_in_bracket
    return total_tax

x = np.linspace(0, max_income, sections)
y = [0] * sections

for index, item in enumerate(x):
    y[index] = 100*(item-tax(item))/item

y[0] = 100 # fix divide by zero for the first element

axes= plt.axes()
axes.grid()

plt.plot(x, y)

plt.xlim(0, max_income) 
plt.ylim(0, 110)

plt.xlabel('Gross income')
plt.ylabel('Net income as % of gross income')

plt.title('Net income graph')
plt.show() 
