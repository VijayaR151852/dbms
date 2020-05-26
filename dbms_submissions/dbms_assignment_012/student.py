class DoesNotExist(Exception):
    pass

class MultipleObjectsReturned(Exception):
    pass

class InvalidField(Exception):
    pass

class Student:
    def __init__(self,name=None,age=None,score=None):
        self.name=name
        self.age=age
        self.student_id=None
        self.score=score
    @classmethod
    def get(cls,**kwargs):
        import sqlite3
        conn=sqlite3.connect("students.sqlite3")
        field=["age","student_id","score"]
        crsr=conn.cursor()
        for key,value in kwargs.items():
            cls.val=value
            if(key in field):
                sql_query="Select * from student where {}={}".format(key,value)
            elif(key=="name"):
                sql_query="Select * from student where name='{}'".format(value)
            else:
                raise InvalidField
                
        crsr.execute(sql_query) 
        ans=crsr.fetchall()
        if(len(ans)==0):
            raise DoesNotExist
        elif(len(ans)>1):
            raise MultipleObjectsReturned
        obj=cls(ans[0][1],ans[0][2],ans[0][3])
        obj.student_id=ans[0][0]
        conn.close()
        return obj
    
    def delete(self):
        import sqlite3
        conn=sqlite3.connect("students.sqlite3")
        crsr=conn.cursor()
        crsr.execute("PRAGMA foreign_keys=on;") 
        sql_query="DELETE FROM student where student_id={}".format(self.student_id)
        crsr.execute(sql_query)
        conn.commit()
        conn.close()
        
    def save(self):
        import sqlite3
        conn=sqlite3.connect("students.sqlite3")
        crsr=conn.cursor()
        crsr.execute("PRAGMA foreign_keys=on;")
        if(self.student_id==None):
            sql_query="insert into student(name,age,score) values('{}',{},{})".format(self.name,self.age,self.score)
            crsr.execute(sql_query)
            conn.commit()
            self.student_id=crsr.lastrowid
            conn.close()
        else:
            q="select * from student where student_id={}".format(self.student_id)
            crsr.execute(q)
            ans=crsr.fetchall()
            if(len(ans))==1:
                sql_query="Update student set name='{}',age={},score={} where student_id={}".format(self.name,self.age,self.score,self.student_id)
                crsr.execute(sql_query)
                conn.commit()
                conn.close()
            else:
                sql_query="update student set student_id={},name='{}',age={},score={} where student_id={}".format(self.student_id,self.name,self.age,self.score,Student.val)
                crsr.execute(sql_query)
                conn.commit()
                conn.close()



