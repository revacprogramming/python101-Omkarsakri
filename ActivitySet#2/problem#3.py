l=[]
t=tuple()
def get_cs():
  
  s='system=s;database=d;username=u;password=p'
  return s

def cs_to_lot(cs):
  y=cs.split(';')
  return y
def main():
  cs = get_cs()
  
  lot = cs_to_lot(cs)
  

  length = len(lot)
  for i in range(length):
    x = lot[i].split('=')
    t=tuple(x)
    l.append(t)
  return l
  
if _name_ == '_main_':
    main()
print(l)
