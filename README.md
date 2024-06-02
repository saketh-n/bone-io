# Gene Expression Pathways in Bone Growth and Remodeling

## Objective

The objective of this project is to analyze gene expression data to identify pathways and genes involved in bone growth and remodeling. Understanding these pathways can provide insights into bone-related diseases and potential therapeutic targets.

## Achievements

### Data Loading

- Successfully loaded various datasets from the Gene Expression Omnibus (GEO).
- Manually downloaded Annotation, Full and Series family metadata files
- [Example dataset](https://www.ncbi.nlm.nih.gov/sites/GDSbrowser?acc=GDS5519)
- *load_data.py*

### Data Preprocessing

- Cleaned and normalized the data to ensure it was ready for analysis.
- *preprocess_data.py*

### Exploratory Data Analysis (EDA)

- Performed descriptive statistics and visualizations to understand the data distribution.
- Generated histograms and box plots for numerical columns.
- *eda.py*

### Correlation Analysis and Statistical Testing

- Conducted correlation analysis to identify relationships between gene expressions.
- Performed statistical tests (t-tests and ANOVA) to identify significant differences in gene expression related to bone growth and remodeling.
- Handled large datasets and ensured sufficient data for statistical tests.
- *analysis.py*

## Next Steps

### Correlation Analysis and Statistical Testing
1. **Optimization**
   - Runs quite slow for 1.7 GB of Data, how to speed up?

### Pathway and Functional Analysis

1. **Gene Ontology (GO) Enrichment Analysis:**
   - Identify overrepresented GO terms in the significant genes.

2. **Pathway Analysis:**
   - Use tools like KEGG or Reactome to map gene expression data to biological pathways.
   - Perform and interpret these analyses to uncover pathways involved in bone growth and remodeling.

### Model Development

1. **Predictive Modeling:**
   - Develop predictive models (e.g., regression, machine learning) to identify key genes and pathways involved in bone growth and remodeling.

2. **Validation:**
   - Validate the models using cross-validation or a separate test dataset.

### Documentation and Presentation

1. **Report Writing:**
   - Document the findings, methods, and results in a detailed report.

2. **Presentation Preparation:**
   - Prepare a presentation summarizing the research, methods, and key findings.

## Datasets

The datasets used in this project can be downloaded from the following link:

[Download Datasets](https://drive.google.com/drive/folders/10AoprlN6X7iQtmcS0HyrQuN6Hmb-Zwzr?usp=sharing)

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/saketh-n/bone-io.git
   cd bone io
2. Download the datasets
   - Visit the [link](https://drive.google.com/drive/folders/10AoprlN6X7iQtmcS0HyrQuN6Hmb-Zwzr?usp=sharing) and download the datasets
   - Place the Datasets folder within the same directory as the scripts file
3. Install the required dependencies:
   ```bash
   pip3 install -r requirements.txt
4. Run the scripts for steps 1-4
   - STEP 1
   ```bash
   python3 load_data.py
   ```
   - STEP 2
   ```bash
   python3 preprocess_data.py
   ```
   - STEP 3
   ```bash
   python3 eda.py
   ```
   - STEP 4
   ```bash
   python3 analysis.py
   ```
