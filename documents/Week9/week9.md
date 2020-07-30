


## Done
## To Do
- Do what the postdoc tole me to do 
- finish prediction stuff
- use SVR with inputs of B2M, HLA-Family and CD74 to try to predict CD8 T cells
    - try using linear kernel, if it works well or comparable to RBF kernel tehn use that and state weights assigned with it  
- Genes with DNA Repair, Stem Cell, apoptosis/cell death, inflammatory pathway, or epithelial mesenchymal transitionstem cell
- Stacked bar chart for mortality rates
- use mortality rate instead of living status
- Video!!!!!
- report correlation for bap1 -1 age vs dss time
- add lines for correaltion and text on lines for correlation coeffience and p value for the scatterplots which show correlation
- Visualize the mortality rate differences
- keep naming consistent, use immune naming for immune clustering graphs
- Start by showing immune cell fractions for immune cell clusters
- add plot for tumor radius of expression groups
- add one more column for statistical test used and if all the same state test
- Write bap1 wild type or bap1 mutated instead of 0 and -1
- look at intersections of gene expression clusters and immune clusters
- Use the barchart for immune vizualization for each expression group then order within expression group based on tumor radius and age of diagnosis


### Stuff
Did all of the stuff for the paper also have results for the predicion models



## Week 10 Doing USC Xena analysis
- Percentage of BAP1 by cluster:
    - Percentage of BAP1 -1 by cluster:  [1.0, 0.47058823529411764, 0.4375]
    - Percentage of BAP1 0 by cluster:  [0.0, 0.5294117647058824, 0.5625
- Immune differences between BAP1 groups
    - CD8 T cells  difference between groups  0   1  p-value:  0.00027535644116621975
    - Monocytes  difference between groups  0   1  p-value:  0.007911008312463533
    - Eosinophils  difference between groups  0   1  p-value:  0.030634448044689143
    - B cells  difference between groups  0   1  p-value:  0.034145127411382696
    - CD4 T cells  difference between groups  0   1  p-value:  0.00010020775928581038
    - NK cells  difference between groups  0   1  p-value:  0.016484882575862253
    - Macrophages  difference between groups  0   1  p-value:  0.00037538175596295314
    - DC  difference between groups  0   1  p-value:  0.007948980537117336

- Correlations between Immune cells and phenotypes amongst all patients:
    - IMMUNE CELL , PHENOTYPE, R, P-VALUE
    - CD8 T cells  and  BAP1_mutation :  -0.34470342171145874 0.0017411892842276529
    - Monocytes  and  BAP1_mutation :  0.2615821518796912 0.019088040024874024
    - CD4 T cells  and  BAP1_mutation :  0.4085068981494726 0.0001686850618580667
    - NK cells  and  BAP1_mutation :  0.2436896864241234 0.029385556634287286
    - Macrophages  and  BAP1_mutation :  -0.3770884043101068 0.0005649313516437987
    - DC  and  BAP1_mutation :  0.35670610568243827 0.0011629743521011256
    - T cells gamma delta  and  DSS_time :  -0.24942630060306223 0.025666766115505186
    - CD4 T cells  and  DSS_time :  0.27838923269467103 0.012403837624473567
    - NK cells  and  DSS_time :  0.2410123383804429 0.031270976316329066
    - Macrophages  and  DSS_time :  -0.24309789888245056 0.02979382876079005
    - DC  and  DSS_time :  0.281421671501485 0.011444389023417826
    - CD8 T cells  and  os_status :  0.37403419653735026 0.000631383863668405
    - B cells  and  os_status :  -0.23772568947593353 0.033723653888735564
    - Macrophages  and  os_status :  0.2958656640019888 0.007708162373662026
    - Mast cells  and  os_status :  -0.3377084410648439 0.0021872187142347893
    - B cells  and  stage :  -0.26256049684700977 0.0186279650300359
    - DC  and  stage :  -0.2529012886283474 0.023614387785239038
