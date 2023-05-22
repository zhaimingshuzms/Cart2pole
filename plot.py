import matplotlib.pyplot as plt
import sys
def get_rewards(file_path):
    # Initialize lists to store rewards
    rewards = []
    # Read the test file
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Parse the lines and extract rewards and steps
    for line in lines:
        if line.startswith("mean_rewards"):
            _, reward = line.strip().split()
            reward = reward[1:-1]
            rewards.append(float(reward))
    
    return rewards

rewards_list = []
for i in sys.argv[1:]:
    rewards_list.append(get_rewards(i))



print(rewards_list)
# Plot rewards
plt.figure(figsize=(6,10))
for i in range(len(rewards_list)):
    # plt.plot(range(len(rewards_list[i])), rewards_list[i], label="r"+str(3-i))
    plt.plot(range(len(rewards_list[i])), rewards_list[i], label="r"+str(i*2+1))
plt.xlabel("Index",fontsize=30)
plt.ylabel("Reward",fontsize=30)
plt.title("Reward Change with Index",fontsize=40)

# font-size
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

# Show the plots
plt.legend(fontsize=30)
plt.show()



