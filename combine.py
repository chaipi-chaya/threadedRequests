import csv,json

with open('products.csv', "w") as csvf: 
  for n in range(0,201):
    fn = 'products/pid_' + str(n).rjust(4, '0') + '.json'
    with open(fn, "r") as f: 
      d = f.read()
      data = json.loads(d)
      w = {}
      w['prod_id'] = n
      if data['prod_name'] != 'None':
        w['prod_sku'] = data['prod_sku']
        w['prod_cat'] = data['prod_cat']
        w['prod_name'] = data['prod_name']
      else :
        w['prod_sku'] = 'N/A'
        w['prod_cat'] = 'N/A'
        w['prod_name'] = 'N/A'
      writer = csv.DictWriter(csvf, fieldnames = ['prod_id', 'prod_sku', 'prod_cat', 'prod_name'])
      writer.writerow(w)
      f.close()
      
    if n % 50 == 0:
        print('pid', n)

