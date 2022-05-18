import numpy as np

# Nominal 

int1 = np.asarray([-0.0975,    0.0972])
int2 = np.asarray([-0.4428,    0.4428])
int3 = np.asarray([-0.0496,    0.0496])
int4 = np.asarray([-0.0557,    0.0557])
int5 = np.asarray([-0.0753,    0.0753])

# Impaired

intimp1 = np.asarray([-0.0924,    0.0924])
intimp2 = np.asarray([-0.4207,    0.4207])
intimp3 = np.asarray([-0.0472,    0.0472])
intimp4 = np.asarray([-0.0529,    0.0529])
intimp5 = np.asarray([-0.0715,    0.0715])

l1 = int1[1] - int1[0]
li1 = intimp1[1] - intimp1[0]

l2 = int2[1] - int2[0]
li2 = intimp2[1] - intimp2[0]

l3 = int3[1] - int3[0]
li3 = intimp3[1] - intimp3[0]

l4 = int4[1] - int4[0]
li4 = intimp4[1] - intimp4[0]

l5 = int5[1] - int5[0]
li5 = intimp5[1] - intimp5[0]

eta1 = 0.04095631266343603
eta2 = 0.017794397799958336

sqr = lambda x : x*x
ETA = np.sqrt(2*sqr(eta1) + 3*sqr(eta2))

dh1 = max(int1[1] - intimp1[1], intimp1[0] - int1[0])
dh2 = max(int2[1] - intimp2[1], intimp2[0] - int2[0])
dh3 = max(int3[1] - intimp3[1], intimp3[0] - int3[0])
dh4 = max(int4[1] - intimp4[1], intimp4[0] - int4[0])
dh5 = max(int5[1] - intimp5[1], intimp5[0] - int5[0])

print(eta1, eta2, ETA)
print(dh1, dh2, dh3, dh4, dh5)

print(1, '&', np.around(dh1, 4), '&', np.around(100*(eta1/dh1), 1), '&', np.around(100*(l1 - 2*eta1)/li1, 1), '&', np.around(100*(l1 - 2*ETA)/li1, 1), '\\\\')
print(2, '&', np.around(dh2, 4), '&', np.around(100*(eta1/dh2), 1), '&', np.around(100*(l2 - 2*eta1)/li2, 1), '&', np.around(100*(l2 - 2*ETA)/li2, 1), '\\\\')
print(3, '&', np.around(dh3, 4), '&', np.around(100*(eta2/dh3), 1), '&', np.around(100*(l3 - 2*eta2)/li3, 1), '&', np.around(100*(l3 - 2*ETA)/li3, 1), '\\\\')
print(4, '&', np.around(dh4, 4), '&', np.around(100*(eta2/dh4), 1), '&', np.around(100*(l4 - 2*eta2)/li4, 1), '&', np.around(100*(l4 - 2*ETA)/li4, 1), '\\\\')
print(5, '&', np.around(dh5, 4), '&', np.around(100*(eta2/dh5), 1), '&', np.around(100*(l5 - 2*eta2)/li5, 1), '&', np.around(100*(l5 - 2*ETA)/li5, 1), '\\\\')
