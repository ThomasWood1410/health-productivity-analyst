import pandas as pd
import matplotlib.pyplot as plt
import os

def run_analysis():
    print("--- Script Started ---")
    
    # Absolute path logic
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.normpath(os.path.join(current_dir, '..', 'data', 'activity.csv'))
    
    print(f"Checking for data at: {csv_path}")

    if not os.path.exists(csv_path):
        print("❌ ERROR: activity.csv not found in the data folder!")
        return
    else:
        print("✅ File found! Loading data...")

    try:
        df = pd.read_csv(csv_path)
        print("📊 Data loaded successfully:")
        print(df.head(3)) # Show first 3 rows

        correlation = df['steps'].corr(df['study_hours'])
        print(f"\n📈 Correlation calculated: {correlation:.2f}")

        plt.scatter(df['steps'], df['study_hours'])
        plt.title(f"Correlation: {correlation:.2f}")
        
        plot_path = os.path.join(current_dir, '..', 'correlation_plot.png')
        plt.savefig(plot_path)
        print(f"🚀 Success! Plot saved to: {plot_path}")

    except Exception as e:
        print(f"❌ AN ERROR OCCURRED: {e}")

if __name__ == "__main__":
    run_analysis()