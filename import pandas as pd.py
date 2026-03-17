import pandas as pd

# 1. Încărcăm datele murdare pe care le-ai creat deja
df = pd.read_excel('Date_Murdare_Mari.xlsx')

# 2. Curățăm textul: scoatem spațiile și punem prima literă mare
df['Nume_Sector'] = df['Nume_Sector'].str.strip().str.title()

# 3. Curățăm numerele: scoatem spațiile din coloana de Chirii
df['Chirie_Euro'] = pd.to_numeric(df['Chirie_Euro'].astype(str).str.strip(), errors='coerce')

# 4. Salvăm fișierul de portofoliu
df.to_excel('Portofoliu_Final_Curat.xlsx', index=False)

print("✨ MAGIE! Datele sunt acum curate și gata pentru raportare.")