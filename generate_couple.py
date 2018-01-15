from distance_function import *
import csv

def compute(e1, e2, s):
    e1, e2 = hashing(e1), hashing(e2)
    return (e1, e2, s, jaccard_similarity(e1,e2,2), jaccard_similarity(e1,e2,3), cosine_string_similarity(e1,e2,2),
            cosine_string_similarity(e1,e2,3), Levenshtein.jaro(e1,e2), Levenshtein.jaro_winkler(e1,e2, prefix_weight=3), Levenshtein.ratio(e1,e2))
if __name__ == '__main__':
    with open("email-pop.txt","r",encoding="utf-8") as f:
        liste_simi = [[email.split("@")[0] for email in x.split("\n") if len(email) > 1] for x in f.read().split('##')]

    emails = [compute(email_1,email_2,True) for group in liste_simi[:] for i,email_1 in enumerate(group) for email_2 in group[i+1:]]
    temp = [compute(email_1,email_2,False) for i,group in enumerate(liste_simi[:500]) for email_1 in group for group2 in liste_simi[i+1:500] for email_2 in group2]
    l = [("email1","email2","Classe","Jaccard (n=2)","Jaccard (n=3)","Cosine (n=2)","Cosine (n=3)",
          "Jaro","Winkler","Levenshtein")] + emails + temp
    with open("data_simi_sept.csv", "w", newline='') as f:
        writer = csv.writer(f,delimiter=',')
        writer.writerows(l)
