import matplotlib.pyplot as plt
 
# x axis values
x = [10000.0,1000.0,100.0,10.0,1.0,0.1,0.01,0.001,0.0001,0.00001]
# corresponding y axis values
y_rbf = [0.589156626506,0.55,0.578313253012,0.640361445783,0.669277108434,0.657228915663,0.66686746988,0.671084337349,0.659036144578,0.638554216867]
y_linear=[0.579518072289,0.569277108434,0.551807228916,0.628313253012,0.668674698795,0.675301204819,0.660240963855,0.666265060241,0.672289156627,0.628915662651]
y_poly2=[0.573493975904,0.53734939759,0.553012048193,0.634337349398,0.65421686747,0.666265060241,0.680722891566,0.66686746988,0.64156626506,0.621686746988]
y_poly3=[0.564457831325,0.586746987952,0.595180722892,0.630120481928,0.663855421687,0.679518072289,0.680120481928,0.667469879518,0.636144578313,0.642771084337]
lw=2
plt.plot(x, y_rbf, color='navy', lw=lw, label='RBF model')
plt.plot(x, y_linear, color='darkorange', lw=lw, label='linear model')
plt.plot(x, y_poly2, color='c', lw=lw, label='Poly2 model')
plt.plot(x, y_poly3, color='cornflowerblue', lw=lw, label='Poly3 model')

# plotting the points 
#plt.plot(x, y)
import matplotlib.pyplot as plt
 
# x axis values
x = [10000.0,1000.0,100.0,10.0,1.0,0.1,0.01,0.001,0.0001,0.00001]
# corresponding y axis values
y_rbf = [0.589156626506,0.55,0.578313253012,0.640361445783,0.669277108434,0.657228915663,0.66686746988,0.671084337349,0.659036144578,0.638554216867]
y_linear=[0.579518072289,0.569277108434,0.551807228916,0.628313253012,0.668674698795,0.675301204819,0.660240963855,0.666265060241,0.672289156627,0.628915662651]
y_poly2=[0.573493975904,0.53734939759,0.553012048193,0.634337349398,0.65421686747,0.666265060241,0.680722891566,0.66686746988,0.64156626506,0.621686746988]
y_poly3=[0.564457831325,0.586746987952,0.595180722892,0.630120481928,0.663855421687,0.679518072289,0.680120481928,0.667469879518,0.636144578313,0.642771084337]
lw=2
plt.plot(x, y_rbf, color='navy', lw=lw, label='RBF model')
plt.plot(x, y_linear, color='darkorange', lw=lw, label='linear model')
plt.plot(x, y_poly2, color='c', lw=lw, label='Poly2 model')
plt.plot(x, y_poly3, color='cornflowerblue', lw=lw, label='Poly3 model')

# plotting the points 
#plt.plot(x, y)
tick_locs = [10,20,30,40,50,60,70,80,90,100]
tick_lbls = [10000.0,1000.0,100.0,10.0,1.0,0.1,0.01,0.001,0.0001,0.00001]
plt.xticks(tick_locs, tick_lbls)
# naming the x axis
plt.xlabel('c')
# naming the y axis
plt.ylabel('Accuracy')
 
# giving a title to my graph
plt.title("SVM kernels Comparision With Varying C ")
plt.legend()
# function to show the plot
plt.show()
 
# naming the x axis
plt.xlabel('c')
# naming the y axis
plt.ylabel('Accuracy')
 
# giving a title to my graph
plt.title("SVM kernels Comparision With Varying C ")
plt.legend()
# function to show the plot
plt.show()


'''
import matplotlib.pyplot as plt
 
# x axis values
x = [10000.0,1000.0,100.0,10.0,1.0,0.1,0.01,0.001,0.0001,0.00001]
# corresponding y axis values
y_rbf = [0.589156626506,0.55,0.578313253012,0.640361445783,0.669277108434,0.657228915663,0.66686746988,0.671084337349,0.659036144578,0.638554216867]
y_linear=[0.579518072289,0.569277108434,0.551807228916,0.628313253012,0.668674698795,0.675301204819,0.660240963855,0.666265060241,0.672289156627,0.628915662651]
y_poly2=[0.573493975904,0.53734939759,0.553012048193,0.634337349398,0.65421686747,0.666265060241,0.680722891566,0.66686746988,0.64156626506,0.621686746988]
y_poly3=[0.564457831325,0.586746987952,0.595180722892,0.630120481928,0.663855421687,0.679518072289,0.680120481928,0.667469879518,0.636144578313,0.642771084337]
lw=2
plt.plot(x, y_rbf, color='navy', lw=lw, label='RBF model')
plt.plot(x, y_linear, color='darkorange', lw=lw, label='linear model')
plt.plot(x, y_poly2, color='c', lw=lw, label='Poly2 model')
plt.plot(x, y_poly3, color='cornflowerblue', lw=lw, label='Poly3 model')

# plotting the points 
#plt.plot(x, y)
 
# naming the x axis
plt.xlabel('c')
# naming the y axis
plt.ylabel('Accuracy')
 
# giving a title to my graph
plt.title("SVM kernels Comparision With Varying C ")
plt.legend()
# function to show the plot
plt.show()
'''