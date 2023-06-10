# WEAT
Replicação de "Implementation of WEAT (and WEFAT) (Caliskan et al., 2017)."

Como usar:

Primeiro, visite http://nilc.icmc.usp.br/nilc/index.php/repositorio-de-word-embeddings-do-nilc para baixar o modelo pré-treinado em português. Os embeddings na pasta data usa GloVe de 300 dimensões. Baixe o arquivo txt e coloca no diretório raiz.

Instale os pacotes em requirements.txt com pip install.

Depois rode o comando com:

python main.py --data_file_name DATA_FILE_NAME --embedded_data_file_name EMBEDDED_DATA_FILE_NAME --glove_file_name GLOVE_FILE_NAME --wefat_association_file_name WEFAT_ASSOCIATION_FILE_NAME --test TEST --iterations N --distribution_type DISTRIBUTION_TYPE

Onde: <br>
    DATA_FILE_NAME: nome dos arquivos de palavras-alvo/atributos. Neste exemplo: os arquivos data/weat_...json para rodar no teste WEAT ou data/wefat_1.json para rodar o teste WEFAT.<br>
    EMBEDDED_DATA_FILE_NAME: nome do arquivo onde é armazenado os embeddings das palavras dos testes. Informe um nome identificador, que o algoritmo irá criar caso não existir. (Neste caso, não é necessário criar à priori) <br>
    GLOVE_FILE_NAME: nome do arquivo txt do GloVe; obrigatório caso o arquivo de EMBEDDED_DATA_FILE_NAME não exista<br>
    WEFAT_ASSOCIATION_FILE_NAME: Arquivo usado para o teste WEFAT onde contém o mapeamento das profissões para dos dados do mundo real que você deseja analisar. Neste exemplo, data/wefat_1_percentage_women.json utiliza as proporções de mulheres no mercado de trabalho brasileiro. <br>
    TEST: WEAT ou WEFAT <br>
    N: número de interações para calcular o valor-p. <br>
    DISTRIBUTION_TYPE: tipo de distribuição usada para calcular o valor-p (normal ou empirical)<br>
    
## WEAT
Mostra o effect size e o valor-p.

## WEFAT
Mostra o gráfico da teste estatístico com as estatísticas do mundo real junto com o coeficiente de correlação de Pearson.
Caso o wefat_assocation_file_name foi especificado. Caso contrário, mostra o effect size e o valor-p para cada palavra de atributo.

## Referências
Caliskan, A., Bryson, J. J., & Narayanan, A. (2017). Semantics derived automatically from language corpora contain human-like biases. Science, 356(6334), 183–186. https://doi.org/10.1126/science.aal4230<br>
<br>
Pennington, J. (2014). GloVe: Global Vectors for Word Representation. Stanford.edu. https://nlp.stanford.edu/projects/glove/<br>
<br>
Guide to Using Pre-trained Word Embeddings in NLP. (2021, June 1). Paperspace Blog. https://blog.paperspace.com/pre-trained-word-embeddings-natural-language-processing/#using-glove-word-embeddings<br>
<br>
U.S. Bureau of Labor Statistics. (2019, January 18). Employed persons by detailed occupation, sex, race, and Hispanic or Latino ethnicity. Bls.gov. https://www.bls.gov/cps/cpsaat11.htm<br>
<br>
Toney-Wails, A., & Caliskan, A. (2021). ValNorm Quantifies Semantics to Reveal Consistent Valence Biases Across Languages and Over Centuries. ArXiv:2006.03950 [Cs]. https://arxiv.org/abs/2006.03950<br>
<br>
Caliskan, A. (2017). Replication Data for: WEFAT and WEAT(UNF:6:C9yaa+UeGfFmtuHz734iKw==, V2). [Data set]. Harvard Dataverse. https://doi.org/10.7910/DVN/DX4VWP<br>
