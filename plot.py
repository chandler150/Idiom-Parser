import matplotlib.pylab as plt
import numpy as np
from os.path import expanduser
import matplotlib as mpl
import matplotlib.font_manager as font_manager
import os.path as path
import matplotlib as mpl
import math
print("Your style sheets are located at: {}".format(path.join(mpl.__path__[0], 'mpl-data', 'stylelib')))

def set_size(width, fraction=1):
    """Set figure dimensions to avoid scaling in LaTeX.

    Parameters
    ----------
    width: float
            Document textwidth or columnwidth in pts
    fraction: float, optional
            Fraction of the width which you wish the figure to occupy

    Returns
    -------
    fig_dim: tuple
            Dimensions of figure in inches
    """
    # Width of figure (in pts)
    fig_width_pt = width * fraction

    # Convert from pt to inches
    inches_per_pt = 1 / 72.27

    # Golden ratio to set aesthetic figure height
    # https://disq.us/p/2940ij3
    golden_ratio = (5**.5 - 1) / 2

    # Figure width in inches
    fig_width_in = fig_width_pt * inches_per_pt
    # Figure height in inches
    fig_height_in = fig_width_in * golden_ratio

    fig_dim = (fig_width_in, fig_height_in)

    return fig_dim

def fic():
    #*************************************************************************
    #WORKS OF FICTION PLOTS
    newnewx = []

    w_fic = {'w_fic_2006.txt': 717, 'w_fic_2010.txt': 721, 'w_fic_2004.txt': 707, 'w_fic_1993.txt': 625, 'w_fic_1995.txt': 724, 'w_fic_2007.txt': 705, 'w_fic_1991.txt': 677, 'w_fic_1990.txt': 670, 'w_fic_2000.txt': 694, 'w_fic_1997.txt': 667, 'w_fic_1998.txt': 663, 'w_fic_2009.txt': 728, 'w_fic_2002.txt': 664, 'w_fic_2012.txt': 536, 'w_fic_1999.txt': 720, 'w_fic_2011.txt': 767, 'w_fic_2008.txt': 752, 'w_fic_2001.txt': 684, 'w_fic_2005.txt': 673, 'w_fic_2003.txt': 737, 'w_fic_1994.txt': 661, 'w_fic_1996.txt': 617, 'w_fic_1992.txt': 596}
    w_fic_num_sent = {'w_fic_2006.txt': 311175, 'w_fic_2010.txt': 300437, 'w_fic_2004.txt': 321470, 'w_fic_1993.txt': 316856, 'w_fic_1995.txt': 311307, 'w_fic_2007.txt': 334370, 'w_fic_1991.txt': 331047, 'w_fic_1990.txt': 336203, 'w_fic_2000.txt': 305742, 'w_fic_1997.txt': 282500, 'w_fic_1998.txt': 300948, 'w_fic_2009.txt': 301259, 'w_fic_2002.txt': 297282, 'w_fic_2012.txt': 178155, 'w_fic_1999.txt': 339736, 'w_fic_2011.txt': 314645, 'w_fic_2008.txt': 317487, 'w_fic_2001.txt': 309406, 'w_fic_2005.txt': 309815, 'w_fic_2003.txt': 327060, 'w_fic_1994.txt': 310585, 'w_fic_1996.txt': 300924, 'w_fic_1992.txt': 314609}
    myList = w_fic.items()


    myList = sorted(myList)
    print(myList)
    x, y = zip(*myList)
    newx = []
    newy = []
    newnewx = []
    for i in range(len(x)):
        #print(x[i])
        newx.append(x[i].split('_')[2].split('.')[0])
        newy.append((y[i]/w_fic_num_sent[x[i]])*100)
    #print(newy)
    # Pure # of Idioms recognized
    return sum(y)
    return truncate(sum(newy)/len(newy),2)

    for i in newx:
        newnewx.append(int(i))

    width = 506.295
    fig, ax = plt.subplots(1, 1, figsize=set_size(width))
    ax.plot(newnewx, newy)
    plt.title("Idiom Use Rate in the Genre of Fiction ")
    plt.xlabel("By Year")
    plt.ylabel("Percentage Rate per Sentence in Corpus")
    plt.xticks(fontsize=10)
    plt.xticks(np.arange(min(newnewx), max(newnewx) + 1, 5.0))
    #plt.plot(newnewx, y)
    plt.style.use('tex')
    plt.style.use('seaborn')
    plt.show()
    fig.savefig('Fiction_rel.jpg', format='jpg', bbox_inches='tight')

    #*************************************************************************
    #WORKS OF ACADEMICS PLOTS
    #*************************************************************************
