Q1='''
select player.player_id,matchcaptain.team_id,jersey_no,name,date_of_birth,age 
from player inner join matchcaptain on captain=player.player_id
left join goaldetails on captain=goaldetails.player_id
where goal_id is null;
'''

Q2='''
select team_id,count(match_no) from matchteamdetails group by team_id;
'''

Q3='''
select team_id,
(select count(goal_id) 
from goaldetails
where team_id=g.team_id)/cast((select count(player_id) from player where team_id=g.team_id) as float) as avg_goal_score from team g where avg_goal_score>0;
'''

Q4='''
select captain,count(match_no) as no_of_times_captain 
from matchcaptain
group by captain; 
'''

Q5='''
select count(distinct(captain)) as no_players 
from matchcaptain 
inner join match on matchcaptain.match_no=match.match_no
where captain=player_of_match;
'''

Q6='''
select distinct(player_id) from player 
where player_id in(select captain from matchcaptain)
and player_id not in(select player_of_match from match);
'''

Q7='''
select strftime('%m',play_date) as month,count(match_no) 
from match 
group by month 
order by count(match_no) desc;
'''

Q8='''
select jersey_no,count(captain) 
from matchcaptain inner join player on player_id=captain 
group by jersey_no order by count(captain) desc,jersey_no desc;
'''

Q9='''
select player_id,avg(audience)
from match inner join matchteamdetails on matchteamdetails.match_no=match.match_no 
inner join player on matchteamdetails.team_id=player.team_id 
group by player_id
order by avg(audience) desc,player_id desc;
'''

Q10='''
select team_id,avg(age) from player group by team_id;
'''

Q11='''
select avg(age) from player inner join matchcaptain on player_id=captain;
'''

Q12='''
select strftime('%m',date_of_birth) as month,count(player_id) 
from player
group by month
order by count(player_id) desc,month desc;
'''

Q13='''
select captain,count(win_lose) 
from matchteamdetails 
inner join matchcaptain on matchteamdetails.match_no=matchcaptain.match_no
where win_lose="W" and matchcaptain.team_id=matchteamdetails.team_id
group by captain 
order by count(*) desc;
'''
