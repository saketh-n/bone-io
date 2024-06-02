import pandas as pd
from scipy.stats import ttest_ind, f_oneway
from load_data import load_all
import time
import multiprocessing as mp

# Load all data frames
data_frames = load_all()

# List of relevant columns identified
target_variables = [
    'SampleID', 'Accession', 'ID', 'IDENTIFIER', 'ID_REF',
    'Gene ID', 'ENTREZ_GENE_ID', 'Entrez_Gene_ID', 'Gene Symbol', 'Gene Title',
    'Gene symbol', 'Gene title', 'ILMN_Gene', 'RefSeq Transcript ID', 'RefSeq_ID',
    'Representative Public ID', 'GB_ACC', 'GB_LIST', 'GenBank Accession', 'Protein_Product',
    'RANGE_GB', 'RANGE_START', 'RANGE_STOP', 'RANGE_STRAND', 'SPOT_ID', 'Platform_CLONEID',
    'Platform_ORF', 'Platform_SEQUENCE', 'Platform_SPOTID', 'total_probes',
    'Gene Ontology Biological Process', 'Gene Ontology Cellular Component',
    'Gene Ontology Molecular Function', 'Ontology_Component', 'Ontology_Function',
    'Ontology_Process', 'GO:Component', 'GO:Component ID', 'GO:Function', 'GO:Function ID',
    'GO:Process', 'GO:Process ID', 'Annotation Date', 'Chromosome', 'Chromosome annotation',
    'Chromosome location', 'Cytoband', 'Definition', 'Obsolete_Probe_Id', 'Probe_Chr_Orientation',
    'Probe_Coordinates', 'Probe_Start', 'Probe_Type', 'Nucleotide Title', 'Source', 'Species',
    'Species Scientific Name', 'Target Description', 'Synonyms', 'Search_Key',
    'Source_Reference_ID', 'category', 'gene_assignment', 'mrna_assignment', 'nuID', 'seqname'
]

def correlation_analysis(data_frames):
    correlations = {}
    for name, df in data_frames.items():
        numeric_df = df.select_dtypes(include=[float, int])
        if not numeric_df.empty:
            print(f"Calculating correlations for {name} with shape {numeric_df.shape}")
            correlations[name] = numeric_df.corr()
    return correlations

def statistical_testing(args):
    data_frames, target_variable = args
    results = {}
    for name, df in data_frames.items():
        if target_variable in df.columns:
            print(f"Performing statistical testing for {name} and target variable {target_variable}")
            groups = df[target_variable].unique()
            group_data = [df[df[target_variable] == group].select_dtypes(include=[float, int]) for group in groups]
            
            # Check for empty or insufficient data
            if len(group_data) < 2 or any(len(group) < 2 for group in group_data):
                print(f"Skipping {name} for {target_variable} due to insufficient data")
                continue

            if len(groups) == 2:
                # Perform t-test for two groups
                stat, p_value = ttest_ind(group_data[0], group_data[1], nan_policy='omit')
                results[name] = {'t-test': {'statistic': stat, 'p_value': p_value}}
            elif len(groups) > 2:
                # Perform ANOVA for more than two groups
                stat, p_value = f_oneway(*group_data)
                results[name] = {'ANOVA': {'statistic': stat, 'p_value': p_value}}
    return (target_variable, results)

def save_correlation_and_testing_results(correlations, testing_results, filename="correlation_and_testing_results.txt"):
    with open(filename, 'w') as file:
        file.write("Correlation Analysis:\n")
        for name, corr in correlations.items():
            file.write(f"\n{name}:\n")
            file.write(corr.to_string())
            file.write("\n")
        
        file.write("\n\nStatistical Testing:\n")
        for target_variable, result in testing_results.items():
            file.write(f"\nResults for {target_variable}:\n")
            for name, res in result.items():
                file.write(f"\n{name}:\n")
                file.write(str(res))
                file.write("\n")

start_time = time.time()

# Perform correlation analysis
correlations = correlation_analysis(data_frames)

# Prepare arguments for multiprocessing
args = [(data_frames, target_variable) for target_variable in target_variables]

# Total number of tasks for progress calculation
total_tasks = len(args)
completed_tasks = 0

# Perform statistical testing in parallel
pool = mp.Pool(mp.cpu_count())
results = []

for result in pool.imap_unordered(statistical_testing, args):
    results.append(result)
    completed_tasks += 1
    progress = (completed_tasks / total_tasks) * 100
    print(f'Progress: {progress:.2f}%')

pool.close()
pool.join()

# Collect all testing results
all_testing_results = dict(results)

# Save correlation and statistical testing results to a file
save_correlation_and_testing_results(correlations, all_testing_results)

end_time = time.time()
print(f"Script completed in {end_time - start_time} seconds")
