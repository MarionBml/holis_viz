import streamlit as st
import pandas as pd

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
def load_proc_imp():  
    process_details = load_process_data()  
    proc_imp = pd.read_csv('data/BI_2.02__03_Procedes_Impacts.csv', sep = ';', encoding='latin-1', header = 0)
    
    columns_sorted = proc_imp.iloc[:,4:].sort_index(axis=1)
    columns_sorted.columns = process_details['Flux Name']
    
    proc_imp = proc_imp.iloc[:,:4].join(columns_sorted)
    proc_imp.drop(proc_imp.index[0], inplace = True)

    proc_imp = proc_imp.T
    proc_imp.columns = proc_imp.iloc[0]
    proc_imp = proc_imp.iloc[1:]
    return proc_imp

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