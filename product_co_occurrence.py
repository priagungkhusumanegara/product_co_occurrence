import networkx as nx
import pandas as pd
from networkx.algorithms import bipartite

# df = pd.read_excel("FKT Data/fkt_cooccurrence.xlsx")
# G = nx.from_pandas_dataframe(df, 'Booking_Service_Id', 'Name_Product')
# W = bipartite.weighted_projected_graph(G, df['Name_Product'].unique())
# X = nx.to_pandas_dataframe(W)

df = pd.read_excel("co-occurrence.xlsx")
df = df[~df.CATEGORY_PRODUCT.isnull()]
G = nx.from_pandas_dataframe(df, 'BOOKING_ID', 'CATEGORY_PRODUCT')
W = bipartite.weighted_projected_graph(G, df['CATEGORY_PRODUCT'].unique())
X = nx.to_pandas_dataframe(W)
X.to_excel("product_pairing.xlsx")
