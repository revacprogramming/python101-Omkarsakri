def get_cs():
  k=input("Enter the credentials:- ")
  return k


def cs_to_dict(cs):
  d=dict()
  k=cs.split(";")
  for i in k:
    j=i.split("=")
    d[j[0]]=j[1]
  return d


def dict_to_cs(d):
  for i,j in d.items():
    print(i,"=",j,end=";")
    # print(d.keys(),d.values())


def main():
    cs=get_cs()
    d=cs_to_dict(cs) 
    print(d)
    cs = dict_to_cs(d)
    # print(cs)


if __name__ == '__main__':
    main()
