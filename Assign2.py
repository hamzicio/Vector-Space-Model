#author k163710

# coding=utf8
import math
import os
from nltk.tokenize import word_tokenize
import re
import json
from collections import defaultdict



shaikha=[] #for comparing in normalization
qdictionary ={} #runtime query dictionary for parsing
querydictionary =defaultdict(lambda: defaultdict(list))
qidfDict=defaultdict(lambda: defaultdict(list)) #idftf for query on runtime
idfdictionary ={} #idf for every word
file = open(r"C:\Users\SHAIKH\.spyder-py3\Assign2\list.txt", "r")
stop_words = []
for w in file:
    stop_words.extend(word_tokenize(w))   
    
    

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

#computing idf 
def computeIDF(doc,dictforidfcalc):
    import math
    idfDict=defaultdict(lambda: defaultdict(list))
    for word in sorted(dictforidfcalc.items()):
        idf=math.log10(50 / float(word[1]))
        idfdictionary[word[0]]=idf
  
  #computing idf*tf      
    for wordi,val in sorted(doc.items()):
         for key in val.items():
            n=key[1]
            for i in n:
                lico=i
            idfDict[key[0]][wordi].append(idfdictionary.get(wordi) * int(lico))
    
    
        
#exporting idf , idf *tf for future use
    json.dump(idfdictionary, open(r"C:\Users\SHAIKH\.spyder-py3\Assign2\IDFDictionary.json", 'w'))     
  
        
    return idfDict    



    
                

          


def Union(lst1, lst2): 
    final_list = list(set(lst1) | set(lst2)) 
    return final_list  


#normalization of vectors
def l2_norm(list1):
    sum1=0
    for i in list1:
         sum1=sum1 + math.pow((i),(2))
         sidar=math.sqrt(sum1)
         
    sum1=0    

        
        
    return sidar

operates=["and", "or","not"]

def dot(v1, v2):
     return sum(x*y for x,y in zip(v1,v2))
#removing stopwords
def removestop(list1):
    list2=[]
    for i in  list1:
        if not i in stop_words or i in operates:
                list2.append(i)
                
                
                         
    return list2   

def Diff(li1, li2): 
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2] 
    return li_dif     
                
    
        


totaldocs=['01.txt','02.txt','03.txt','04.txt','05.txt','06.txt','07.txt','08.txt','09.txt','10.txt','11.txt','12.txt','13.txt','14.txt','15.txt','16.txt','17.txt','18.txt','19.txt','20.txt','21.txt','22.txt','23.txt','24.txt','25.txt','26.txt','27.txt','28.txt','29.txt','30.txt','31.txt','32.txt','33.txt','34.txt','35.txt','36.txt','37.txt','38.txt','39.txt','40.txt','41.txt','42.txt','43.txt','44.txt','45.txt','46.txt','47.txt','48.txt','49.txt','50.txt']

docker=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50']

#query parsing on runtime
def Start():
 list1=[]
 list2=[]  

 
 list2.clear()
 query=input("Enter a  query\n")
 worda= query.casefold()
 worda = re.sub('-', ' ', worda)
 worda = re.sub(r"\W", " ", worda)
        # result = re.sub(r"\d", " ", result)
        # result = re.sub(r"\s+[a-z]\s+", " ", result)
 worda = re.sub(r"\s+", " ", worda)
 worda = re.sub(r"^\s", "", worda)
 worda = re.sub(r"\s$", "", worda)
 wordf = worda.split()
 wordf=removestop(wordf)
#calculating tf for each word
 for eachword in sorted(wordf):
                   qdictionary[eachword]=0
                   for i, j in enumerate(wordf):
                       if j == eachword: 
                         momo=qdictionary[eachword]
                         del qdictionary[eachword]
                         qdictionary[eachword]=momo+1

     
  
 
           
 #assigning 0 for words  not in query        
 for chapao in sorted(data):
     if chapao not in qdictionary.keys():
        qdictionary[chapao]=0
        
  
 #calculating tf*idf for query   
 finalvector={}
 for eachu in sorted(qdictionary.items()):
     s=eachu[1]
     n=eachu[0]
     qidfDict[n]=((abs(float(importedidf.get(n))) * float(s)))
     list2.append((qidfDict[n]))
 
    
 s2=l2_norm(list2)
 for i in docker:
     eachdoc=importedidftf.get(str(i))
     for m in eachdoc.items():
         for s in m[1]:
             list1.append(abs((s)))
             
             
     s1=l2_norm(list1)
     finalvector[str(i)]= dot(list1,list2) / (s1 * s2)
     list1.clear()
    
     #print(eachdoc)
     
 
 qdictionary.clear();  
 #final vector being calculated for all words in query
 listofTuples = sorted(finalvector.items() , reverse=True, key=lambda x: x[1])
 for elem in (listofTuples) :
    if(elem[1] >= 0.005): #displaying values greater than alpha
        print(elem)

   
 
             

 
 

 #importing all the exported files including idf , idf *tf and dictionary
