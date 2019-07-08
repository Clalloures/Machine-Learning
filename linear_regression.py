from sklearn import linear_model, datasets

#digit dataset from sklearn
digits = datasets.load_digits()

#create the LinearRegression model
clf = linear_model.LinearRegression()

#set training set
x, y = digits.data[:-1], digits.target[:-1]

#train model
clf.fit(x, y)

#predict
y_pred = clf.predict([digits.data[-1]])
y_true = digits.target[-1]

print(y_pred)
print(y_true)
