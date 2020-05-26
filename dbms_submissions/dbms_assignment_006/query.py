Q1='''select fname,lname 
    from actor inner join cast on id=pid 
    where mid=12148;'''
            
Q2='''select Count(pid) 
    from actor inner join cast on id=pid 
    where fname='Harrison (I)' and lname='Ford';'''
    
Q3='''select Distinct(pid) 
    from movie inner join cast on id=mid 
    where name like 'Young Latin Girls%';'''
    
Q4='''select count(Distinct pid) 
    from movie inner join cast on id=mid 
    where year between 1990 and 2000;'''