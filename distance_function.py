import numpy as np
import Levenshtein

def ngram(s, n=2):
    s = list(s)
    return [tuple(s[i:i+n]) for i in range(len(s)-n+1)]

def jaccard_similarity(s1, s2, n=2):
    '''
    1 -> proche et 0 -> different
    :param s1: string 1
    :param s2: string 2
    :param n: n-gram
    :return: similarity between s1 and s2
    '''
    t1 = set(ngram(s1,n))
    t2 = set(ngram(s2,n))
    #print(t1)
    #print(t2)
    inter = t1.intersection(t2)
    union = t1.union(t2)
    return len(inter)/len(union) # tout en commun donne 1

def cosine_distance(v1,v2):
    # v1 et v2 doivent être des vecteurs de nombres
    n1 = np.linalg.norm(v1)
    n2 = np.linalg.norm(v2)
    norms = n1*n2
    if norms !=0:
        return np.dot(v1,v2)/norms # si proche donne 0
    else:
        return 0

def cosine_string_similarity(s1,s2,n=2):
    t1 = set(ngram(s1,n))
    t2 = set(ngram(s2,n))
    t = t1.union(t2)
    v1 = [1 if x in t1 else 0 for x in t]
    v2 = [1 if x in t2 else 0 for x in t]
    #print(t)
    #print(v1,v2)
    return cosine_distance(v1,v2)

def hashing(email):
    return "".join(filter(lambda x:x.isalpha(),email))


if __name__ == '__main__':
    st1 = "servicesachats.enligne"
    st2 = "service"
    k=3
    print(jaccard_similarity(st1,st2,k))
    print(cosine_string_similarity(st1,st2,k))
    print(Levenshtein.distance(st1,st2))
    print(Levenshtein.ratio(st1,st2))
    print(Levenshtein.jaro(st1,st2)) # Jaro: si identique donne 1
    print(Levenshtein.jaro_winkler(st1,st2))