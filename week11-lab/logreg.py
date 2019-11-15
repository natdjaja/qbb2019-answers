#!/usr/bin/env python3

import scanpy.api as sc
import seaborn as sns
import umap as umap

# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()

sc.pp.filter_genes(adata, min_counts = 1) #only consider genes with more than 1 count
sc.pp.normalize_per_cell(adata, key_n_counts = 'n_counts_all') #normalize with total UMI count per cell

filter_result = sc.pp.filter_genes_dispersion(adata.X, flavor = 'cell_ranger', n_top_genes=1000, log = False)

adata = adata[:, filter_result.gene_subset] #filter genes
sc.pp.normalize_per_cell(adata)  # need to redo normalization after filtering
sc.pp.log1p(adata)
sc.pp.scale(adata)

sc.pp.neighbors(adata)
sc.tl.louvain(adata,  resolution = 0.3)    
sc.tl.umap(adata)
sc.pl.umap(adata,color = ["louvain", "Malat1", "Ccna2", "mt-Atp6", "Lhx6", "mt-Cytb", "Zbtb20", "Npas1", "Ftl1", "Trem2", "Reln", "Col3a1"], legend_loc='on data')

sc.tl.rank_genes_groups(adata, 'louvain', method = 'logreg')
sc.pl.rank_genes_groups(adata)