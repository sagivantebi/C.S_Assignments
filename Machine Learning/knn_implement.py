import numpy as np # linear algebra
import matplotlib.pyplot as plt

def euclidean_distance(p1, p2):
  return np.linalg.norm(p1 - p2)


from collections import Counter
class KNeighborsClassifier:
  def __init__(self, distance_metric=None, n_neighbors=None):
    self.k = n_neighbors
    self.distance_metric = []

  def fit(self, x, y):
    self.x = x
    self.y = y

  def predict(self, x_test):
    predictions =[self._predict(x_one_sample) for  x_one_sample in x_test]
    return np.array(predictions)
  
  def _predict(self,  x_one_sample):
    #compute distances metric
    distance_metric = [euclidean_distance(x_one_sample,x_train) for x_train in self.x]
    # get k nearest neighbors
    k_neighbors = np.argsort(distance_metric[:self.k])
    k_nearest_neighbors_lables = [self.y[i] for i in k_neighbors]
    # find most common neighbor and decide
    most_common = Counter(k_nearest_neighbors_lables).most_common()
    return most_common[0][0]

def error_rate(y_predict, y_true):
  return np.mean(y_predict != y_true)

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(x_train,y_train)

pred = knn.predict(x_test)
from sklearn.metrics import classification_report,confusion_matrix
print(confusion_matrix(y_test,pred))
print(classification_report(y_test,pred))

MIN_K = 1
MAX_K = 15

def find_best_k(min_k=1, max_k=15):
  testing_accuracy = []
  for num_neighbors in range(min_k,max_k):
    knn = KNeighborsClassifier(n_neighbors=num_neighbors)
    knn.fit(x_train,y_train)
    predict = knn.predict(x_test)
    error_r = error_rate(predict,y_test)
    testing_accuracy.append(error_r)
  arr = np.array(testing_accuracy)
  return [testing_accuracy.index(min(testing_accuracy)) + 1,arr]
  
best_k, error_rate = find_best_k(min_k=MIN_K, max_k=MAX_K)

plt.figure(figsize=(10,6))
plt.plot(range(MIN_K,MAX_K),error_rate,color='blue',linestyle='dashed', marker='o',
         markerfacecolor='red', markersize=10)
plt.title('Error rate vs K')
plt.xlabel('K')
plt.ylabel('Error rate')

knn = KNeighborsClassifier(best_k)
knn.fit(x_train,y_train)
pred = knn.predict(x_test)

print(confusion_matrix(y_test,pred))
print(classification_report(y_test,pred))

  