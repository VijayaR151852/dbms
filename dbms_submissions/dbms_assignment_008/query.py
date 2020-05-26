Q1='''select `director`.id,`director`.fname from director
    where exists(select mid from moviedirector inner join movie on `movie`.id=`moviedirector`.mid
    where year>2000 and `director`.id=`moviedirector`.did)
    and not exists(select mid from moviedirector inner join movie on `movie`.id=`moviedirector`.mid
    where year<2000 and `director`.id=`moviedirector`.did)
    order by `director`.id asc;'''
    
Q2='''select `d`.fname,(select name from movie inner join moviedirector
    on `movie`.id=`MovieDirector`.mid where `moviedirector`.did=`d`.id
    order by rank desc,name asc limit 1) from director as d limit 100;'''
    
Q3='''select * from actor 
    where not exists(select mid from cast inner join movie on `cast`.mid=`movie`.id
    where `actor`.id=`cast`.pid and `movie`.year between 1990 and 2000) 
    order by `actor`.id desc limit 100;'''
