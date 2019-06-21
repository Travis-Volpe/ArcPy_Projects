#Everything Together

from sklearn.datasets import load_boston
from sklearn.linear_model import (LinearRegression, Ridge,
                                  Lasso, RandomizedLasso)
from sklearn.feature_selection import RFE, f_regression
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
import numpy as np
from minepy import MINE

np.random.seed(0)

#names = pd.DataFrame(X.columns.values)
prenames = pd.DataFrame(X)
names = list(X.columns)
#names = ["x%s" % i for i in range(0, 199)]

X = df.iloc[:, 1:200]
y = df.isAlive

ranks = {}

def rank_to_dict(ranks, names, order=1):
    minmax = MinMaxScaler()
    ranks = minmax.fit_transform(order*np.array([ranks]).T).T[0]
    ranks = list([map(lambda x: round(x, 2), ranks)])
    return dict(zip(names, ranks ))

lr = LinearRegression(normalize=True)
lr.fit(X, y)
ranks["Linear reg"] = rank_to_dict(np.abs(lr.coef_), names)

ridge = Ridge(alpha=7)
ridge.fit(X, y)
ranks["Ridge"] = rank_to_dict(np.abs(ridge.coef_), names)

lasso = Lasso(alpha=.05)
lasso.fit(X, y)
ranks["Lasso"] = rank_to_dict(np.abs(lasso.coef_), names)

rlasso = RandomizedLasso(alpha=0.04)
rlasso.fit(X, y)
ranks["Stability"] = rank_to_dict(np.abs(rlasso.scores_), names)

#stop the search when 5 features are left (they will get equal scores)
rfe = RFE(lr, n_features_to_select=5)
rfe.fit(X, y)
ranks["RFE"] = rank_to_dict(list(map(float, rfe.ranking_)), names, order=-1)

rf = RandomForestRegressor()
rf.fit(X, y)
ranks["RF"] = rank_to_dict(rf.feature_importances_, names)

f, pval  = f_regression(X, y, center=True)
ranks["Corr."] = rank_to_dict(f, names)

mine = MINE()
mic_scores = []
for i in range(X.shape[1]):
    mine.compute_score(X.iloc[:,i], y)
    m = mine.mic()
    mic_scores.append(m)

ranks["MIC"] = rank_to_dict(mic_scores, names)

r = {}
for name in names:
    r[name] = list(round(np.mean([ranks[method][name]
                             for method in ranks.keys()]), 2))

methods = sorted(ranks.keys())
ranks["Mean"] = r
methods.append("Mean")

print("\t%s" % "\t".join(methods))
for name in names:
    print("%s\t%s" % (name, "\t".join(list(map(str,
                         [ranks[method][name] for method in methods])))))
