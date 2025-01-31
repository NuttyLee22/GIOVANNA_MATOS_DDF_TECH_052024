# Case Técnico - GIOVANNA_MATOS_DDF_TECH_052024
Case técnico para vaga Engenharia de Soluções com foco em Engenharia de Dados

## Introdução ao case

Como Profissional de Dados na Dadosfera, você irá construir projetos de implementação da plataforma Dadosfera SaaS, em uma empresa, buscando centralizar diversas fontes de dados para aprimorar a tomada de decisões, eficiência operacional e análise estratégica. Após um kickoff bem-sucedido com o cliente, é hora de dar sequência à execução do projeto, enfrentando os desafios específicos delineados pelo cliente.

Seu cliente, uma grande empresa de e-commerce, está com um projeto de contruir uma Plataforma de Dados, com o objetivo de entregar análises descritivas e prescritivas com maior agilidade, menor custo, em todas as áreas da empresa.

PARA O CASE, VOCÊ DEVE PROPOR UMA BASE DE DADOS QUE CONHEÇA E QUE SE ENCAIXE NA NARRATIVA ACIMA.


## Item 0 - Sobre Agilidade e Planejamento

Crie um artefato que represente todas as etapas do projeto, desde a concepção até a implementação, seguindo as melhores práticas do PMBOK. Pode ser, tanto um gantt chart, um fluxograma, um checklist de tarefas ou um kanban board com as tarefas planejadas. Adicione esse fluxograma na documentação do case.

Avançado: Incluir análises de risco, estimativas de custos, e alocação de recursos.
Avançado: Representar interdependências e pontos críticos do projeto.

Link Trello:

    https://trello.com/invite/b/FtcdY7eq/ATTIc37a7cce8eabd4fa1da65036f5ea8627000BEA54/case-engenharia-de-dados

