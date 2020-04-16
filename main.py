import requests,json,threading,time 

def worker(n):
    url = 'https://clarksonmsda.org/api/get_product.php?pid=' + str(n)
    r = requests.get(url) 
    if r.text != '':
      data = json.loads(r.text)
      if data['data'] is not None:
        writteddata = json.dumps(data['data'])
      else :
        writteddata = '{"prod_name": "None"}'
    else :
      writteddata = '{"prod_name": "None"}'
    fn = 'products/' + 'pid_' + str(n).rjust(4, '0') + '.json'
    with open(fn, "w") as outfile: 
      outfile.write(writteddata) 
    
n = 0
while n <= 200:
    while threading.active_count() >= 2000:
        time.sleep(.5) 
    w = threading.Thread(name='tid_'+str(n),target=worker, args=(n,)) 
    w.start()
    if n % 50 == 0:
        print('pid: ', n)

    n+=1