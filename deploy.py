from azureml.core import Workspace, Model
from azureml.core.webservice import AciWebservice
from azureml.core.model import InferenceConfig
from azureml.core.environment import Environment
from azureml.core.model import Model

# Carrega o workspace do Azure
ws = Workspace.from_config()

# Carrega o modelo registrado
model_name = 'diabetes-regression-model'
model = Model(workspace=ws, name=model_name)

# Configura o ambiente de inferência
env = Environment.get(workspace=ws, name='AzureML-sklearn-0.24-ubuntu18.04-py37-cpu')
inference_config = InferenceConfig(entry_script='score.py', environment=env)

# Implantação do modelo como serviço web ACI (Azure Container Instances)
service_name = 'diabetes-regression-service'
deployment_config = AciWebservice.deploy_configuration(cpu_cores=1, memory_gb=1)
service = Model.deploy(workspace=ws,
                       name=service_name,
                       models=[model],
                       inference_config=inference_config,
                       deployment_config=deployment_config)

service.wait_for_deployment(show_output=True)
print(service.state)
