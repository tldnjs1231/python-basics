# Q. 첫줄부터 단어를 이어붙히려고한다. 붙히고자하는 단어가 A, B 일 때 A 의 뒷부분과 B 의 앞부분이 최대로 같을 때 까지 당겨서 이어적는다고 했을 때, 아래 단어들을 이어붙힌 전체 길이를 구해라.
# ( 이때, A 는 N 번째 줄 B 는 N+1 번째줄의 단어를 의미한다 )

# ex1) apple    +   lemon            >   le 가 겹치기 때문에   applemon 
# ex2) watermelon   +   melon      >   melon 이 겹치기 때문에  watermelon
# ex3) apple    +     pineapple        >  겹치치 않기 때문에 applepineapple
# ex4) pineapple  +   apple           > apple 이 겹치기 때문에 pineapple
# ex5) love  +  like                     > 겹치지 않기 때문에 lovelike
# ex6) jeju + juice                     >   ju 가 겹치기 때문에 jejuice
# ex7) piano + orange               > o 가 겹치기 때문에 pianorange



# Q. 고1 영단어 1000 개입니다. 다음 단어 중 모음이 세 종류 이상 들어간 단어들을 이어적었을 때 다음 문자들을 조합해주세요. (모음 : aeiou)

voca = ['require', 'technology', 'individual', 'provide', 'object', 'level', 'involve', 'employ', 'attitude', 'improve', 'research', 'supply', 'tend', 'affect', 'thus', 'benefit', 'demand', 'occasion', 'fashion', 'recognize', 'proper', 'due', 'behave', 'opportunity', 'determine', 'generate', 'exist', 'regret', 'occur', 'available', 'professional', 'frequent', 'contact', 'respond', 'emotional', 'diet', 'severe', 'gloom', 'negative', 'victim', 'biology', 'obtain', 'heal', 'influence', 'critical', 'aware', 'civil', 'immediate', 'material', 'compose', 'permit', 'advantage', 'region', 'insist', 'conclude', 'term', 'approach', 'desire', 'reduce', 'fuel', 'conviction', 'occupy', 'efficient', 'despite', 'issue', 'account', 'secretary', 'firm', 'merely', 'complex', 'audience', 'relieve', 'academic', 'horror', 'threat', 'pure', 'mood', 'consume', 'explode', 'approve', 'steady', 'moral', 'psychology', 'tide', 'secure', 'witness', 'decrease', 'guarantee', 'shadow', 'frustrate', 'pupil', 'leisure', 'annoy', 'portion', 'client', 'expert', 'describe', 'duty', 'define', 'positive', 'participate', 'average', 'publish', 'detail', 'novel', 'oppose', 'delight', 'essential', 'brief', 'intend', 'amaze', 'balance', 'violent', 'arrange', 'lack', 'struggle', 'rely', 'revolution', 'claim', 'attempt', 'injure', 'significant', 'seldom', 'admit', 'grant', 'embarrass', 'interrupt', 'pot', 'decade', 'edge', 'delay', 'indicate', 'error', 'focus', 'mental', 'labor', 'guilty', 'apologize', 'mass', 'feature', 'typical', 'capable', 'accustom', 'nevertheless', 'agriculture', 'minority', 'emphasis', 'sum', 'contrary', 'crazy', 'ray', 'appeal', 'authority', 'comment', 'suspect', 'leap', 'mechanic', 'manufacture', 'brilliant', 'generous', 'decorate', 'factor', 'purchase', 'reveal', 'previous', 'tone', 'ultimate', 'horizon', 'grain', 'companion', 'consequence', 'stock', 'laboratory', 'sufficient', 'sake', 'isolate', 'apparent', 'evolve', 'digest', 'quantity', 'inner', 'reject', 'permanent', 'impact', 'goat', 'telescope', 'species', 'evaluate']


# ex) avatar 의 경우 들어간 모음의 종류는 하나이다.
#      elephant 의 경우 들어간 모음의 종류는 두개이다.
     

# - 7 번째 문자
# - 62 번째 문자
# - 164 번째 문자
# - 279 번째 문자
# - 352 번째 문자
# - 391 번째 문자
# - 408 번째 문자
# - 마지막문자

# erdutaue








