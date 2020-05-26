Q5='''
select distinct derived.mid,female_actors,male_actors from
((select mid,count(pid) as female_actors from actor inner join cast on pid=id where gender="F" group by mid) as female
inner join
(select mid,count(pid) as male_actors from actor inner join cast on pid=id where gender="M" group by mid) as male
on female.mid=male.mid) as derived 
order by derived.mid asc
limit 100;
'''

Q1='''
select actor.id,actor.fname,actor.lname,gender 
from actor inner join cast on actor.id=pid
inner join movie on movie.id=mid 
where name like "Annie%";
'''

Q2='''
select movie.id,movie.name,movie.rank,movie.year 
from movie inner join moviedirector on movie.id=moviedirector.mid
inner join director on moviedirector.did=director.id
where fname ="Biff" and lname="Malibu" and year in(1999,1994,2003)
order by rank desc,year;
'''

Q3='''
select year,count(*) from movie 
group by year 
having avg(rank)>(select avg(rank) from movie)
order by year;
'''

Q4='''
select * from movie 
where year=2001 and rank<(select avg(rank) from movie)
order by rank desc
limit 10;
'''

Q6='''
select distinct pid
from cast
group by pid,mid
having count(distinct role)>1
order by pid
limit 100;
'''

Q7='''
select distinct(fname),count(*) from director group by fname having count(*)>1;
'''

Q8='''
select director.id,director.fname,director.lname 
from director
where exists(select did from cast inner join moviedirector on `moviedirector`.mid=`cast`.mid where `moviedirector`.did=id group by `moviedirector`.mid having count(distinct pid)>=100)
and not exists(select did from cast  inner join moviedirector on `moviedirector`.mid=`cast`.mid where `moviedirector`.did=id group by `moviedirector`.mid having count(distinct pid)<100);   
'''


Q9='''
select id,
(select count(pid) from actor inner join cast on pid=id where gender="F" and mid=c.id),
(select count(pid) from actor inner join cast on pid=id where gender="M" and mid=c.id) 
from movie as c
order by id
limit 100;
'''
