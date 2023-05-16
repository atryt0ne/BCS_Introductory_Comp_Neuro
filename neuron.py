import numpy as np
import matplotlib.pyplot as plt

t_max = 150e-3   
dt = 1e-3        
tau = 20e-3      
el = -60e-3     
vr = -70e-3      
vth = -50e-3     
r = 100e6        
i_mean = 25e-11  
print(t_max, dt, tau, el, vr, vth, r, i_mean)


step_end = 10
v=el
for step in range(step_end):
  t = step * dt
  i = i_mean * (1 + np.sin((t * 2 * np.pi) / 0.01))
  v = v + dt/tau * (el - v + r*i)
  print(f'{t:.3f} {i:.4e} {v:.4e}')

step_end = 25
with plt.xkcd():
  plt.figure()
  plt.title('Synaptic Input I(t)')
  plt.xlabel('time (s)')
  plt.ylabel('I (A)')

  for step in range(step_end):
    t = step * dt
    i = i_mean * (1 + np.sin((t * 2 * np.pi) / 0.01))
    # Plot i (use 'ko' to get small black dots (short for color='k' and marker = 'o'))
    plt.plot(t, i, 'ko')

plt.show()


step_end = int(t_max / dt)
v = el

with plt.xkcd():
  plt.figure()
  plt.title('V_m with sinusoidal I(t)')
  plt.xlabel('time (s)')
  plt.ylabel('V_m (V)');

  
  for step in range(step_end):
    t = step * dt
    i = i_mean * (1 + np.sin((t * 2 * np.pi) / 0.01))
    v = v + dt/tau * (el - v + r*i)

    # Plot v (using 'k.' to get even smaller markers)
    plt.plot(t, v, 'k.')
  plt.show()



# Set random number generator
np.random.seed(2020)

# Initialize step_end and v
step_end = int(t_max / dt)
v = el

plt.figure()
plt.title('$V_m$ with random I(t)')
plt.xlabel('time (s)')
plt.ylabel('$V_m$ (V)')

for step in range(step_end):
    t = step * dt
    # Get random number in correct range of -1 to 1 (will need to adjust output of np.random.random)
    random_num = 2 * np.random.randn()

    # Compute value of i at this time step
    i =  i_mean * (1 + 0.1 * (t_max / dt)**(0.5) * random_num)

    v = v + dt/tau * (el - v + r*i)
    plt.plot(t, v, 'k.')
plt.show()



np.random.seed(2020)

step_end = int(t_max / dt)
n = 50

#DOUBT#############################################################
# Intiatialize the list v_n with 50 values of membrane leak potential el
v_n = [el] * n

with plt.xkcd():
  plt.figure()
  plt.title('Multiple realizations of $V_m$')
  plt.xlabel('time (s)')
  plt.ylabel('$V_m$ (V)')

  for step in range(step_end):
    t = step * dt
    for j in range(0, n):
      i = i_mean * (1 + 0.1 * (t_max/dt)**(0.5) * (2* np.random.random() - 1))
      #DOUBT###################################################### IT IS CALCULATING V(N+DELN)
      # Compute value of v for this simulation
      v_n[j] = v_n[j] + (dt / tau) * (el - v_n[j] + r*i)
    #DOUBT#########################################################
    # Plot all simulations (use alpha = 0.1 to make each marker slightly transparent)
    plt.plot([t] * n, v_n, 'k.', alpha=0.1)
  plt.show()



np.random.seed(2020)
step_end = int(t_max / dt)
n = 50
v_n = [el] * n

plt.figure()
plt.title('Multiple realizations of $V_m$')
plt.xlabel('time (s)')
plt.ylabel('$V_m$ (V)')

for step in range(step_end):
  t = step * dt
  for j in range(0, n):
    i = i_mean * (1 + 0.1 * (t_max/dt)**(0.5) * (2* np.random.random() - 1))
    v_n[j] = v_n[j] + (dt / tau) * (el - v_n[j] + r*i)

  # Compute sample mean by summing list of v_n using sum, and dividing by n
  v_mean = sum(v_n) / n

  plt.plot(n*[t], v_n, 'k.', alpha=0.1)
  plt.plot(t, v_mean, 'C0.', alpha=0.8)
plt.show()




np.random.seed(2020)
step_end = int(t_max / dt)
n = 50
v_n = [el] * n

