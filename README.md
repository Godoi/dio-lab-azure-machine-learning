# Modelo de Previsão com Azure Machine Learning
Este repositório contém um exemplo de como treinar, implantar e consumir um modelo de previsão utilizando o Azure Machine Learning. O modelo é treinado para fazer previsões com base em um conjunto de dados de diabetes.

## Passos para Treinamento e Registro do Modelo
### Treinamento do Modelo:
  - O modelo é treinado usando o script train.py. Este script utiliza a biblioteca scikit-learn para treinar um modelo de regressão linear com dados de diabetes.

### Registro do Modelo no Azure Machine Learning:
 - Após o treinamento, o modelo é registrado no Azure Machine Learning. O script register_model.py realiza esse registro, tornando o modelo disponível para implantação.

## Implantação do Modelo e Configuração do Ponto de Extremidade
### Configuração do Ponto de Extremidade:
- O ponto de extremidade é configurado utilizando o Azure Container Instances (ACI). O script deploy.py cuida dessa implantação, configurando o ambiente de inferência e criando o ponto de extremidade do serviço web.

## Consumo do Ponto de Extremidade com Arquivo .json
### Chamada do Ponto de Extremidade com Dados de Entrada .json:
- Agora, você pode consumir o ponto de extremidade para fazer previsões. O arquivo input_data.json contém um exemplo de dados de entrada. Utilize o script call_endpoint.py para chamar o ponto de extremidade, fornecendo dados de entrada a partir desse arquivo .json.

#### Obs: Este exemplo fornece uma estrutura básica
