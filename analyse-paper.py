import numpy as np
#from scipy.stats import norm
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve
import pandas as pd
import matplotlib
matplotlib.style.use("ggplot")

if __name__ == '__main__':
    # with open( "data_simi_test.csv", "r",encoding="utf-8" ) as f:
    #     reader = csv.DictReader(f)
    #     ls= []
    #     lns = []
    #     classe = []
    #     score_leven = []
    #     for row in reader:
    #         classe.append(1 if row["Classe"]=="True" else 0)
    #         score_leven.append(float(row["Levenshtein"]))
    #         if row["Classe"] == "True":
    #             ls.append(float(row["Levenshtein"]))
    #         else:
    #             lns.append(float(row["Levenshtein"]))
    # print(len(ls), len(lns))
    df = pd.read_csv("data_simi_sept.csv", header=0, index_col=False,
                     converters={2: lambda x: 1 if x == "True" else 0, 3: float, 4: float, 5: float, 6: float, 7: float,
                                 8: float, 9: float})
    # plt.figure("Figure 1")
    # df.groupby("Classe").Levenshtein.plot(kind='hist',bins=50, alpha=0.6, normed=True, legend=True)
    # plt.legend(loc="upper right")
    # plt.show()



    # plt.figure("Figure 1")
    # # Plot the histogram.
    # plt.hist(lns, bins=50, normed=True, alpha=0.6, color='r',
    #          label="non similar username")
    # # Plot the PDF.
    # xmin, xmax = plt.xlim()
    # x = np.linspace(xmin, xmax, 100)
    #
    # # Plot the histogram.
    # plt.hist(ls, bins=50, normed=True, alpha=0.6, color='g',
    #          label="similar username")
    # # Plot the PDF.
    # xmin, xmax = plt.xlim()
    # x = np.linspace(xmin, xmax, 100)
    #
    # title = "Similarité de Levenshtein"
    # plt.legend(loc='upper right')
    # plt.xlabel('Similarité')
    # plt.ylabel('Pourcentage de comparaison dans les différents groupes (en %)')
    # plt.title(title)
    # plt.grid(True)
    # plt.savefig("levenshtein.png")
    # plt.show()

    #ROC curve
    # fpr, tpr, thresholds = roc_curve(df["Classe"], df["Levenshtein"], pos_label=1)
    # plt.figure("Figure 2")
    # lw=2
    # plt.plot(fpr,tpr, color="darkorange",lw=lw, label="ROC curve")
    # plt.plot([0,1],[0,1],color="navy",lw=lw,linestyle="--")
    # plt.xlim([-0.05,1.0])
    # plt.ylim([0.0, 1.05])
    # plt.xlabel('False Positive Rate')
    # plt.ylabel('True Positive Rate')
    # plt.title("ROC curve pour l'algorithme de Levenshtein")
    # plt.legend(loc="lower right")
    # plt.show()
    g, ax3 = plt.subplots(1,1)
    ax3.plot([0,1],[0,1],color="navy",lw=2,linestyle="--")
    ax3.set_xlim([-0.05,1.0])
    ax3.set_ylim([0.0, 1.05])
    ax3.set_xlabel('False Positive Rate')
    ax3.set_ylabel('True Positive Rate')
    ax3.set_title("ROC curve for the different algorithms")

    cmap = ["firebrick","darkorange","gold","green","dodgerblue","blueviolet","orchid"]
    cmap= dict([(k,v) for k,v in zip(df.columns.values.tolist()[3:],cmap)])
    styplemap= ["-","-",":",":","-","-","-"]
    styplemap = dict([(k, v) for k, v in zip(df.columns.values.tolist()[3:], styplemap)])
    for col in df.columns.values.tolist()[3:]:
        print(col)
        fpr, tpr, thresholds = roc_curve(df["Classe"], df[col], pos_label=1)
        ax3.plot(fpr, tpr, color=cmap[col], linestyle=styplemap[col], lw=2, label=col, alpha=1)
        fpr, fnr = list(map(lambda x: x*100, fpr)), list(map(lambda x: (1-x)*100, tpr))
        #t = list(filter(lambda x: x<1,fnr))[-1]
        t,fnr_t, fpr_t = [(t,n,p) for t,n,p in zip(thresholds,fnr,fpr) if n<1][0]
        f, ax = plt.subplots(1,1)
        h1 = df[df["Classe"]==1].hist(ax=ax, column=col,color='g', label='Similar addresses (n={})'.format(len(df[df["Classe"]==1])), normed=True, alpha=0.6, bins=50, histtype='bar', ec='grey')
        h2 = df[df["Classe"] == 0].hist(ax=ax, column=col, color='r', label='Non similar addresses (n={})'.format(len(df[df["Classe"]==0])), normed=True, alpha=0.6, bins=50, histtype='bar', ec='grey')
        ax.set_xlim([0,1])
        ax.set_xlabel("Similarity score")
        ax.set_ylabel("Proportion of addresses (in %)")
        ax2 = ax.twinx()
        l1 = ax2.plot(thresholds, fnr, color="darkgreen", label="False negative rate (FNR)")
        l2 = ax2.plot(thresholds, fpr, color="firebrick", label="False positive rate (FPR)")
        l3 = ax2.plot((t,t), (0,100), color="darkslategray", linestyle="--", label="Decision threshold (T) with FNR < 1%\n T = {:.2f}, FNR={:.2f}%, FPR={:.2f}%".format(t,fnr_t,fpr_t))
        ax2.set_ylabel('False positive and false negative rates (in %)')
        ax2.set_ylim([-1,105])
        ax2.set_xlim([-0.05, 1])
        ax2.tick_params('y')
        ax2.grid(False)
        lines, labels = ax.get_legend_handles_labels()

        lines2, labels2 = ax2.get_legend_handles_labels()
        ax2.legend(lines + lines2, labels + labels2, loc='lower center', bbox_to_anchor=(.5, -0.5))# bbox: position en x et y
        # Shink current axis by 20%
        # box = ax.get_position()
        # ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        # ax2.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        ax.set_title("{} algorithm".format(col))
        f.savefig('./fig/sept_crossname/{}.png'.format(col), bbox_inches='tight')
        #plt.show()
    ax3.legend(loc="lower right")
    g.savefig('./fig/sept_crossname/ROC-2.png', bbox_inches='tight')