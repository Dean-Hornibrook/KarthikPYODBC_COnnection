import pypyodbc
import pandas as pd

def sample_or_not(row):
    if 'w' in str(row['SKU']) or 'W' in str(row['SKU']):
        return 'SAMPLE'
    else:
        return ''

def InitialObject():
    connection = pypyodbc.connect(
        driver='{iSeries Access ODBC Driver}',
        system='shonj1.howost.strykercorp.com',
        uid='V84QRYI',
        pwd='V84QRYI')
    c1 = connection.cursor()
    query = '''SELECT th.* , s.OPCDD AS op_code_desc, pmp.DESCP AS Product_Name FROM 
                (select DISTINCT c.PLNID,a.WRKNO,a.RELNO,a.TRPRD,a.TRSEQ,a.USRID,a.QTYGD,a.TRNDT,a.TRTIM,a.QTYSR,a.SCRRC,a.OPRCD,a.WCNT1,a.WCNT2,a.WCNT3,a.WRKDT,b.OPSDS,b.RLADT,d.LOTID,c.PALPH 
            from V84RMSIRE.SFWTP100 a, V84RMSIRE.MFWOP200 b, V84RMSIRE.MSPMP100 c, V84RMSIRE.MFWOL100 d 
            where a.wrkno = b.wrkno 
            and a.relno = b.relno 
            and a.trseq = b.woseq 
            AND a.trprd = c.prdno 
            AND a.wrkno = d.wrkno 
            AND a.relno = d.relno
            AND c.PLNID IN ( 'IRE100', 'IRE110', 'IRE130',   'IRE160', 'IRE200', 'IRE210',  'IRE220', 'IRE260', 'IRE300', 'IRE400', 'IRE500', 'IRE510', 'IRE600', 'IRE650', 'IRE180', 'IRE170' ) 
            AND YEAR(a.TRNDT) = year(CURRENT DATE) 
            AND MONTH(a.TRNDT) = MONTH(CURRENT DATE)
            
   ) th    
   LEFT OUTER JOIN V84RMSIRE.SFOPP100 s ON s.OPCDE = th.OPRCD
   LEFT OUTER JOIN V84RMSIRE.MSPMP100 pmp ON pmp.PALPH = th.PALPH'''
   
    cols = ['IRE Number','Work Number', 'Release Number', 'SKU', 'OP Sequence', 'User ID', 'Good Quantity', 'Date', 'Time', 'Financial Code', 'Op Code Description', 'Lot ID', 'SKU Group', 'OPCODE_FULL_DESCP', 'FULL_PRODUCT_NAME']
    data= pd.read_sql(query,connection)
    filtered_cols_df = data.iloc[:,[0,1,2,3,4,5,6,7,8,11,16,18,19,20,21]]
    filtered_cols_df.columns = cols
    # filtered_cols_df = pd.read_csv('as400_data.csv')
    # filtered_cols_df.to_csv('as400_data.csv')
    # print(filtered_cols_df.head(5))

    filtered_cols_df['SKU'] = filtered_cols_df['SKU'].str.strip()
    filtered_cols_df['SKU Group'] = filtered_cols_df['SKU Group'].str.strip()
    
    prod_family_df = pd.read_csv('SKU_PRODUCT_FAMILY_REF.csv') 

    filtered_cols_df['Sample_or_not'] = filtered_cols_df.apply(sample_or_not, axis=1)



    prod_family_df['PRODUCT_FAMILY']= prod_family_df['PRODUCT_FAMILY'].str.strip()
    prod_family_df['SKU']= prod_family_df['SKU'].str.strip()

    # cols = ['foo', 'bar', 'new']
    # df['combined'] = df[cols].apply(lambda row: '_'.join(row.values.astype(str)), axis=1)

    merged_df = pd.merge(filtered_cols_df,prod_family_df, left_on = 'SKU Group', right_on = 'SKU', how='left' )

    cols_for_combining = ['Sample_or_not', 'PRODUCT_FAMILY']
    merged_df['PRODUCT_FAMILY'] = merged_df[cols_for_combining].apply(lambda row: ''.join(row.values.astype(str)), axis=1)
    merged_df['SKU'] = merged_df['SKU_x']
    merged_df.drop(['SKU_x', 'SKU_y'], axis=1, inplace=True)

    merged_df.to_csv('chck_file_v2.csv') 

    print(merged_df.head(5))
    
    
    
    
    
    
    
    
    
    
    
    #~~~~~~~~~~~~~~~~~~~~~ DONT DELETE THE BELOW CODE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    
    # reference_df = pd.read_csv("pandas_reference_file.csv")

    # prod_fam_sku_df = reference_df.drop_duplicates(subset=["SKU's Included", "Product Name"])[["SKU's Included", "Product Name"]]

    # # print(prod_fam_sku_df.head())

    # # Create an empty list to store matching Product_family values
    # product_family = []

    # #Remove White spaces 
    # filtered_cols_df['SKU'] = filtered_cols_df['SKU'].str.strip()

    # # filtered_cols_df.to_csv("as400_dumps.csv")
    # # Iterate through df1's 'sku' values
    
    # # filtered_cols_df = pd.read_csv("as400_dumps.csv")
    # for sku in filtered_cols_df['SKU']:
    #     found = False  # Flag to track if a match is found
        
    #     # Iterate through df2's 'skulist' values
    #     for skulist, family in zip(prod_fam_sku_df["SKU's Included"], prod_fam_sku_df['Product Name']):
    #         sku_set = set(sku.split(','))
    #         skulist_set = set(skulist.strip('{}').replace('\n', '').split(','))
    #         # print(skulist_set)
            
    #         # Check if the SKU is a subset of the skulist
    #         if sku_set.issubset(skulist_set):
    #             product_family.append(family)
    #             found = True
    #             break  # Exit the inner loop once a match is found
        
    #     # If no match was found, append None
    #     if not found:
    #         product_family.append(None)

    # # Add the 'Product_family' column to df1
    # filtered_cols_df.loc[:,'Product_family'] = product_family

    # # print(filtered_cols_df.head(150))

    # filtered_cols_df.to_csv("chck_file.csv")

    # return filtered_cols_df.to_json(orient='records')

InitialObject()