## TripodsREU
This is the repo I will be using for all of my Tripods REU studies.

## Week 1 5/26/20
In the first week I will be using GDC data and filling in missing values using the website Genecard. This is necessary because the CibersortX algorithm these IDs to reference genes. It will then produce an output which represents the percentage of immune cell types in the samples. This output will then be used in a package which creates a vizualization of all of the data.

Created Hugoify which fetches the Hugo symbol given the Enterex Gene ID. This will make it so that TumorDecon doesnt just have to discard all of the values which have nan entries. If a symbol cannot be found it will resort to nan and it will be discarded anyways.
