import matplotlib.pyplot as plot

#create lists
numlist = [8, 6, 5, 3]
namelist = ['freshmen', 'sophomores', 'juniors', 'seniors']
colorlist = ['yellow', 'green', 'purple', 'pink']
explodelist = [0.0, 0.0, 0.0, 0.0]

#create pie chart
plot.pie(numlist, labels=namelist, autopct='%1.1f%%',
         colors=colorlist, explode=explodelist, startangle=5)
plot.axis('equal')
plot.savefig('piechart.png')
plot.show()