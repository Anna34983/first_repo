import pandas as pd
from io import BytesIO

def export_excel(df):
    bufor = BytesIO()
    with pd.ExcelWriter(bufor, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Budżet')
    bufor.seek(0)
    return bufor