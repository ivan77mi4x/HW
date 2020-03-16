
# 13.02 - No yelling! 


def filter_words(st):
    return " ".join(st.capitalize().split())

print(filter_words("TeTG test HG"))


#13.02 - Unfinished Loop - Bug Fixing #1

def create_array(n):
    res=[]
    i=1
    while i<=n:
        res.append(i)
        i=i+1
    return res

print(create_array(10))



#13.02 - Find The Distance Between Two Points

def distance(x1, y1, x2, y2):
    return(round(((x2 - x1)**2 + (y2 - y1)**2)**0.5, 2))

print(distance(1,1,0,0))
