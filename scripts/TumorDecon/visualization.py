# visualization.py - Sumeyye Su

import os
import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt

# combine the cells that belong to same family:
def combine_celltypes(df):
    # Check if freqs already sum to 1, and scale them first if not:
    h=np.ones(df.shape[0])
    k=df.sum(axis=1).values
    if not np.array_equal(h,k):
        df=sum_upto_1(df)

    B=['B cells naive', 'B cells memory']
    T_CD4=['T cells CD4 naive', 'T cells CD4 memory resting', 'T cells CD4 memory activated','T cells follicular helper', 'T cells regulatory (Tregs)']
    NK=['NK cells resting', 'NK cells activated']
    Macro= ['Macrophages M0', 'Macrophages M1', 'Macrophages M2']
    Mast=['Mast cells resting','Mast cells activated']
    DC=['Dendritic cells resting', 'Dendritic cells activated']

    df['B cells'] = df[B].sum(axis=1)
    df['T cells CD4'] = df[T_CD4].sum(axis=1)
    df['NK cells'] = df[NK].sum(axis=1)
    df['Macrophages'] = df[Macro].sum(axis=1)
    df['Mast cells']=df[Mast].sum(axis=1)
    df['DC'] = df[DC].sum(axis=1)
    df=df.drop(['Dendritic cells resting', 'Dendritic cells activated','Macrophages M0', 'Macrophages M1', 'Macrophages M2', 'T cells follicular helper','T cells regulatory (Tregs)','NK cells resting', 'NK cells activated','T cells CD4 naive', 'T cells CD4 memory resting', 'T cells CD4 memory activated', 'Mast cells resting', 'Mast cells activated','B cells naive', 'B cells memory'],axis=1)
    df=df.rename({'T cells CD8':'CD8 T cells','T cells CD4':'CD4 T cells'},axis='columns')
    return df

# scale the frequences so they sum up to 1
def sum_upto_1(df):
    df[df<0]=0
    s=df.sum(axis=1)
    df=df.divide(s,axis=0)*1
    return df


def cell_frequency_boxplot(sample_cell_freq, xsize=12, ysize=7):
    """
     Input:
        - 'sample_cell_freq': A dataframe that include cell frequency of samples
            Rows are samples id, columns are cell names
    Output:
        - cells frequency box plot in descending order
    """
    new_cell_freq = combine_celltypes(sample_cell_freq)
    b=new_cell_freq.median(axis = 0)
    b=list(zip(b.index,b))
    b = sorted(b, key=lambda x: x[-1],reverse=True)
    sorted_cells=[x[0] for x in b]
    new_cell_freq=new_cell_freq[sorted_cells]
    sns.set(rc={'figure.figsize':(xsize,ysize)})
    sns.set(style="white")
    palette={'Macrophages':'violet','CD8 T cells':'orange','CD4 T cells':'goldenrod','Monocytes':'lightsalmon','NK cells':'olivedrab','Mast cells':'red','B cells':'darkcyan','T cells gamma delta':'dodgerblue','DC':'gray','Plasma cells':'seagreen','Neutrophils':'navy', 'Eosinophils':'purple'}
    sns.boxplot(order=sorted_cells, data=new_cell_freq,palette=palette)
    sns.swarmplot(order=sorted_cells, data=new_cell_freq,color=".25")
    plt.xlabel('')
    plt.xticks(rotation=90)
    plt.ylabel('Frequencey')
    plt.subplots_adjust(top=0.95,bottom=0.2)
    plt.show()
    return plt


def cell_frequency_barchart(sample_cell_freq, xsize=15, ysize=7):
    """
     Input:
        - 'sample_cell_freq': A dataframe that include cell frequency of samples
            Rows are samples id, columns are cell names
    Output:
        - a barchart plot that shows all cell frequency of all samples
    """
    new_cell_freq=combine_celltypes(sample_cell_freq)
    b=new_cell_freq.median(axis = 0)
    b=list(zip(b.index,b))
    b = sorted(b, key=lambda x: x[-1],reverse=True)
    sorted_cells=[x[0] for x in b]
    new_cell_freq=new_cell_freq[sorted_cells]
    palette={'Macrophages':'violet','CD8 T cells':'orange','CD4 T cells':'goldenrod','Monocytes':'lightsalmon','NK cells':'olivedrab','Mast cells':'red','B cells':'darkcyan','T cells gamma delta':'dodgerblue','DC':'gray','Plasma cells':'seagreen','Neutrophils':'navy', 'Eosinophils':'purple'}
    sns.set(rc={'figure.figsize':(xsize,ysize)})
    sns.set_style("white")

    color=[]
    for gene in sorted_cells:
        a=palette[gene]
        color=color+[a]

    ax=new_cell_freq.plot.barh(stacked=True,color=color,width=1)
    ax.legend(loc='right', bbox_to_anchor=(1.25,0.5),
          fancybox=True, shadow=False, ncol=1)

    plt.yticks([])
    plt.margins(0, 0)
    plt.xlabel('Frequency')
    plt.ylabel('Patients')
    plt.subplots_adjust(top=0.95,left=0.05, right=0.8) # don't cut off legend
    plt.show()
    return


def hierarchical_clustering(sample_cell_freq, xsize=20, ysize=5):
    """
     Input:
        - 'sample_cell_freq': A dataframe that include cell frequency of samples
            Rows are samples id, columns are cell names
    Output:
        - hierarchical clustered heatmap from cell frequency of samples
    """
    # Change figure size:
    plt.rcParams["figure.figsize"] = (xsize,ysize)

    new_cell_freq=combine_celltypes(sample_cell_freq)

    b=new_cell_freq.median(axis = 0)
    b=list(zip(b.index,b))
    b = sorted(b, key=lambda x: x[-1],reverse=True)
    sorted_cells=[x[0] for x in b]
    new_cell_freq=new_cell_freq[sorted_cells]
    sns.clustermap(new_cell_freq,cmap='coolwarm',row_cluster=False)
    plt.subplots_adjust(bottom=0.2)
    plt.show()
    return

def pair_plot(sample_cell_freq, xsize=5, ysize=5):
    """
     Input:
        - 'sample_cell_freq': A dataframe that include cell frequency of samples
           Rows are samples id, columns are cell names
    Output:
        - pairplot from cell frequency of samples
    """
    # Change figure size:
    plt.rcParams["figure.figsize"] = (xsize,ysize)
    new_cell_freq=combine_celltypes(sample_cell_freq)
    b=new_cell_freq.median(axis = 0)
    b=list(zip(b.index,b))
    b = sorted(b, key=lambda x: x[-1],reverse=True)
    sorted_cells=[x[0] for x in b]
    new_cell_freq=new_cell_freq[sorted_cells]

    p = sns.pairplot(new_cell_freq)
    p.fig.set_size_inches(xsize,ysize)
    plt.subplots_adjust(bottom=0.1, top=1.0, left=0.05, right=0.95)
    plt.show()
    return
