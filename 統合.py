import pandas as pd

# filenames
excel_names = ["【統合】依頼_ワクチン高生産化_1.xlsx", "依頼_ワクチン高生産化_１-1.xlsx", "依頼_ワクチン高生産化_２.xlsx","依頼_ワクチン高生産化_3.xlsx", "依頼_ワクチン高生産化_4.xlsx", "依頼_ワクチン高生産化_4-1.xlsx"]

# read them in
excels = [pd.ExcelFile(name) for name in excel_names]

# turn them into dataframes
frames = [x.parse(x.sheet_names[0], header=None,index_col=None) for x in excels]

# delete the first row for all frames except the first
# i.e. remove the header row -- assumes it's the first
frames[1:] = [df[1:] for df in frames[1:]]

# concatenate them..
combined = pd.concat(frames)

# write it out
combined.to_excel("c.xlsx", header=False, index=False)
