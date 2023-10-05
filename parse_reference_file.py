import pandas as pd

reference_df = pd.read_csv("pandas_reference_file.csv")

print(reference_df.head(5))

prod_fam_sku_df = reference_df.drop_duplicates(subset=["SKU's Included", "Product Name"])[["SKU's Included", "Product Name"]]

prod_fam_sku_df['Skus'] = prod_fam_sku_df["SKU's Included"].to_list()

print(prod_fam_sku_df.head())

sample_df = pd.DataFrame({'sku':["6215-5-011", "6215-5-021"], })

melted_df = pd.melt(prod_fam_sku_df, id_vars=['Product Name'], var_name='Skus', value_name='Sku')

print(melted_df.head())

