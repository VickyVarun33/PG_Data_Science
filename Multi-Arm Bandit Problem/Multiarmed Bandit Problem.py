import numpy as np

class MultiArmedBandit:
    def __init__(self, num_arms, epsilon):
        self.num_arms = num_arms
        self.epsilon = epsilon
        self.q_values = np.zeros(num_arms)
        self.action_counts = np.zeros(num_arms)

    def select_action(self):
        if np.random.rand() < self.epsilon:
            return np.random.randint(self.num_arms)  # Exploration
        else:
            return np.argmax(self.q_values)  # Exploitation

    def update(self, action, reward):
        self.action_counts[action] += 1
        self.q_values[action] += (reward - self.q_values[action]) / self.action_counts[action]

def simulate_bandit(num_arms, epsilon, num_steps):
    bandit = MultiArmedBandit(num_arms, epsilon)
    rewards = []

    for _ in range(num_steps):
        action = bandit.select_action()
        # Simulating reward as a random number from a normal distribution
        reward = np.random.normal(q_true[action], 1)
        bandit.update(action, reward)
        rewards.append(reward)

    return rewards

# Number of arms (actions) in the bandit problem
num_arms = 5
# True Q-values of each arm (simulated rewards)
q_true = np.random.normal(0, 1, num_arms)
# Epsilon value for epsilon-greedy method
epsilon = 0.1
# Number of steps (time periods) for the simulation
num_steps = 1000

# Simulate the bandit algorithm
rewards = simulate_bandit(num_arms, epsilon, num_steps)

# Print the average reward obtained
print("Average reward:", np.mean(rewards))
