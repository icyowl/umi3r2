import matplotlib.pyplot as plt
import numpy as np

# imarin
p = 1/99.9
st_p = 1/9.9
q = 1 - p
st_q = 1 - st_p
st = 5
pz = 'heso', 'denchu', 'attacker', 'gen1', 'gen2'
prize = dict(zip(pz, [3, 2, 11, 3, 4]))
count = 10
round_ = 10, 5, 5
ratio = 0.1, 0.57, 0.33
jitan = 95, 45, 20
zanho = 8 - 2 # 残保留（残保留8 - 欠損保留2)

st_persistency = 1-st_q**st
jt = [x+zanho for x in jitan]
jt_prob = [1-q**x for x in jt]
jt_presistency = np.dot(jt_prob, ratio)
presistence_rate = 1 - ((1 - st_persistency) * (1 - jt_presistency))
# print(presistency)  # 0.625...
expected_renchan = 1/(1-presistence_rate)
print('renchan', expected_renchan)  # 2.669...

expected_round = np.dot(round_, ratio)
# print(expected_round)  # 5.5

x = 0
payout = prize['attacker'] * count - count
ty = expected_renchan * expected_round * (payout-x)
print('ty:', ty)

border = 250 / (ty * p)
print('border:', border)  # 16.837

# invest = 99.9 * 250 / rate
# a = ty / invest
# print(a)