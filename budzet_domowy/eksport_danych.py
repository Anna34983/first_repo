import pandas as pd
from io import BytesIO

def export_excel(df):
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Budżet')
    buffer.seek(0)
    return buffer