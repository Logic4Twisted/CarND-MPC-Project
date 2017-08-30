import matplotlib.pyplot as plt

with open('output.txt') as f:
	lines = f.readlines()

ctes = []
epsis = []
steer = []
speed = []
for line in lines:
	if line.startswith('cte = '):
		ctes.append(float(line[len ('cte = '):]))
	if line.startswith('epsi = '):
		epsis.append(float(line[len ('epsi = '):]))
	if line.startswith('steer_value = '):
		steer.append(float(line[len('steer_value = '):]))
	if line.startswith('speed = '):
		speed.append(float(line[len('speed = '):]))

t = range(len(ctes))

f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)
l1, = ax1.plot(t, ctes, color='r')
ax1.grid(True)
l2, = ax2.plot(t, epsis, color='g')
ax2.grid(True)
ax2.set_ylim([-5.0,5.0])
l3, = ax3.plot(t, steer, color='b')
ax3.grid(True)
ax1.set_title('Initial performace')
plt.legend([l1, l2, l3],["cte", "epsi", "steer_value"])
plt.show()