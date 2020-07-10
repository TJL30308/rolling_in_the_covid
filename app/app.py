import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'
df = pd.read_csv(url, parse_dates=True)

states = df['state'].unique()

for state in states:
    
    state_name = state
    print(f'Generating plot for {state_name}')
    
    df_state = df[df['state']==state]
    dates = df_state['date']
    new_dates = dates[1:]
    cases = df_state['cases']
    new_cases = np.diff(cases)
    new_df = pd.DataFrame({'date': new_dates, 
                  'new_cases': new_cases})
    
    date_seventh = df_state['date'][::14]
    rolling_cases = new_df['new_cases'].rolling(7).mean()
    
    fig, ax = plt.subplots(figsize=(10, 8))

    right_side = ax.spines['right']
    right_side.set_visible(False)
    left_side = ax.spines['left']
    left_side.set_visible(False)
    top_side = ax.spines['top']
    top_side.set_visible(False)
    bottom_side = ax.spines['bottom']
    bottom_side.set_visible(False)

    plt.plot(new_df['date'], rolling_cases, color='red')
    # plt.xticks(ticks=date_seventh[1:13], rotation=45)
    plt.xticks([])
    plt.yticks([])
    plt.title(f'{state}', fontsize=18)
    # plt.ylabel('Cases')

    plt.savefig(f'plots/{state_name}_plot.png', dpi=None, facecolor='w', edgecolor='w', orientation='portrait')

    plt.close()