def acad():
    newnewx = []
    w_acad = {'w_acad_1993.txt': 417, 'w_acad_2005.txt': 388, 'w_acad_2009.txt': 430, 'w_acad_2000.txt': 424, 'w_acad_1997.txt': 430, 'w_acad_2012.txt': 225, 'w_acad_2006.txt': 415, 'w_acad_1990.txt': 376, 'w_acad_1995.txt': 386, 'w_acad_1996.txt': 417, 'w_acad_2004.txt': 396, 'w_acad_2011.txt': 438, 'w_acad_2002.txt': 401, 'w_acad_1991.txt': 370, 'w_acad_2001.txt': 439, 'w_acad_1998.txt': 416, 'w_acad_2007.txt': 450, 'w_acad_2008.txt': 350, 'w_acad_2010.txt': 397, 'w_acad_1999.txt': 405, 'w_acad_1992.txt': 390, 'w_acad_1994.txt': 396, 'w_acad_2003.txt': 373}
    w_acad_num_sent = {'w_acad_1993.txt': 180745, 'w_acad_2005.txt': 162078, 'w_acad_2009.txt': 211634, 'w_acad_2000.txt': 166766, 'w_acad_1997.txt': 189965, 'w_acad_2012.txt': 131009, 'w_acad_2006.txt': 170247, 'w_acad_1990.txt': 164249, 'w_acad_1995.txt': 177811, 'w_acad_1996.txt': 178520, 'w_acad_2004.txt': 169140, 'w_acad_2011.txt': 215261, 'w_acad_2002.txt': 168503, 'w_acad_1991.txt': 169017, 'w_acad_2001.txt': 163290, 'w_acad_1998.txt': 169449, 'w_acad_2007.txt': 189357, 'w_acad_2008.txt': 162620, 'w_acad_2010.txt': 193978, 'w_acad_1999.txt': 162830, 'w_acad_1992.txt': 172977, 'w_acad_1994.txt': 176515, 'w_acad_2003.txt': 169156}
    myList = w_acad.items()

    myList = sorted(myList)
    print(myList)
    x, y = zip(*myList)
    newx = []
    newy = []
    for i in range(len(x)):
        #print(x[i])
        newx.append(x[i].split('_')[2].split('.')[0])
        newy.append(y[i]/w_acad_num_sent[x[i]]*100)
    return sum(y)
    return truncate(sum(newy)/len(newy),2)
    #print(newy)
    # Pure # of Idioms recognized
    for i in newx:
        newnewx.append(int(i))
    width = 506.295
    fig, ax = plt.subplots(1, 1, figsize=set_size(width))
    ax.plot(newnewx, newy)
    plt.title("Idiom Use Rate in the Genre of Academics ")
    plt.xlabel("By Year")
    plt.ylabel("Percentage Rate per Sentence in Corpus")
    plt.xticks(fontsize=10)
    plt.xticks(np.arange(min(newnewx), max(newnewx) + 1, 5.0))
    #plt.plot(newnewx, y)
    plt.style.use('tex')
    plt.style.use('seaborn')
    plt.show()
    fig.savefig('Academic_Rel.jpg', format='jpg', bbox_inches='tight')

    #*************************************************************************
    #WORKS OF SPOKEN PLOTS
    #*************************************************************************
def spok():
    newnewx = []
    w_spok = {'w_spok_1993.txt': 665, 'w_spok_1999.txt': 661, 'w_spok_2010.txt': 651, 'w_spok_1997.txt': 657, 'w_spok_2003.txt': 689, 'w_spok_1990.txt': 620, 'w_spok_1994.txt': 665, 'w_spok_1992.txt': 634, 'w_spok_2001.txt': 656, 'w_spok_1996.txt': 640, 'w_spok_2006.txt': 660, 'w_spok_1998.txt': 684, 'w_spok_1991.txt': 592, 'w_spok_2009.txt': 627, 'w_spok_2000.txt': 687, 'w_spok_1995.txt': 660, 'w_spok_2007.txt': 627, 'w_spok_2012.txt': 535, 'w_spok_2011.txt': 654, 'w_spok_2008.txt': 602, 'w_spok_2004.txt': 680, 'w_spok_2005.txt': 684, 'w_spok_2002.txt': 692}
    w_spok_num_sent = {'w_spok_1993.txt': 270906, 'w_spok_1999.txt': 298834, 'w_spok_2010.txt': 306255, 'w_spok_1997.txt': 265141, 'w_spok_2003.txt': 292990, 'w_spok_1990.txt': 220636, 'w_spok_1994.txt': 279564, 'w_spok_1992.txt': 272125, 'w_spok_2001.txt': 262549, 'w_spok_1996.txt': 264117, 'w_spok_2006.txt': 303105, 'w_spok_1998.txt': 286268, 'w_spok_1991.txt': 211323, 'w_spok_2009.txt': 286841, 'w_spok_2000.txt': 254767, 'w_spok_1995.txt': 289658, 'w_spok_2007.txt': 294499, 'w_spok_2012.txt': 178727, 'w_spok_2011.txt': 311673, 'w_spok_2008.txt': 253472, 'w_spok_2004.txt': 285061, 'w_spok_2005.txt': 294334, 'w_spok_2002.txt': 288137}

    myList = w_spok.items()

    myList = sorted(myList)
    print(myList)
    x, y = zip(*myList)
    newx = []
    newy = []
    for i in range(len(x)):
        #print(x[i])
        newx.append(x[i].split('_')[2].split('.')[0])
        newy.append(y[i]/w_spok_num_sent[x[i]]*100)
    #print(newy)
    # Pure # of Idioms recognized
    return sum(y)
    return truncate(sum(newy)/len(newy),2)

    for i in newx:
        newnewx.append(int(i))
    width = 506.295
    fig, ax = plt.subplots(1, 1, figsize=set_size(width))
    ax.plot(newnewx, newy)
    plt.title("Idiom Use Rate in the Genre of Spoken Word")
    plt.xlabel("By Year")
    plt.ylabel("Percentage Rate per Sentence in Corpus")
    plt.xticks(fontsize=10)
    plt.xticks(np.arange(min(newnewx), max(newnewx) + 1, 5.0))
    # plt.plot(newnewx, y)
    plt.style.use('tex')
    plt.style.use('seaborn')
    plt.show()
    fig.savefig('Spoken_Rel.jpg', format='jpg', bbox_inches='tight')


    #*************************************************************************
    #WORKS OF NEWS PLOTS
    #*************************************************************************
