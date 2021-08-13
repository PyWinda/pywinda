import matplotlib.pyplot as plt
import numpy as np



def plotg(x,y,**plt_kwargs):

    fig,ax=plt.subplots(figsize=(10,8))
    ax.set_title(plt_kwargs['title'],fontsize=16,fontname='Times New Roman')
    ax.set_xlabel(plt_kwargs['xlabel'],fontname='Times New Roman')
    ax.set_ylabel(plt_kwargs['ylabel'],fontname='Times New Roman')


    textstr=''  #making the text option available for pwploter
    n = 1
    for key,value in plt_kwargs['text'].items():
        text=str(key)+' = '+str(value)+'\n'
        textstr=textstr+text
    textstr=textstr.rstrip("\n")
    props = dict(boxstyle='round', facecolor='gray', alpha=0.6)
    ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=12,verticalalignment='top', bbox=props,fontname='Times New Roman')

    ax.plot(x,y)
    resx=(max(x)-min(x))/len(x)*5
    resy=(max(y)-min(y))/len(y)*5

    ax.set_xticks(np.arange(min(x),max(x)+resx,resx),)
    ax.set_xticklabels(ax.get_xticks(), rotation=60,fontname='Times New Roman')
    ax.set_yticks(np.arange(min(y),max(y)+resy,resy))
    ax.set_xticklabels(ax.get_xticks(),fontname='Times New Roman')
    ax.grid(axis='both')

    return fig,ax
