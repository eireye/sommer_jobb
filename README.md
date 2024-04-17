# sommer_jobb

Tips: Lag et program som kan lage en fil også loop på alle filene i etterkant. 
Typ som kan brukes slik i terminalen:

for year in {2012..2022}; do
  file="/ssb/stamme03/fouoff_pii/Raadata/forskerpersonale/wk01/fpreg_dump${year}.xlsx"
  if [ -f "$file" ]; then
    python main.py "$file"
  else
    echo "Fil ikke funnet: $file"
  fi
done