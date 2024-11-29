import streamlit as st
import pandas as pd
import numpy as np

@st.cache_data
def load_process_data():    
    process_details = pd.read_excel('data/BI_2.02__02_Procedes_Details.xlsx', index_col=1)
    process_details = process_details.T
    process_details.columns = process_details.columns.str.strip()
    process_details.set_index('UUID', inplace = True)
    process_details = process_details.drop(process_details.columns[[5, 7, 8, 9, 10]],axis = 1)
    process_details.drop(process_details.index[0], inplace = True)
    process_details.rename(columns={process_details.columns[1]: "Flux Name" }, inplace = True)
    process_details.drop(process_details.columns[process_details.nunique() == 1], axis=1, inplace=True)
    process_details = process_details.drop(['Biomass ratio', 'Thermal solar ratio', 'Geothermal ratio', 'Tide ratio', 
                                        'Other ratio comment', 'Transmission losses consider', 'Losses ratio',  'Mix comment'], axis=1)
    #On renomme les colonnes Method et Methods qui sont chacune des duplicates (4 colonnes)
    process_details.columns = ['Flux Name', 'Version', 'Quantitative product or process properties',
       'Synonyms', 'Categorization (level 1)', 'Categorization (level 2)',
       'Categorization (level 3)', 'Categorization (level 4)',
       'General comment on data set', 'reference_flow', 'ReferenceQuantity',
       'Unit', 'Reference year', 'Dataset valid until',
       'Time representativeness description', 'Geographical area',
       'Technology description including background system',
       'Technical purpose of product or process',
       'Flow diagramm(s) or picture(s)', 'Type of data set',
       'LCI method principle', 'Deviations from LCI method principle',
       'LCI method approaches', 'Deviations from LCI method approaches',
       'Data cut off and completeness principles',
       'Data selection and combination principles',
       'Deviations from selection and combination principles',
       'Data treatment and extrapolations principles',
       'Deviations from treatment and extrapolation principles',
       'Data source(s) used for this data set', 'Sampling procedure',
       'Data collection period', 'Use advice for data set',
       'Completeness product model', 'Scope', 'Validation_Methods',
       'Data quality indicator', 'Review details',
       'Reviewer name and institution', 'Subsequent review comments',
       'Complete review report', 'Commissioners', 'Project',
       'Data set generator / modeller', 'Data entry by',
       'Date of last revision', 'Registration authority',
       'Registration number', 'Owner of data set', 'Copyright ?',
       'Access and use restrictions', 'Confidentiality',
       'Limit confidentiality date', 'Method', 'Method parametes', 'Source_Method',
       'Not considered exclusions', 'Consummers transport inclusion',
       'Infrastructures consider', 'URI', 'Cut off criteria rule',
       'Amount of electricity required for the process',
       'productAllocationValue', 'productAllocationType',
       'productAllocationComment', 'Electrical mix (Geographical area: )',
       'Methods', 'Nuclear ratio', 'Coal ratio', 'Natural gas ratio',
       'Oil ratio', 'Hydroelectric ratio', 'Wind ratio', 'Waste ratio',
       'Solar PV ratio', 'Other ratio', 'PCI value']
    return process_details

@st.cache_data
def load_expl(): 
    cat_impacts =  pd.read_excel('data/BI_2.02__06_CatImpacts_Details.xlsx', index_col=1)
    cat_impacts = cat_impacts.T
    cat_impacts.columns = cat_impacts.columns.str.strip()
    cat_impacts.set_index('UUID', inplace = True)
    cat_impacts.rename(columns={cat_impacts.columns[1]: "French Name" }, inplace = True)
    cat_impacts.drop(cat_impacts.index[0], inplace = True)
    cat_impacts.drop(cat_impacts.columns[cat_impacts.nunique() == 1], axis=1, inplace=True)
    cat_impacts['Dataset format'] = 'ILCD format'
    return cat_impacts


@st.cache_data
def load_proc_imp():  
    process_details = load_process_data()  
    proc_imp = pd.read_csv('data/BI_2.02__03_Procedes_Impacts.csv', sep = ';', encoding='latin-1', header = 0)
    
    columns_sorted = proc_imp.iloc[:,4:].sort_index(axis=1)
    columns_sorted.columns = process_details['Flux Name']
    
    proc_imp = proc_imp.iloc[:,:4].join(columns_sorted)
    proc_imp.drop(proc_imp.index[0], inplace = True)

    proc_imp = proc_imp.T
    proc_imp.columns = proc_imp.iloc[0]
    #On remplace l'outlier des radiations ionisantes de l'islande en prenant la 2e plus grande valeur 
    #proc_imp.loc['Electricity grid mix, IS','b5c632be-def3-11e6-bf01-fe55135034f3'] = 120740
    proc_imp = proc_imp.iloc[1:]
    proc_imp.index = proc_imp.index.str.strip()
    return proc_imp

# Créer vecteur des transformations en npt : facteurs d'aggrégation après normalisation et pondération
# https://energieplus-lesite.be/theories/enveloppe9/totem/totem-performance-environnementale-score-agrege-ou-detaille/
dic = {'b5c611c6-def3-11e6-bf01-fe55135034f3' : 1100000,
        'b5c629d6-def3-11e6-bf01-fe55135034f3' : 1176000000,
        'b2ad6d9a-c78d-11e6-9d9d-cec0c932ce01' : 26000,
        '0db6bc32-3f72-48b9-bdb3-617849c2752f' : 26000,
        '2105d3ac-c7c7-4c80-b202-7328c14c66e8' : 26000,
        'b53ec18f-7377-4ad3-86eb-cc3f4f276b2b' : 17000000,
        'b5c619fa-def3-11e6-bf01-fe55135034f3' : 1500000, 
        'b5c614d2-def3-11e6-bf01-fe55135034f3' : 210000,
        'b5c610fe-def3-11e6-bf01-fe55135034f3' : 1200000,
        'b5c602c6-def3-11e6-bf01-fe55135034f3' : 12000,
        'b5c632be-def3-11e6-bf01-fe55135034f3' : 450,
        'b2ad6110-c78d-11e6-9d9d-cec0c932ce01' : 1300,
        'b2ad6494-c78d-11e6-9d9d-cec0c932ce01' : 1186000000,
        'b2ad6890-c78d-11e6-9d9d-cec0c932ce01' : 97
        }

@st.cache_data

def load_proc_imp_npt():
    process_details = load_process_data()  

# On calcule la version normalisée et pondérée en npt de proc_imp
    proc_imp_npt = load_proc_imp().iloc[3:].astype('float32')
    for column in proc_imp_npt.columns: 
        proc_imp_npt[column] = proc_imp_npt[column] * dic[column] 

# On ajoute une colonne avec le score total par process en mpt 
    return proc_imp_npt