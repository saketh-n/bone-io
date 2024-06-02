import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF

def descriptive_statistics(data_frames):
    stats = {}
    for name, df in data_frames.items():
        numeric_df = df.select_dtypes(include=[float, int])
        if not numeric_df.empty:
            stats[name] = numeric_df.describe()
    return stats

def visualize_data(data_frames, pdf):
    for name, df in data_frames.items():
        numeric_df = df.select_dtypes(include=[float, int])
        
        if numeric_df.empty:
            print(f"Skipping visualization for {name} as it has no numeric columns.")
            continue

        # Histograms
        fig, axes = plt.subplots(nrows=1, ncols=len(numeric_df.columns), figsize=(20, 5))
        numeric_df.hist(ax=axes)
        plt.suptitle(f'Histograms for {name}')
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        fig.savefig(f"{name}_histograms.png")
        pdf.add_page()
        pdf.image(f"{name}_histograms.png", x=10, y=10, w=pdf.w - 20)
        
        # Box plots
        fig, ax = plt.subplots(figsize=(10, 8))
        numeric_df.plot(kind='box', ax=ax)
        plt.title(f'Box plots for {name}')
        fig.savefig(f"{name}_boxplots.png")
        pdf.add_page()
        pdf.image(f"{name}_boxplots.png", x=10, y=10, w=pdf.w - 20)
        
        # Pair plots (scatter plot matrix) for smaller datasets
        if numeric_df.shape[1] <= 10:  # Adjust this threshold based on your dataset
            sns.pairplot(numeric_df)
            plt.suptitle(f'Pair plots for {name}')
            plt.tight_layout(rect=[0, 0.03, 1, 0.95])
            plt.savefig(f"{name}_pairplots.png")
            pdf.add_page()
            pdf.image(f"{name}_pairplots.png", x=10, y=10, w=pdf.w - 20)

def save_statistics_to_text(stats, filename="descriptive_statistics.txt"):
    with open(filename, "w") as file:
        for name, stat in stats.items():
            file.write(f"Descriptive statistics for {name}:\n")
            if isinstance(stat, pd.DataFrame):
                file.write(stat.to_string())
            else:
                file.write(stat)
            file.write("\n\n")

if __name__ == "__main__":
    from load_data import load_all
    from preprocess_data import clean_data

    data_frames = load_all()

    data_frames = clean_data(data_frames)

    # Perform descriptive statistics
    stats = descriptive_statistics(data_frames)

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    save_statistics_to_text(stats)

    visualize_data(data_frames, pdf)

    pdf.output("EDA_Report.pdf")
