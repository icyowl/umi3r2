import matplotlib.pyplot as plt
import numpy as np

p = 1/99.9
q = 1 - p
kp = 1/18.0
prize = {'heso': 3, 'denchu': 2, 'attacker': 10}
count = 10
round_ = 10, 10, 7, 5, 3
ratio = 0.02, 0.01, 0.01, 0.9, 0.06
time_saving = 33  # 時短
remain = 0  # 時短抜けの残保留（残保留6 - 欠損保留6)

probability_of_next_bonus = 1 * 0.55 + (1-q**(time_saving+remain)) * 0.45
expected_count = 1/(1-probability_of_next_bonus)
expected_rounds = np.dot(round_, ratio)
payout_for_round = prize['attacker'] * count - count
ty = expected_count * expected_rounds * payout_for_round  # T(特賞)Y(寄り玉) 1421.916
border = 250 / (ty * p)

print('TY:', ty, 'Border', border, '1R payout', payout_for_round)
base = border
base = 22
invest = 99.9 * 250 / base
a = ty / invest
print(a)