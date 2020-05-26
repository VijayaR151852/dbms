Q1='''select count(id) 
        from movie 
        where year<2000;'''
Q2='''select avg(rank) 
        from movie 
        where year=1991;'''
Q3='''select min(rank) 
        from movie 
        where year=1991;'''
Q4='''select fname,lname 
        from cast inner join actor on id=pid  
        where mid=27;'''
Q5='''select count(mid) 
        from actor inner join cast on id=pid    
        where fname="Jon" and lname="Dough";'''
Q6='''select name 
        from movie 
        where (name like "Young Latin Girls%")
        and 
        (year between 2003 and 2006);'''
Q7='''select fname,lname 
        from Director 
        where id in
        (select did from moviedirector 
        where mid in(select id from movie where name like "Star Trek%"));'''
Q8='''select name from movie 
        where id in(select mid from moviedirector where did in
        (select id from director where fname ="Jackie (I)" and lname="Chan") 
        intersect 
        select mid from cast where pid in
        (select id from actor where fname ="Jackie (I)" and lname="Chan")) 
        order by name asc;'''
Q9='''select fname,lname 
        from(director inner join moviedirector on `director`.id=did) as data 
        inner join movie on `movie`.id=`data`.mid 
        where `movie`.year=2001 group by did having count(`data`.did)>=4 
        order by fname asc,lname desc;'''
Q10='''select gender,count(gender) 
        from actor group by gender order by gender;'''
Q11='''select distinct m1.name,m2.name,m1.rank,m1.year 
        from movie m1,movie m2 
        where (m1.rank==m2.rank 
        and m1.year==m2.year)
        and m1.name<>m2.name
        order by m1.name limit 100;'''
Q12='''select `actor`.fname,`movie`.year,avg(`movie`.rank) 
        fromq(actor inner join cast on `actor`.id=pid) as first 
        inner join movie on `first`.mid=`movie`.id
        group by `actor`.id,`movie`.rank order by `actor`.fname ASC,`movie`.year DESC limit 100;'''
Q13= '''select `actor`.fname,`director`.fname,avg(`movie`.rank) as score
        from movie
        inner join cast on `movie`.id=`cast`.mid
        inner join moviedirector on `cast`.mid=`moviedirector`.mid 
        inner join actor on `cast`.pid=`actor`.id 
        inner join director on `moviedirector`.did=`director`.id
        group by `actor`.id,`director`.id 
        having count(`moviedirector`.mid)>=5 
        order by score desc,`director`.fname asc,`actor`.fname asc limit 100;'''