plt.figure()
plt.title('Multiple realizations of $V_m$')
plt.xlabel('time (s)')
plt.ylabel('$V_m$ (V)')


for step in range(step_end):
  t = step * dt
  for j in range(0, n):
    i = i_mean * (1 + 0.1 * (t_max/dt)**(0.5) * (2* np.random.random() - 1))
    v_n[j] = v_n[j] + (dt / tau) * (el - v_n[j] + r*i)
  v_mean = sum(v_n) / n

  # Initialize a list `v_var_n` with the contribution of each V_n(t) to
  # Var(t) with a list comprehension over values of v_n
  v_var_n = [(v - v_mean)**2 for v in v_n]
  #this is a list

  # Compute sample variance v_var by summing the values of v_var_n with sum and dividing by n-1
  v_var = sum(v_var_n)/(n - 1)

  # Compute the standard deviation v_std with the function np.sqrt
  v_std = v_var**0.5

  plt.plot(n*[t], v_n, 'k.', alpha=0.1)
  plt.plot(t, v_mean, 'C0.', alpha=0.8, markersize=10)
  # Plot mean + standard deviation with alpha=0.8 and argument 'C7'
  plt.plot(t, v_mean + v_std, 'C7.', alpha=0.8)
  # Plot mean - standard deviation with alpha=0.8 and argument 'C7'
  plt.plot(t, v_mean - v_std, 'C7.', alpha=0.8)
plt.show()



np.random.seed(2020)
step_end = int(t_max / dt) - 1
t_range = np.linspace(0, t_max, num=step_end, endpoint=False)
v = el * np.ones(step_end)

# Simulate current over time
i = i_mean * (1 + 0.1 * (t_max/dt) ** (0.5) * (2 * np.random.random(step_end) - 1))

for step in range(1, step_end):

  # Compute v as function of i
  v[step] = v[step - 1] + (dt / tau) * (el - v[step - 1] + r * i[step])

with plt.xkcd():
  plt.figure()
  plt.title('$V_m$ with random I(t)')
  plt.xlabel('time (s)')
  plt.ylabel('$V_m$ (V)')

  plt.plot(t_range, v, 'k.')
  plt.show()


# Set random number generator
np.random.seed(2020)
step_end = int(t_max / dt)
n = 50
t_range = np.linspace(0, t_max, num=step_end)
v_n = el * np.ones([n, step_end])
i = i_mean * (1 + 0.1 * (t_max / dt)**(0.5) * (2 * np.random.random([n, step_end]) - 1))

# Loop for step_end - 1 steps
for step in range(1, step_end):

   # Compute v_n
   v_n[:, step] = v_n[:, step - 1] + (dt / tau) * (el - v_n[:, step - 1] + r * i[:, step])

with plt.xkcd():
  plt.figure()
  plt.title('Multiple realizations of $V_m$')
  plt.xlabel('time (s)')
  plt.ylabel('$V_m$ (V)')

  plt.plot(t_range, v_n.T, 'k', alpha=0.3)
  plt.show()




step_end = int(t_max / dt)
n = 50
t_range = np.linspace(0, t_max, num=step_end)
v_n = el * np.ones([n, step_end])
i = i_mean * (1 + 0.1 * (t_max / dt)**(0.5) * (2 * np.random.random([n, step_end]) - 1))

for step in range(1, step_end):
  v_n[:, step] = v_n[:, step - 1] + (dt / tau) * (el - v_n[:, step - 1] + r * i[:, step])


v_mean = np.mean(v_n, axis=0)
v_std = np.std(v_n, axis=0)
with plt.xkcd():
  plt.figure()
  plt.title('Multiple realizations of $V_m$')
  plt.xlabel('time (s)')
  plt.ylabel('$V_m$ (V)')

  plt.plot(t_range, v_n.T, 'k', alpha=0.3)

  plt.plot(t_range, v_n[-1], 'k', alpha=0.3, label='V(t)')
  plt.plot(t_range, v_mean, 'C0', alpha=0.8, label='mean')
  plt.plot(t_range, v_mean+v_std, 'C7', alpha=0.8)
  plt.plot(t_range, v_mean-v_std, 'C7', alpha=0.8, label='mean $\pm$ std')

  plt.legend()
  plt.show()
