def read_data(sql_query):
    import sqlite3
    connection = sqlite3.connect("students.sqlite3")
    crsr = connection.cursor() 
    crsr.execute(sql_query) 
    ans= crsr.fetchall()  
    connection.close() 
    return ans

class InvalidField(Exception):
    pass

class Student:
    def __init__(self,name=None,age=None,score=None):
        self.name=name
        self.age=age
        self.student_id=None
        self.score=score  
        
    @classmethod
    def filter(cls,**kwargs):
        #print(*cls().__dict__.keys())
        fields=[*cls().__dict__.keys()]
        #print(fields)
        '''query_att=[]
        dic={"gt":">","lt":"<","lte":"<=","gte":">=","neq":"<>"}
        for key,value in kwargs.items():
            if("__" in key):
                temp_field,expression=key.split("__")
                if(temp_field not in fields):
                    raise InvalidField
                else:
                    if(expression=="contains"):
                        sql_query="name like '%{}%'".format(value)
                    elif(expression=="in"):
                        s=",".join("'"+str(i)+"'" for i in value) 
                        sql_query="{} in ({})".format(str(temp_field),s)
                    else:
                        sql_query="{} {} '{}'".format(temp_field,dic[expression],value)
            else:
                if(key not in fields):
                    raise InvalidField
                else:
                    sql_query="{}='{}'".format(key,value)
            query_att.append(sql_query)
        query_att_string=" and ".join(i for i in query_att)
        return query_att_string
        
    @classmethod
    def aggregate(cls,aggregation,field=None,**kwargs):
        fields=["name","student_id","age","score"]
        if(len(kwargs)>=1):
            query_att_string=cls.filter(**kwargs)
            multiple_sql_query="select {}({}) from student where {}".format(aggregation,field,query_att_string)
        elif(field==None):
            multiple_sql_query="select count(*) from student"
        else:
            if(field not in fields):
                raise InvalidField
            else:
                multiple_sql_query="select {}({}) from student".format(aggregation,field) 
        ans=read_data(multiple_sql_query)
        ans=ans[0][0]
        return ans
        
    @classmethod
    def avg(cls,field,**kwargs):
        ans=cls.aggregate("avg",field,**kwargs)
        return ans
    
    @classmethod
    def min(cls,field,**kwargs):
        ans=cls.aggregate("min",field,**kwargs)
        return ans
    
    @classmethod
    def max(cls, field, **kwargs):
        ans=cls.aggregate("max",field,**kwargs)
        return ans
    
    @classmethod
    def sum(cls, field, **kwargs):
        ans=cls.aggregate("sum",field,**kwargs)
        return ans
    
    @classmethod
    def count(cls, field=None, **kwargs):
        ans=cls.aggregate("count",field,**kwargs)
        return ans'''
        
Student.filter(age=20)
