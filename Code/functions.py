import pandas as pd
def combine_industry_codes(dataset, codes_to_merge, new_code_label):
    mask = dataset['Industry_Code'].isin(codes_to_merge)
    subset = dataset[mask]
    results = []

    for year, group in subset.groupby('Year'):
        row = group.iloc[0, :4].copy()
        row['Industry_Code'] = new_code_label 
        summed_values = group.iloc[:, 4:].sum()
        combined = pd.concat([row, summed_values])
        results.append(combined)

    new_rows = pd.DataFrame(results)
    dataset = dataset[~mask]
    dataset = pd.concat([dataset, new_rows], ignore_index=True)
    return dataset

