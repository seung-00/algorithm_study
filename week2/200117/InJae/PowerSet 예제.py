import pandas as pd
import matplotlib.pyplot as plt
csv_path = r"C:\Users\Ju\Desktop\빅데이터 공부\핸즈온 머신러닝 스터디\chapter2\housing.txt"

housing = pd.read_csv(csv_path)

pd.set_option('display.max_columns', 500)

housing.head()

housing.describe()

housing.hist(bins = 50, figsize=(20,15))
plt.show()


#test set 만들기
import numpy as np

def split_train_test(data, test_ratio):
    np.random.seed(42)
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data)*test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]

    return data.iloc[train_indices], data.iloc[test_indices]

train_set, test_set = split_train_test(housing, 0.2)
print(len(train_set), "train + ", len(test_set), "test")


#무작위 트레이닝, 테스트셋 나누기
from sklearn.model_selection import train_test_split

train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)
##################

#층화추출하기
    #중간소득이 주택가격 예측에 매우 중요하므로 카테고리 특성으로 만들어서 층화추출에 적용하기.
housing["income_cat"] = np.ceil(housing["median_income"] / 1.5)
#where은 condition을 만족하지 않은 값을 대체해줌. inplace는 boolean값에서 False는 True로 변경
housing["income_cat"].where(housing["income_cat"] < 5, 5.0, inplace=True)
housing["income_cat"].hist()
plt.show()

    #사이킷 런에서 계층추출

from sklearn.model_selection import StratifiedShuffleSplit

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]

    #income_cat 특성 삭제하여 원상 복구
for set_ in (strat_train_set, strat_test_set):
    set_.drop("income_cat", axis = 1, inplace = True)

#train_set만을 다루기
housing = strat_train_set.copy()

#지리적 데이터 시각화
housing.plot(kind="scatter", x="longitude", y= "latitude")
plt.show()

#밀집지역 확인 alpha 값 부여
housing.plot(kind="scatter", x="longitude", y= "latitude", alpha = 0.1)
plt.show()

#주택가격 나타내기
housing.plot(kind="scatter", x="longitude", y ="latitude", alpha = 0.4,
             s=housing["population"]/100, label="population", figsize=(10,7),
             c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True, sharex = False
             )
plt.legend()
plt.show()

#상관관계 조사
corr_matrix = housing.corr()

corr_matrix["median_house_value"].sort_values(ascending = False)

#산점도행렬그리기
from pandas.plotting import scatter_matrix
attributes = ["median_house_value","median_income", "total_rooms", "housing_median_age"]
scatter_matrix(housing[attributes], figsize=(12, 8))
plt.show()

housing.plot(kind="scatter", x="median_income", y="median_house_value", alpha=0.1)
plt.show()

#특성조합
housing["rooms_per_household"] = housing["total_rooms"]/housing["households"]
housing["bedrooms_per_room"] = housing["total_bedrooms"]/housing["total_rooms"]
housing["population_per_household"] = housing["population"]/housing["households"]

corr_matrix = housing.corr()
corr_matrix["median_house_value"].sort_values(ascending=False)
####

#데이터 준비
housing = strat_train_set.drop("median_house_value", axis = 1)
housing_labels = strat_train_set["median_house_value"].copy()

#데이터 정제. na값 처리
housing.dropna(subset=["total_bedrooms"]) #해당 구역 제거 (행삭제)
housing.drop("total_bedrooms",axis=1) #전체 특성 삭제 (열삭제)
median = housing["total_bedrooms"].median() #특정값 채우기. (메디안으로 채움)
housing["total_bedrooms"].fillna(median, inplace = True) #na값을 메디안으로 저장

#sklearn으로 쉽게 누락된 값 다루기
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy="median")

housing_num = housing.drop("ocean_proximity",axis=1)

imputer.fit(housing_num)

    #비교
imputer.statistics_
housing_num.median().values

    #채우기
X = imputer.transform(housing_num)

housing_tr = pd.DataFrame(X, columns=housing_num.columns,
                          index = list(housing.index.values))

########

#범주형 데이터 다루기
housing_cat = housing["ocean_proximity"]
housing_cat.head(10)

housing_cat_encoded, housing_categories = housing_cat.factorize()

#숫자로 된 범주형 값을 원-핫 벡터로 바꿔주는 OneHotEncoder 사용하기
from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder(categories = 'auto')
housing_cat_1hot = encoder.fit_transform(housing_cat_encoded.reshape(-1,1)) #-1은 차원지정하지 않음,

#텍스트 카테고리->숫자, 숫자를 원핫바꿔주는 변환 동시처리
#104p 옮긴이 41에서 pd.get_dummies(housing)으로 간단히 처리 가능.
    #sklearn에 class없네;

h = pd.get_dummies(housing)

housing.columns

from sklearn.base import BaseEstimator, TransformerMixin

rooms_ix, bedrooms_ix, population_ix, household_ix = 3, 4, 5, 6


class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room=True):  # *args나 **kargs가 아닙니다.
        self.add_bedrooms_per_room = add_bedrooms_per_room

    def fit(self, X, y=None):
        return self  # 더 할 일이 없습니다.

    def transform(self, X, y=None):
        rooms_per_household = X[:, rooms_ix] / X[:, household_ix]
        population_per_household = X[:, population_ix] / X[:, household_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household, bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]

attr_adder = CombinedAttributesAdder(add_bedrooms_per_room=False)
housing_extra_attribs = attr_adder.transform(housing.values)

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

num_pipeline = Pipeline([('imputer',SimpleImputer(strategy='median')),
                         ('attribs_adder', CombinedAttributesAdder()),
                         ('std_scaler', StandardScaler()),
                         ])


housing_num_tr = num_pipeline.fit_transform(housing_num)

from sklearn.base import BaseEstimator, TransformerMixin

class DataFrameSelector(BaseEstimator, TransformerMixin):
    def __init__(self,attribute_names):
        self.attributes_names = attribute_names
    def fit(self,X,y=None):
        return self
    def transform(self, X):
        return X[self.attributes_names].values

from sklearn.pipeline import FeatureUnion

full_pipeline = FeatureUnion(transformer_list = [
    ("DataFrameSelector", DataFrameSelector),
    ("num_pipeline", num_pipeline),
])

