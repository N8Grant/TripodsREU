import pandas as pd
import urllib
import xml.etree.ElementTree as ET


def read_file(file_name, sep='\t'):
    file = pd.read_csv(file_name, header=0, sep=sep)
    name_first_col = list(file)[0]
    file.set_index(name_first_col, inplace=True)
    return file, name_first_col


def get_results_from_db2db(genes, input_type, output_type):
    url = 'https://biodbnet-abcc.ncifcrf.gov/webServices/rest.php/biodbnetRestApi.xml?method=db2db&format=row&' \
          'input=' + input_type + '&inputValues=' + genes + '&outputs=' + output_type + '&taxonId=9606'
    u = urllib.request.urlopen(url)
    response = u.read()
    tree = ET.ElementTree(ET.fromstring(response))
    root = tree.getroot()

    output_str = []
    for new_gene_name in root.iter(output_type):
        output_str.append(new_gene_name.text[:15])
    return output_str


if __name__ == "__main__":
    convert_to_ensembl = True

    if convert_to_ensembl:
        # here specify the input file
        gene_symbol, first_col = read_file("GSE75990_TPM_GEO.txt")
        print(len(gene_symbol))
        ensembl_name = []
        for i in range(len(gene_symbol)//700 + 1):
            gene_names = ','.join(list(gene_symbol.index)[i*700:min((i+1)*700, len(gene_symbol))])
            new_name = get_results_from_db2db(gene_names, 'genesymbolandsynonyms', 'EnsemblGeneID')
            ensembl_name += new_name
            print(len(ensembl_name))
        gene_symbol.index = ensembl_name
        gene_symbol = gene_symbol.rename_axis(first_col, axis=0)
        gene_symbol = gene_symbol[gene_symbol.index != '-']
        print(len(gene_symbol))
        # specify output file name
        gene_symbol.to_csv("GSE75990_TPM_GEO_enseml.txt", sep='\t')