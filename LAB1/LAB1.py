import random
import matplotlib.pyplot as plt
steps=100
X=0
Y=0
x_positions=[X]
y_positions=[Y]

for i in range(steps):
  direction=random.choice(['left','right','straight'])
  if direction=='left':
    X=X-1
  elif direction=='right':
    X=X+1
  else:
    Y=Y+1
  x_positions.append(X)
  y_positions.append(Y)

plt.figure(figsize=(10,10))
plt.plot(x_positions,y_positions,marker='o',markersize=2,color='g')
plt.scatter(x_positions[0],y_positions[0],color='blue',label='START')
plt.scatter(x_positions[-1],y_positions[-1],color='red',label='END')
plt.title("Random Walk Simulations of a drunk person")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.legend()
plt.show()
