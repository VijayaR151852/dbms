Q1='''
    select avg(age) from player;
    '''

Q2='''select match_no,play_date from match 
    where audience>50000 
    order by match_no asc;'''
    
Q3='''select team_id,count(win_lose) from matchteamdetails 
    where win_lose="W" group by team_id 
    order by count(win_lose) desc,team_id asc;'''
    
Q4='''select match_no,play_date from match 
    where stop1_sec>(select avg(stop1_sec) from match)
    order by match_no desc;'''

Q5='''select match_no,`team`.name,`player`.name 
    from matchcaptain 
    inner join team on `team`.team_id=`matchcaptain`.team_id 
    inner join player on `player`.player_id=`matchcaptain`.captain
    order by match_no,`team`.name;'''

Q6='''select `match`.match_no,`player`.name,`player`.jersey_no 
    from  match inner join player on `player`.player_id=`match`.player_of_match 
    group by match_no
    order by match_no asc;'''

Q7='''select `team`.name,avg(age) 
    from player inner join team on `player`.team_id =`team`.team_id
    group by `team`.team_id having avg(age)>26
    order by `team`.name;'''
    
Q8='''
    select `player`.name,jersey_no,age,count(goal_id)
    from goaldetails inner join player on `goaldetails`.player_id=`player`.player_id
    where age<=27
    group by `goaldetails`.player_id 
    order by count(goal_id) desc,`player`.name;
    '''
    
Q9='''
    select team_id,count(goal_id)*100.0/(select count(goal_id) from goaldetails)
    from goaldetails 
    group by team_id;
    '''

Q10='''select avg(total) from
    (select count(goal_id) as total from goaldetails group by team_id);'''
    
Q11='''
    select `player`.player_id,name,date_of_birth from player
    where player_id not in(select `goaldetails`.player_id from goaldetails) order by player_id asc;
    '''
   
Q12='''
    select `team`.name,`match`.match_no,audience,audience-(select avgerage
    from(select `matchteamdetails`.team_id,avg(audience) as avgerage from matchteamdetails 
    inner join match on `matchteamdetails`.match_no=`match`.match_no group by `matchteamdetails`.team_id) as inner
    where 'inner'.team_id=`outer`.team_id)
    from (matchteamdetails inner join match on `matchteamdetails`.match_no=`match`.match_no 
    inner join team on `matchteamdetails`.team_id=`team`.team_id) as outer order by `match`.match_no asc;
    '''
    