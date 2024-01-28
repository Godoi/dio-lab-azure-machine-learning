from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from azureml.core import Workspace, Experiment, Model

# Carrega o conjunto de dados de diabetes
diabetes = load_diabetes()
X_train, X_test, y_train, y_test = train_test_split(diabetes.data, diabetes.target, test_size=0.2, random_state=42)

# Treina um modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)

# Avalia o modelo
accuracy = model.score(X_test, y_test)
print(f'Acurácia do modelo: {accuracy}')

# Registra o modelo no Azure Machine Learning
ws = Workspace.from_config()
experiment = Experiment(workspace=ws, name='diabetes-regression')
run = experiment.start_logging()
model_name = 'diabetes-regression-model'
Model.register(workspace=ws, model_path='.', model_name=model_name)
run.complete()
