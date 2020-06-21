import pandas as pd


def convert_to_gene_name(raw, ens_hug, ens_hug2):
    to_be_dropped = []

    for i, gene in enumerate(raw):
        # first search in the ens_hug2 then if not found in ens_hug
        is_found = ens_hug2.loc[ens_hug2['ensemble_geneid'] == gene]
        if len(is_found) > 0 and is_found.index[0] != "#N/A":
            raw[i] = is_found.index[0]

        else:
            t = ens_hug.loc[ens_hug['Ensembl ID(supplied by Ensembl)'] == gene]
            # first search in 'Ensembl ID(supplied by Ensembl)' column, if not found, search the other col

            if len(t) > 0:
                if type(t.index[0]) == str:
                    raw[i] = t.index[0]

            else:
                t2 = ens_hug.loc[ens_hug['Ensembl gene ID'] == gene]
                if len(t2) > 0:
                    if type(t2.index[0]) == str:
                        raw[i] = t2.index[0]
                    else:
                        print(gene)
                        to_be_dropped.append(gene)
                else:
                    print(gene)
                    to_be_dropped.append(gene)
    return raw, to_be_dropped


def convert_to_ensemble(raw, ens_hug, ens_hug2):
    to_be_dropped = []

    for i, gene in enumerate(raw):
        # first search in the ens_hug2 then if not found in ens_hug
        is_found = ens_hug2.loc[ens_hug2['Associate Gene Name'] == gene]

        if len(is_found) > 0:
            raw[i] = is_found.index[0]
        else:
            t = ens_hug.loc[ens_hug['Approved symbol'] == gene]
            # first search in 'approved symbol' column, if not found, search others

            if len(t) > 0:
                if type(t.index[0]) == str:
                    raw[i] = t.index[0]
                elif type(t['Ensembl gene ID'][0]) == str:
                    raw[i] = t['Ensembl gene ID'][0]

            else:
                find = ens_hug.isin([gene]).any(axis=1)
                # temp = find.loc[find == True]
                temp = ens_hug[find == True]

                if len(temp) > 0:
                    if type(temp.index[0]) == str:
                        raw[i] = temp.index[0]
                    elif type(temp['Ensembl gene ID'][0]) == str:
                        raw[i] = temp['Ensembl gene ID'][0]
                    else:
                        print(gene)
                        to_be_dropped.append(gene)
                else:
                    print(gene)
                    to_be_dropped.append(gene)

    # raw = raw.drop(to_be_dropped)
    return raw, to_be_dropped


def run_ensembl_to_gene(input_name, output_name, sep='\t'):
    raw_counts = pd.read_csv(input_name, header=0, sep=sep)
    name_first_col = list(raw_counts)[0]
    raw_counts[name_first_col] = [name[: name.find('.')] for name in list(raw_counts[name_first_col])]

    ensembl_hugo = pd.read_csv("../scripts/convert_geneID_ensembl/hugo_enseml_synonym.txt", header=0, sep="\t")
    ensembl_hugo2 = pd.read_csv("../scripts/convert_geneID_ensembl/GSE87692_Primary_HsESF_TPMs_073015.txt", header=0, sep="\t")

    ensembl_hugo2 = ensembl_hugo2[['ensemble_geneid', 'Associate Gene Name']]
    ensembl_hugo2.set_index('Associate Gene Name', inplace=True)

    ensembl_hugo.dropna(subset=['Ensembl ID(supplied by Ensembl)', 'Ensembl gene ID'], how='all', inplace=True)
    ensembl_hugo = ensembl_hugo.set_index('Approved symbol')

    gene_names, to_be_dropped = convert_to_gene_name(list(raw_counts[name_first_col]), ensembl_hugo, ensembl_hugo2)
    raw_counts[name_first_col] = gene_names
    raw_counts = raw_counts.set_index(name_first_col)
    raw_counts = raw_counts.drop(to_be_dropped)
    raw_counts.to_csv(output_name, sep='\t')


def run_gene_to_ensembl(input_name, output_name, sep='\t'):
    raw_counts = pd.read_csv(input_name, header=0, sep=sep)
    name_first_col = list(raw_counts)[0]
    raw_counts[name_first_col] = raw_counts[name_first_col].str.lower()

    ensembl_hugo = pd.read_csv("../scripts/convert_geneID_ensembl/hugo_enseml_synonym.txt", header=0, sep="\t")
    ensembl_hugo2 = pd.read_csv("../scripts/convert_geneID_ensembl/GSE87692_Primary_HsESF_TPMs_073015.txt", header=0, sep="\t")

    ensembl_hugo2 = ensembl_hugo2[['ensemble_geneid', 'Associate Gene Name']]
    ensembl_hugo2.set_index('ensemble_geneid', inplace=True)
    ensembl_hugo2['Associate Gene Name'] = ensembl_hugo2['Associate Gene Name'].str.lower()

    ensembl_hugo.dropna(subset=['Ensembl ID(supplied by Ensembl)', 'Ensembl gene ID'], how='all', inplace=True)
    ensembl_hugo = ensembl_hugo.set_index('Ensembl ID(supplied by Ensembl)')
    # new1 = ensembl_hugo['Synonyms'].str.split(", ", n=4, expand=True)
    new1 = ensembl_hugo['Previous symbols'].str.split(", ", n=4, expand=True)
    new2 = ensembl_hugo['Synonyms'].str.split(", ", n=4, expand=True)
    ensembl_hugo.drop(columns=['Previous symbols'], inplace=True)
    frames = [ensembl_hugo, new1, new2]
    ensembl_hugo = pd.concat(frames, axis=1)
    ensembl_hugo = ensembl_hugo.apply(lambda x: x.astype(str).str.lower())
    ensembl_hugo['Ensembl gene ID'] = ensembl_hugo['Ensembl gene ID'].str.upper()

    gene_names, to_be_dropped = convert_to_ensemble(list(raw_counts[name_first_col]), ensembl_hugo, ensembl_hugo2)
    raw_counts[name_first_col] = gene_names
    raw_counts = raw_counts.set_index(name_first_col)
    raw_counts = raw_counts.drop(to_be_dropped)
    raw_counts.to_csv(output_name, sep='\t')


if __name__ == "__main__":
    convert_to_gene_ID = False
    convert_to_ensemble_ID = False

    if convert_to_gene_ID:
        run_ensembl_to_gene(input_name="GSE75990_ensembl.txt", output_name="GSE75990_gene.txt")

    if convert_to_ensemble_ID:
        run_gene_to_ensembl(input_name="GSE75990_TPM_GEO.txt", output_name="GSE75990_ensembl.txt", sep='\t')
