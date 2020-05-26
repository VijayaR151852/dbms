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
        crsr=conn.cursor()
        sql_query=""
        for key,value in kwargs.items():
            field,expression=key.split("__")
            if(expression=="gt"):
                sql_query="Select * from Student where {}>{}".format(field,value)
            if(expression=="gte"):
                sql_query="Select * from Student where {}>={}".format(field,value)
            if(expression=="lt"):
                sql_query="Select * from Student where {}<{}".format(field,value)
            if(expression=="lte"):
                sql_query="Select * from Student where {}<={}".format(field,value)
                
        crsr.execute(sql_query) 
        ans=crsr.fetchall()
        conn.close()
        return ans
    
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
            sql_query="insert into student(student_id,name,age,score) values(null,'{}',{},{})".format(self.name,self.age,self.score)
            crsr.execute(sql_query)
            self.student_id=crsr.lastrowid
        else:
            sql_query="Update student set name='{}',age={},score={} where student_id={}".format(self.name,self.age,self.score,self.student_id)
            crsr.execute(sql_query)
        conn.commit()
        conn.close()
        
s=Student.get(age__gt=30)
print(s)