if os.path.isfile(r"C:\Users\SHAIKH\.spyder-py3\Assign2\SavedDictionary.json") :
  a1=input("Press 1 to enter query or 2 to print IDF * TF Values or 3 to print IDF Values   or 4 to exit\n\n")  
  data = json.load(open(r"C:\Users\SHAIKH\.spyder-py3\Assign2\SavedDictionary.json"))
  importedidftf = json.load(open(r"C:\Users\SHAIKH\.spyder-py3\Assign2\ImportIDFTF.json"))
  importedidf= json.load(open(r"C:\Users\SHAIKH\.spyder-py3\Assign2\IDFDictionary.json"))
  
  while a1 != "4":
      if a1 =="1": 
       Start()   
      elif a1 =="2":
          print(importedidftf)
      elif a1 =="3":
          print(importedidf)
      elif a1=="4":
       exit
       
      a1=input("Press 1 to enter query or 2 to print IDF * TF Values or 3 to print IDF Values   or 4 to exit\n\n")  
      
        
   
  
else:  

 dictionary =defaultdict(lambda: defaultdict(list))
 dictforidfcalc=defaultdict(lambda: defaultdict(list))

 file = open(r"C:\Users\SHAIKH\.spyder-py3\Assign2\list.txt", "r")
 directory = r"C:\Users\SHAIKH\.spyder-py3\Assign2\Stories"
 stop_words = []
 for w in file:
    stop_words.extend(word_tokenize(w))

# print(stop_words)
    
 #parsing all the documents and tokenizing
 for filename in sorted((os.listdir(directory))):
    f = os.fsdecode(filename)
    if f.endswith(".txt"):
        story = open(r'C:\Users\SHAIKH\.spyder-py3\Assign2\Stories\\' + filename)
        word = story.read();
        m = word.casefold()
        worda = re.sub('-', ' ', m)
        worda = re.sub(r"\W", " ", worda)
        # result = re.sub(r"\d", " ", result)
        # result = re.sub(r"\s+[a-z]\s+", " ", result)
        worda = re.sub(r"\s+", " ", worda)
        worda = re.sub(r"^\s", "", worda)
        worda = re.sub(r"\s$", "", worda)
        wordf = worda.split()
        wordf=removestop(wordf)
        wordf.sort()
        for eachword in wordf:
                   #print(eachword)
                   sar=(os.path.splitext(os.path.basename(filename))[0])
                   dictionary[eachword][sar]=[]
                   for i, j in enumerate(wordf):
                       if j == eachword: 
                         momo=len(dictionary[eachword][sar])
                         del dictionary[eachword][sar]
                         dictionary[eachword][sar].append(momo+1)
                         
                          
                 

      
 for wordname, docid in dictionary.items():
         for key in docid:
             shaikha.append(key)
             
         dictforidfcalc[wordname]=len(shaikha);
         fi=Diff(docker,shaikha)
         for minu in sorted(fi):
            dictionary[wordname][minu]=[]
            dictionary[wordname][minu].append(0)
         
         shaikha.clear()
         fi.clear()
         
         
         
 #calculating idf*tf
 exportidftf=computeIDF(dictionary,dictforidfcalc)       
         
         
         
      
 #exporting files for future use
 json.dump(dictionary, open(r"C:\Users\SHAIKH\.spyder-py3\Assign2\SavedDictionary.json", 'w'))
 json.dump(exportidftf, open(r"C:\Users\SHAIKH\.spyder-py3\Assign2\ImportIDFTF.json", 'w'))
 Start() #starting query parsing





       


  
 


           
            
            

