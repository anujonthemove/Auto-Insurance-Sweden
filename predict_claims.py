import pandas as pd
import matplotlib.pyplot as plt

# Calculating the cost i.e how good a line is or distance of each point from the line 
def cost(x_values, y_values, m, b):
	cost = 0
	N = (len(data))
	for i in range(N):
		cost += (( m * x_values[i] + b ) - y_values[i]) ** 2
	print cost	/ float(N)
		
def gradient_descent(x_values, y_values, m, b, iterations, rate): 
	for i in range(iterations):
		m , b = calculate_gradient_descent(x_values, y_values, m, b, rate) 
	return m , b	

# Differenciating cost function i.e calculating partial derivatives for each
def calculate_gradient_descent(x_values, y_values, m_current , b_current, rate):
	N = float(len(data))
	gradient_m = 0
	gradient_b = 0
	for value in range(len(data)):
		x_value = x_values[value]
		y_value = y_values[value]
		gradient_m += -(2/N) * x_value * (y_value - ((m_current * x_value) + b_current))
		gradient_b += -(2/N) * (y_value - ((m_current * x_value) + b_current))
	updated_m = m_current - (gradient_m * rate)
	updated_b = b_current - (gradient_b * rate)
	return updated_m ,updated_b

# Plot with given x, y, m, b		
def plot(x_values, y_values, m, b):
	y = m*x_values + b
	plt.scatter(x_values,y_values)
	plt.plot(x_values,y)
	plt.show()

# reading from excel file 
data = pd.read_excel('data.xls')

# X = number of claims
# Y = Total payment for all claims

# Extracting feature and target variable
x_values = data['X']
y_values = data['Y']
#print x_values
#print y_values

#Starting values for slope and intercept 
m = 0
b = 0

# Initialising number of iterations and learning rate
iterations = 10000
rate = 0.0001

# Values and plots for starting m and b
print ('Starting m : {}, Starting b :{}'.format(m,b))
cost(x_values, y_values, m, b)
#plot(x_values, y_values, m, b)

best_m , best_b =  gradient_descent(x_values, y_values, m, b, iterations, rate)

# Values and plots for best m and b
print ('Best m : {}, Best b :{}'.format(best_m,best_b))
cost(x_values, y_values, best_m, best_b)
plot(x_values, y_values, best_m, best_b)



