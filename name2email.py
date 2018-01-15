if __name__ == '__main__':
    with open("names.txt","r",encoding="utf-8") as f:
        names= [tuple(ligne.strip().split(" ")) for ligne in f.readlines()]

    couple=[]
    for i in range(1,len(names)-1):
        print(i)
        couple.append((names[i][0],names[i][1]))
        couple.append((names[i][0],names[i-1][1]))
        couple.append((names[i][0],names[i+1][1]))

    with open("email-pop.txt","w",encoding="utf-8") as f:
        for prenom,nom in couple:
            f.write("{}.{}@test.com\n".format(prenom,nom))
            f.write("{}.{}@test.com\n".format(nom,prenom))
            f.write("{}{}@test.com\n".format(prenom[0],nom))
            if len(prenom) >=5:
                f.write("{}.{}@test.com\n".format(prenom[:3],nom))
            if len(nom) >=5:
                f.write("{}{}@test.com\n".format(prenom,"".join(filter(lambda x: x not in "aeiuoy", nom))))
            f.write("##\n")