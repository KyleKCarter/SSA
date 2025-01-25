# from scipy.stats import norm
import math

# O/U Formula
# Given data
P = 6  # Predetermined combined score
A1 = 3.62  # Average points per game for Team 1
O1 = 2.62  # Average points allowed by Team 1
A2 = 2.44  # Average points per game for Team 2
O2 = 3.12  # Average points allowed by Team 2

# Step 1: Calculate expected scores for both teams
E1 = (A1 + O2) / 2
E2 = (A2 + O1) / 2

# Step 2: Combined expected score
E = E1 + E2

# Step 3: Standard deviation of combined score
sigma1 = 0.15 * A1
sigma2 = 0.15 * A2
sigma_combined = math.sqrt(sigma1**2 + sigma2**2)

# Step 4: Z-score
Z = (P - E) / sigma_combined

# Step 5: Probabilities using normal distribution CDF
print(Z)
# probability_under = norm.cdf(Z)  # Probability of combined score being under P
# probability_over = 1 - probability_under  # Probability of combined score being over P

# probability_under, probability_over




# ML Formula
# Given data for winning probabilities calculation with win percentages
A1 = 36.4  # Average points per game for Team 1
O1 = 12.1  # Average points allowed by Team 1
wins1 = 12  # Team 1 season wins
losses1 = 2  # Team 1 season losses

A2 = 34.3  # Average points per game for Team 2
O2 = 14.5  # Average points allowed by Team 2
wins2 = 13  # Team 2 season wins
losses2 = 2  # Team 2 season losses

# Step 1: Win percentages for each team
WP1 = wins1 / (wins1 + losses1)
WP2 = wins2 / (wins2 + losses2)

# Step 2: Adjust expected scores by win percentages
E1 = (A1 + O2) / 2 * WP1
E2 = (A2 + O1) / 2 * WP2

# Step 3: Standard deviation for each team's score
sigma1 = 0.15 * A1
sigma2 = 0.15 * A2

# Step 4: Calculate Z-score for Team 1 winning
Z = (E1 - E2) / math.sqrt(sigma1**2 + sigma2**2)

print(Z)
# Step 5: Calculate winning probabilities
# probability_team1_wins = norm.cdf(Z)
# probability_team2_wins = 1 - probability_team1_wins

# E1, E2, Z, probability_team1_wins, probability_team2_wins