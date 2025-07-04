def homework(target_online_retail_data_tb, n): 
    
    df = pd.DataFrame(target_online_retail_data_tb)
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    customer_total = df.groupby('CustomerID')['TotalPrice'].sum().reset_index()
    customer_total_sorted = customer_total.sort_values(by='TotalPrice', ascending=False).reset_index(drop=True)
    customer_total_sorted['Group'] = pd.qcut(
        customer_total_sorted['TotalPrice'], 
        q=n, 
        labels=False, 
        duplicates='drop'
    )
    group_sales = customer_total_sorted.groupby('Group')['TotalPrice'].sum().reset_index()
    total_sales = group_sales['TotalPrice'].sum()
    group_sales['SalesShare'] = group_sales['TotalPrice'] / total_sales
    group_sales_sorted = group_sales.sort_values(by='SalesShare', ascending=False).reset_index(drop=True)
    group_sales_sorted['Group'] = ['グループ' + str(i+1) for i in range(len(group_sales_sorted))]
    return pd.Series(
        group_sales_sorted['SalesShare'].values,
        index=group_sales_sorted['Group']
    ).astype(float)

