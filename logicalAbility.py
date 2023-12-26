

matrix =[{'id : 0', 'name : a', 'description : aa', 'level : 1', "parent_id : 'none'"},

{'id : 1', 'name : b', 'description : bb', 'level : 2', 'parent_id : 0'},

{'id : 2', 'name : c', 'description : cc', 'level : 3', 'parent_id : 1'},

{'id : 3', 'name : b23', 'description : bb', 'level : 2', 'parent_id : 1'},

{'id : 4', 'name : c45', 'description : cc', 'level : 3', 'parent_id : 3'}]
#getid---->get category id then-->>filter all on the basics of category id and append as matrix and id==>>

def fun(matrix,id):
   # its takes matrix and keyid and return dictionary and its key
   res={}
   for i in range(len(matrix)):
      if(matrix[i]['keyid']==id):
         res["name"] = matrix[i]['name']
         res["description"] = matrix[i]['description']
         res["parent_id"] = matrix[i]['parent_id']
   return res

def utilty(matrix,id):
   
      
         
         