![image](https://github.com/NuttyLee22/GIOVANNA_MATOS_DDF_TECH_052024/assets/68132085/db2f393e-6adc-4cae-9d1a-3efe46f21cc5)

![image](https://github.com/NuttyLee22/GIOVANNA_MATOS_DDF_TECH_052024/assets/68132085/c7d40f1b-bc82-4c58-b360-cc53d21a6baa)


## Item 1 - Sobre a Base de Dados

Seguindo o cenário proposto na definição do Case, pesquise e sugira uma base de dados para fazer todo case ponta a ponta.

Base sugerida: 

    https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce?resource=download

![image](https://github.com/NuttyLee22/GIOVANNA_MATOS_DDF_TECH_052024/assets/68132085/b1cf38b9-7735-4e7b-a01d-930f32b43585)


## Item  2.1 - Sobre a Dadosfera - Integrar

Vamos iniciar com o carregamento e posterior análise descritiva dos dados propostos. Utilizando o módulo de Coleta da Dadosfera, conecte a sua base de dados proposta e suba esses dados para a Plataforma.

Lembre-se: você deve carregar, pelo menos, 100.000 registros para que seu case seja avaliado por completo.

Os datasets também estão presentes no caminho: Docs/datasets/Brazilian_E-Commerce_Public_Dataset_by_Olist

    https://github.com/NuttyLee22/GIOVANNA_MATOS_DDF_TECH_052024/tree/main/Docs/datasets/Brazilian_E-Commerce_Public_Dataset_by_Olist

Link:

    https://app.dadosfera.ai/en-US/catalog/data-assets

![print7](https://github.com/NuttyLee22/GIOVANNA_MATOS_DDF_TECH_052024/assets/68132085/b0353469-4fef-4348-b0e2-a98679a830a5)

![print8](https://github.com/NuttyLee22/GIOVANNA_MATOS_DDF_TECH_052024/assets/68132085/120bade1-46b7-45b9-a2f5-506836d2e258)


## Item  3 - Sobre a Dadosfera - Explorar

Usando os seus conhecimentos da documentação da Dadosfera, faça a carga desse dataset, catalogue-o com as informações mais relevantes, seguindo boas práticas de Dicionário de Dados.

![print4](https://github.com/NuttyLee22/GIOVANNA_MATOS_DDF_TECH_052024/assets/68132085/9ee526be-44da-40b7-8c0e-a3f49d1e0f39)


## Item 4 - Sobre Data Quality

Após a integração e exploração dos dados do site de e-commerce, você identificou várias inconsistências e dados faltantes que podem impactar negativamente a performance dos modelos de IA e a experiência de compra dos clientes. Como você abordaria a melhoria da qualidade desses dados utilizando as ferramentas e práticas recomendadas pela Dadosfera?

    1. Limpeza de Dados:

    Implementação de técnicas de Limpeza de Dados para corrigir erros, remover duplicatas e preencher valores ausentes. 
    Utilizar regras de negócios e conhecimento do domínio para garantir a consistência e precisão dos dados.

    2. Enriquecimento de Dados:

    Enriquecer os dados do e-commerce com informações de fontes externas, como dados demográficos, comportamentais e de mercado, 
    para aprimorar a análise e a tomada de decisões.Também podemos utilizar técnicas de Machine Learning para imputar valores faltantes 
    de forma inteligente e precisa.

Gere um relatório de qualidade dos dados usando uma biblioteca apropriada - great-expectations ou soda-core -  para identificar inconsistências e dados faltantes.

Arquivo: src/checagem_qualidade_dados/data_quality.py

    https://github.com/NuttyLee22/GIOVANNA_MATOS_DDF_TECH_052024/blob/main/src/checagem_qualidade_dados/data_quality.py

![image](https://github.com/NuttyLee22/GIOVANNA_MATOS_DDF_TECH_052024/assets/68132085/41e13105-93ea-4d0f-89b3-05429f0e232d)

![image](https://github.com/NuttyLee22/GIOVANNA_MATOS_DDF_TECH_052024/assets/68132085/5b26f91b-9cac-476a-9314-e8aa3374519c)


*OBS: Não foi possível gerar o arquivo do relatório devido à inconsistencias com a instalação das bibliotecas soda-core e great-expectations*

## Item 5 - Sobre o uso de GenAI e LLMs - Processar

Traga um dataset desestruturado e, utilizando IA, gere features em cima desses dados.

Uso do Google AI Studio para gerar os features:

![image](https://github.com/NuttyLee22/GIOVANNA_MATOS_DDF_TECH_052024/assets/68132085/b41a8e21-3d01-4877-b346-3fb243e9f7b6)

Resultado:

![image](https://github.com/NuttyLee22/GIOVANNA_MATOS_DDF_TECH_052024/assets/68132085/662be532-c006-43b5-8842-4bbd4a457402)


Arquivo disponível em: Docs/features_product_search_corpus/features-product-search-corpus.md

    https://github.com/NuttyLee22/GIOVANNA_MATOS_DDF_TECH_052024/blob/main/Docs/features_product_search_corpus/features-product-search-corpus.md

## Item 6 - Sobre Modelagem de Dados

Com os dados importados, precisamos propor uma modelagem de dados que seja condizente com o cenário dos dados e do cliente.

Crie um modelagem seguindo os princípios de Kimball, Data Vault ou outro - que deve ser explicado e justificado - com 2 visões finais dos dados.

Bonus: desenhe o diagrama representando as camadas finais do DW proposto.

Arquivo: Docs/modelagem_dados_brazil_ecommerce_olist

    https://github.com/NuttyLee22/GIOVANNA_MATOS_DDF_TECH_052024/tree/main/Docs/modelagem_dados_brazil_ecommerce_olist

![ecommerce-olist](https://github.com/NuttyLee22/GIOVANNA_MATOS_DDF_TECH_052024/assets/68132085/e9a05315-242e-4f09-a164-f3855f775ca6)

![image](https://github.com/NuttyLee22/GIOVANNA_MATOS_DDF_TECH_052024/assets/68132085/a9786dd7-10b1-4197-8bf7-cb84990c2a1f)


## Item  7 - Sobre Análise de Dados - Analisar

Crie uma Coleção com o formato <nome> <sobrenome> - <mes_ano> assim como no exemplo:

Crie um dashboard que mostre uma análise das categoria e uma análise de série-temporal. Salve a Query SQL utilizada e também o print do resultado da query no documento markdown deste teste. Crie, pelo menos, 5 visualizações/questões em cima dos dados, utilizando 5 tipos de visualizações diferentes.

Link Coleção:

    https://metabase-treinamentos.dadosfera.ai/collection/471-giovanna-matos-052024

![print3](https://github.com/NuttyLee22/GIOVANNA_MATOS_DDF_TECH_052024/assets/68132085/2abb0b9f-b7ab-4c34-9c02-8e502f73a674)

Exemplo de Query: 

    https://metabase-treinamentos.dadosfera.ai/question/966-lucro-de-vendas-por-estado

![image](https://github.com/NuttyLee22/GIOVANNA_MATOS_DDF_TECH_052024/assets/68132085/0c9b7f77-6dab-48fb-ab29-23b32b12b33e)


Link Dashboard:

    https://metabase-treinamentos.dadosfera.ai/dashboard/109-dash-vendas-ecommerce-olist

![image](https://github.com/NuttyLee22/GIOVANNA_MATOS_DDF_TECH_052024/assets/68132085/8bbd7e10-ba98-45f9-800b-182f61074cd7)

![image](https://github.com/NuttyLee22/GIOVANNA_MATOS_DDF_TECH_052024/assets/68132085/167a4286-e70d-4353-ba07-16a761836e12)

![image](https://github.com/NuttyLee22/GIOVANNA_MATOS_DDF_TECH_052024/assets/68132085/351b432b-2d33-46cd-b3a0-f40713a40f2d)

![image](https://github.com/NuttyLee22/GIOVANNA_MATOS_DDF_TECH_052024/assets/68132085/11f6ccb4-418a-4cbe-bef8-43e5e6af0237)


## Item  8 - Sobre Pipelines

Uma das etapas essenciais de um projeto de Dados é a criação de Pipelines de Dados. Desde o processo de criação de modelos inteligentes, utilizando-se de Machine Learning, até a Engenharia de Dados, com Pipelines de Transformação e Limpeza de Dados.

Agora você tem que criar um pipeline para processar os dados anteriores. Para criar um pipeline, acesse nosso módulo de inteligência e siga este guia na nossa documentação.

Link:

    https://app-intelligence-treinamentos.dadosfera.ai/pipeline?project_uuid=a0229280-a34c-47ff-9bc5-cdbed3e4ae5e&pipeline_uuid=a16d4e62-14f4-4d6e-a81b-00b8bc2f366a

![image](https://github.com/NuttyLee22/GIOVANNA_MATOS_DDF_TECH_052024/assets/68132085/4330def2-fbb1-44ac-af04-3e944e969d7a)

## Item  9 - Sobre Data Apps

Agora você tem que criar um Data App utilizando Streamlit para explorar os dados anteriores. Para criar um Data App, acesse nosso módulo de inteligência e siga este guia na nossa documentação. 

Link:

    https://app-intelligence-treinamentos.dadosfera.ai/pipeline?project_uuid=a0229280-a34c-47ff-9bc5-cdbed3e4ae5e&pipeline_uuid=a16d4e62-14f4-4d6e-a81b-00b8bc2f366a

![image](https://github.com/NuttyLee22/GIOVANNA_MATOS_DDF_TECH_052024/assets/68132085/33611ba7-cbe2-4998-8508-b3b1b8bdd836)

![image](https://github.com/NuttyLee22/GIOVANNA_MATOS_DDF_TECH_052024/assets/68132085/0128c509-8c54-44f3-95f7-db6be7c8654e)

Link:

    https://app-intelligence-treinamentos.dadosfera.ai/pipeline?project_uuid=80b7938b-d4fa-4e63-9b1e-a5b040eb7812&pipeline_uuid=13858f16-44ec-4c17-ae6b-a0714df69f0c

![print5](https://github.com/NuttyLee22/GIOVANNA_MATOS_DDF_TECH_052024/assets/68132085/038bc9e5-518f-42ae-9258-70098e3e4392)

![image](https://github.com/NuttyLee22/GIOVANNA_MATOS_DDF_TECH_052024/assets/68132085/e866973b-aade-402b-be8c-3c912ada4a15)

![print6](https://github.com/NuttyLee22/GIOVANNA_MATOS_DDF_TECH_052024/assets/68132085/e5a1a796-903a-4c3f-bf00-5c0e05ed5d93)



## Item 10 - Apresentação do Case

Após a primeira reunião com nossa equipe de vendas, você deve fornecer uma solução técnica que atenda às exigências e se encaixe na arquitetura deles. Aqui está o diagrama da arquitetura atual deles:

![Untitled](https://github.com/NuttyLee22/GIOVANNA_MATOS_DDF_TECH_052024/assets/68132085/f409d986-14ae-4101-9e3a-3950801c10dc)

Você deve mostrar, com base nos seus estudos sobre a Documentação da Dadosfera, a viabilidade de substituirmos essa solução pelo case construído.

Link Vídeo:

    https://youtu.be/C9TU6HnjSRM


## Item Bonus - Sobre GenAI + Data Apps

Utilize este Data App como referência para criar um gerador de apresentações de produto. Seu objetivo é chegar em uma apresentação para mostrar as principais características do Produto a fim de vender mais. Utilize a API do Dall-e ou outro gerador de imagens para gerar uma imagem do produto. No notebook, documente em separado os prompts utilizados. 
Exemplo de uso do Dall-e aqui:

![Untitled](https://github.com/NuttyLee22/GIOVANNA_MATOS_DDF_TECH_052024/assets/68132085/79d72d7a-6626-4e5a-af53-8e55c99ffda3)

Link: 

    https://app-intelligence-treinamentos.dadosfera.ai/jupyter-lab?project_uuid=80b7938b-d4fa-4e63-9b1e-a5b040eb7812&pipeline_uuid=13858f16-44ec-4c17-ae6b-a0714df69f0c&

![image](https://github.com/NuttyLee22/GIOVANNA_MATOS_DDF_TECH_052024/assets/68132085/50f08908-20ff-437b-81f6-377457d58f04)

