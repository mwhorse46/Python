from matplotlib  import pyplot as plt

x = [5,6,7,8]
y = [7,3,8,3]

print(len(x))
print(len(y))

plt.plot(x,y)

plt.title('Epic Chart')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show() 
