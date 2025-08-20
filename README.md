# Fine tuning of a BERT model in Spanish for the task of multiclass classification  

## Project Description  

This project extracts, processes, and classifies Spanish-language communications using BERT-based NLP models with PyTorch Lightning. Its goal is to automatically categorize messages, enabling efficient organization and analysis of large text corpora.

## Study Summary  

> **In this project, we present the tuning and adaptation of BERT, a pre-trained Transformer-based model, with the objective of improving classification performance in natural language processing.**  

The study focuses on a dataset from Sinco, a communication management platform where users raise various issues and situations. A major challenge identified was __class imbalance__ due to the diversity of situations presented. 

To address this, we applied data-processing techniques such as __oversampling__, __undersampling__, and __weight assignment__ to balance the distribution of examples across classes.  

We then adapted BERT by adding __neural network layers__ and tuning hyperparameters (learning rate, activation functions). These adaptations were evaluated both on the balanced dataset and on the original data. The best results—79 % accuracy, 80 % recall, and a 79 % F1-score—were obtained by assigning class weights. These outcomes demonstrate the methodology’s potential given the data’s complexity and class diversity.

## Repository Structure  

01-Data_extraction_sinco.ipynb  :arrow_right: Jupyter notebook for data extraction and preprocessing  

02-Data_Analysis.ipynb :arrow_right:
 Exploratory Data Analysis (EDA) and visualizations  

03-Bert_clasification_models.ipynb :arrow_right: Models implementation and training with PyTorch Lightning  

datos_sinco.xlsx :arrow_right:
Original dataset (not versioned)  

filtered_dataset.xlsx :arrow_right: Cleaned/filtered dataset (not versioned)

categories.py :arrow_right: Helper logic module (ignored by Git)

env :arrow_right: Python virtual environment directory  

__pycache__ :arrow_right: Python cache directory (ignored)  

requirements.txt :arrow_right:
 List of Python dependencies  

## Requirements & Setup  

- Python 3.8+  
- Git  
- (Optional) GPU for faster training  

*Clone the repository and install dependencies:*

```sh
git clone https://github.com/Margy-Garzon/FineTuning_Bert.git 
cd FineTuning_Bert
git clone
cd app
python3 -m venv env
source env/bin/activate
pip3 install -r requitements.txt
```

## Workflow  

1. __01-Data_extraction_sinco.ipynb__

    - Run all cells to extract and preprocess raw data.  
    - Generates `datos_sinco.xlsx`.  

2. __02-Data_Analysis.ipynb__

    - Explore and visualize the preprocessed dataset.  

3. __03-Bert_clasification_models.ipynb__

    - Define and train the BERT-based classifier.  
    - Evaluate model performance and generate classification metrics.

## Contributing  

Contributions are welcome!  

- Open an Issue for bugs or feature requests.  
- Submit a Pull Request with improvements.

## More information

For more information consulting the next paper in the link:  <https://www.researchgate.net/publication/393703307_MODELO_DE_APRENDIZAJE_AUTOMATICO_BASADO_EN_BERT_EN_ESPANOL_PARA_LA_CLASIFICACION_MULTICLASE_DE_LAS_COMUNICACIONES_DE_SINCO>

## Authors

- [@margy-garzon](https://www.linkedin.com/in/margy-garzon/)