lyrics = """cause i i i am in the stars tonight
so watch me bring the fire and set the night alight
shoes on  get up in the morning
cup of milk  let us rock and roll
king kong  kick the drum  rolling on like a rolling stone
sing song when i am walking home
jump up to the top  lebron
ding dong  call me on my phone
ice tea and a game of ping pong  huh
this is getting heavy
can you hear the bass boom  i m ready  woo hoo
life is sweet as honey
yeah  this beat cha ching like money  huh
disco overload  i am into that  i am good to go
i am diamond  you know i glow up
hey  so let us go
cause i i i am in the stars tonight
so watch me bring the fire and set the night alight  hey
shining through the city with a little funk and soul
so i am a light it up like dynamite  whoa oh oh
bring a friend  join the crowd
whoever wanna come along
word up  talk the talk
just move like we off the wall
day or night  the sky is alight
so we dance to the break of dawn
ladies and gentlemen  i got the medicine
so you should keep ya eyes on the ball  huh
this is getting heavy
can you hear the bass boom  i am ready  woo hoo
life is sweet as honey
yeah  this beat cha ching like money
disco overload  i am into that  i am good to go
i am diamond  you know i glow up
let us go
cause i i i am in the stars tonight
so watch me bring the fire and set the night alight  hey
shining through the city with a little funk and soul
so i am a light it up like dynamite  whoa oh oh
dy na na na  na na  na na na  na na na  life is dynamite
dy na na na  na na  na na na  na na na  life is dynamite
shining through the city with a little funk and soul
so i am a light it up like dynamite  whoa oh oh
dy na na na  na na  na na  ayy
dy na na na  na na  na na  ayy
dy na na na  na na  na na  ayy
light it up like dynamite
dy na na na  na na  na na  ayy
dy na na na  na na  na na  ayy
dy na na na  na na  na na  ayy
light it up like dynamite
 cause i i i m in the stars tonight
so watch me bring the fire and set the night alight
shining through the city with a little funk and soul
so i am a light it up like dynamite  this is ah
cause i i i am in the stars tonight
so watch me bring the fire and set the night alight  alight  oh
shining through the city with a little funk and soul
so i am a light it up like dynamite  whoa  light it up like dynamite
dy na na na  na na  na na na  na na na  life is dynamite
dy na na na  na na  na na na  na na na  life is dynamite
shining through the city with a little funk and soul
so i am a light it up like dynamite  whoa oh oh"""



##### set 활용: dynamite 문제 #####

# BTS - Dynamite 에서 사용된 단어 별 등장 횟수를 중복 없이 출력

words = lyrics.split()

for i in set(words):
    print(i, words.count(i))



##### dictionary 활용: dynamite 문제 #####

# BTS - Dynamite 에서 사용된 단어 별 등장 횟수를 딕셔너리 형태로 저장

words = lyrics.split()

# key: 단어, value: 빈도수
dic = {}

for i in set(words):
    dic[i] = words.count(i)
print(dic)