def news():
    newnewx = []
    w_news = {'w_news_1999.txt': 682, 'w_news_2011.txt': 653, 'w_news_2006.txt': 698, 'w_news_2003.txt': 675, 'w_news_2001.txt': 667, 'w_news_2005.txt': 683, 'w_news_2012.txt': 470, 'w_news_2007.txt': 685, 'w_news_2009.txt': 635, 'w_news_2004.txt': 691, 'w_news_1992.txt': 687, 'w_news_1991.txt': 649, 'w_news_1998.txt': 676, 'w_news_2010.txt': 675, 'w_news_2000.txt': 702, 'w_news_1993.txt': 698, 'w_news_2002.txt': 654, 'w_news_2008.txt': 700, 'w_news_1996.txt': 691, 'w_news_1995.txt': 697, 'w_news_1990.txt': 644, 'w_news_1994.txt': 707, 'w_news_1997.txt': 661}
    w_news_num_sent = {'w_news_1999.txt': 222765, 'w_news_2011.txt': 202053, 'w_news_2006.txt': 219825, 'w_news_2003.txt': 221942, 'w_news_2001.txt': 217538, 'w_news_2005.txt': 221828, 'w_news_2012.txt': 109999, 'w_news_2007.txt': 207713, 'w_news_2009.txt': 212028, 'w_news_2004.txt': 224289, 'w_news_1992.txt': 217200, 'w_news_1991.txt': 215417, 'w_news_1998.txt': 223275, 'w_news_2010.txt': 222472, 'w_news_2000.txt': 220521, 'w_news_1993.txt': 222082, 'w_news_2002.txt': 218662, 'w_news_2008.txt': 214623, 'w_news_1996.txt': 226980, 'w_news_1995.txt': 223962, 'w_news_1990.txt': 207190, 'w_news_1994.txt': 220664, 'w_news_1997.txt': 226072}

    myList = w_news.items()

    myList = sorted(myList)
    print(myList)
    x, y = zip(*myList)
    newx = []
    newy = []
    for i in range(len(x)):
        #print(x[i])
        newx.append(x[i].split('_')[2].split('.')[0])
        newy.append(y[i]/w_news_num_sent[x[i]]*100)
    return sum(y)
    return truncate(sum(newy)/len(newy),2)
    #print(newy)
    # Pure # of Idioms recognized

    for i in newx:
        newnewx.append(int(i))
    width = 506.295
    fig, ax = plt.subplots(1, 1, figsize=set_size(width))
    ax.plot(newnewx, newy)
    plt.title("Idiom Use Rate in the Genre of News/Media")
    plt.xlabel("By Year")
    plt.ylabel("Percentage Rate per Sentence in Corpus")
    plt.xticks(fontsize=10)
    plt.xticks(np.arange(min(newnewx), max(newnewx) + 1, 5.0))
    # plt.plot(newnewx, y)
    plt.style.use('tex')
    plt.style.use('seaborn')
    plt.show()
    fig.savefig('News_Rel.jpg', format='jpg', bbox_inches='tight')

def truncate(number, decimals=0):
    """
    Returns a value truncated to a specific number of decimal places.
    """
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer.")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more.")
    elif decimals == 0:
        return math.trunc(number)

    factor = 10.0 ** decimals
    return math.trunc(number * factor) / factor

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i])
def barplot(fict, aca, new, spo):
    # creating data on which bar chart will be plot
    width = 506.295
    fig, ax = plt.subplots(1, 1, figsize=set_size(width))

    x = ["Fiction", "Academic", "News/Media",
         "Spoken"]

    y = [fict, aca, new, spo]


    # making the bar chart on the data
    plt.bar(x, y)

    # calling the function to add value labels
    addlabels(x, y)

    # giving title to the plot
    plt.title("Average Idiom Occurance Across the COCA")

    # giving X and Y labels
    plt.ylabel("Average Percentage Rate per Sentence in Corpus")

    #plt.style.use('tex')
    plt.style.use('seaborn')
    # visualizing the plot
    #plt.show()
    fig.savefig('All_Rel.jpg', format='jpg', bbox_inches='tight')
def main():
    fict = fic()
    new = news()
    aca = acad()
    spo = spok()
    #plots()
    barplot(fict, aca, new, spo)
if __name__ == "__main__":
    main()