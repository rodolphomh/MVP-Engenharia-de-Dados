# MVP-Engenharia-de-Dados

Esse é meu projeto de análise de dados focado em Churn (evasão de clientes). O objetivo aqui foi entender os motivos que levam os clientes de uma empresa de telecomunicações a cancelar os seus serviços e, a partir daí, propor estratégias de retenção baseadas em dados.

Estruturei este projeto em duas grandes etapas para simular um ambiente real de engenharia e análise:

1. Engenharia de Dados (ETL no Databricks)
Para garantir a escalabilidade, utilizei a plataforma Databricks.

Organizei os dados em camadas (Bronze para os dados brutos e Gold para os dados limpos).

Realizei todo o tratamento utilizando SQL, onde fiz a renomeação de colunas, conversão de tipos (como transformar o tenure em inteiro) e padronização de categorias (como transformar indicadores de idosos em 'Sim'/'Não').

Nota: Como utilizo a versão gratuita do Databricks, exportei o resultado final para o meu GitHub para garantir que a análise no Colab funcione sempre.

2. Análise Exploratória e Insights (Google Colab)
Com os dados já tratados, utilizei este notebook para realizar a análise diagnóstica. Foquei em:

Visualização de Dados: Usei Seaborn e Matplotlib para criar gráficos que facilitam a leitura dos padrões.

Durante a análise, descobri pontos críticos que impactam o negócio:

Contratos: Percebi que clientes com contratos mensais têm uma propensão ao churn muito maior (42.7%) do que aqueles com contratos de dois anos (2.8%).

Suporte Técnico: Notei que clientes que não utilizam o suporte técnico cancelam quase 3 vezes mais do que os que utilizam.

Métodos de Pagamento: Clientes que pagam via "Cheque Eletrônico" representam a maior fatia de evasão.

Desenvolvido por Rodolpho Hruby. Este projeto faz parte do meu projeto de Engenharia e Análise de Dados.
