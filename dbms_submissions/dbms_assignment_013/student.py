def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("selected_students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()
	
def read_data(sql_query):
    import sqlite3
    connection = sqlite3.connect("selected_students.sqlite3")
    crsr = connection.cursor() 
    crsr.execute(sql_query) 
    ans= crsr.fetchall()  
    connection.close() 
    return ans

class InvalidField(Exception):
    pass

class MultipleObjectsReturned(Exception):
    pass

class DoesNotExist(Exception):
    pass

class Student:
    def __init__(self,name=None,age=None,score=None):
        self.name=name
        self.age=age
        self.student_id=None
        self.score=score    
        
    def __repr__(self):
        return "Student(student_id={0}, name={1}, age={2}, score={3})".format(
            self.student_id,
            self.name,
            self.age,
            self.score)
       
    @classmethod
    def get(cls,**kwargs):
        field=["age","student_id","score"]
        for key,value in kwargs.items():
            cls.val=value
            if(key in field):
                sql_query="Select * from student where {}={}".format(key,value)
            elif(key=="name"):
                sql_query="Select * from student where name='{}'".format(value)
            else:
                raise InvalidField
        ans=read_data(sql_query)
        if(len(ans)==0):
            raise DoesNotExist
        elif(len(ans)>1):
            raise MultipleObjectsReturned
        obj=cls(ans[0][1],ans[0][2],ans[0][3])
        obj.student_id=ans[0][0]
        return obj
        
    def delete(self):
        sql_query="DELETE FROM student where student_id={}".format(self.student_id)
        write_data(sql_query)
        
    def save(self):
        if self.student_id is None:
            sql_query="insert into student(name,age,score) values('{}',{},{})".format(self.name,self.age,self.score)
            write_data(sql_query)
            record="select student_id from student where name='{}' and age={} and score={}".format(self.name,self.age,self.score)
            record_result=read_data(record)
            self.student_id=record_result[0][0]
        else:
            sql_query1="update student set student_id={},name='{}',age={},score={} where student_id={}".format(self.student_id,self.name,self.age,self.score,self.val)
            write_data(sql_query1)   
    
    @classmethod        
    def filter(cls,**kwargs):
        query_att=[]
        objects=[]
        dic={"gt":">","lt":"<","lte":"<=","gte":">=","neq":"<>"}
        fields=["name","student_id","age","score"]
        for key,value in kwargs.items():
            if("__" in key):
                field,expression=key.split("__")
                if(field not in fields):
                    raise InvalidField
                else:
                    if(expression=="contains"):
                        sql_query="name like '%{}%'".format(value)
                    elif(expression=="in"):
                        s=",".join("'"+str(i)+"'" for i in value) 
                        sql_query="{} in ({})".format(str(field),s)
                    else:
                        sql_query="{} {} '{}'".format(field,dic[expression],value)
            else:
                if(key not in fields):
                    raise InvalidField
                else:
                    sql_query="{}='{}'".format(key,value)
            query_att.append(sql_query)
      
        query_att_string=" and ".join(i for i in query_att)
        multiple_sql_query="select * from student where {}".format(query_att_string)
        ans=read_data(multiple_sql_query)
        for res in range (len(ans)):
            obj=cls(ans[res][1],ans[res][2],ans[res][3])
            obj.student_id=ans[res][0]
            objects.append(obj)
        return objects

