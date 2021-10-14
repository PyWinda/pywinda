import matplotlib.pyplot as plt
import numpy as np
import matplotlib
# Say, "the default sans-serif font is COMIC SANS"
matplotlib.rcParams['font.sans-serif'] = "Times New Roman"
# Then, "ALWAYS use sans-serif fonts"
matplotlib.rcParams['font.family'] = "sans-serif"
# Pywinda color codes:

pgreen1='#009C86'
pgreen2='#0397A1'
pblue='#05354B'
pred='#96394E'
ppink='#ECA48E'
pyellow='#ECD384'


def plot(x,y,**plt_kwargs):
    fig,ax=plt.subplots(figsize=(10,8))

    if 'title' in plt_kwargs:
        ax.set_title(plt_kwargs['title'], fontsize=16, fontname='Times New Roman')
    if 'xlabel' in plt_kwargs:
        ax.set_xlabel(plt_kwargs['xlabel'], fontname='Times New Roman')
    if 'ylabel' in plt_kwargs:
        ax.set_ylabel(plt_kwargs['ylabel'], fontname='Times New Roman')
    if 'text' in plt_kwargs:
        textstr=''  #making the text option available for pwploter
        for key, value in plt_kwargs['text'].items():
            text = str(key)+' = '+str(value)+'\n'
            textstr=textstr+text
        textstr=textstr.rstrip("\n")
        props = dict(boxstyle='round', facecolor=pgreen1, alpha=0.6)
        ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=12,verticalalignment='top', bbox=props,fontname='Times New Roman')

    ax.plot(x,y)
    resx=(max(x)-min(x))/len(x)*5
    resy=(max(y)-min(y))/len(y)*5

    xticks=[]
    ytick=[]

    for i in np.arange(min(x),max(x)+resx,resx):
        xticks.append(round(i,6)) #create the xticks with 6 decimal places
    for i in np.arange(min(y),max(y)+resy,resy):
        ytick.append(round(i,6))  #create the ytick with 6 decimal places

    ax.set_xticks(xticks)
    ax.set_xticklabels(ax.get_xticks(), rotation=60,fontname='Times New Roman')

    ax.set_yticks(ytick)
    ax.set_yticklabels(ax.get_yticks(),fontname='Times New Roman')
    ax.grid(axis='both')

    return fig,ax


def hist(x,bins,density=True,**plt_kwargs):
    fig,ax=plt.subplots(figsize=(10,8))

    if 'title' in plt_kwargs:
        ax.set_title(plt_kwargs['title'], fontsize=16, fontname='Times New Roman')
    if 'xlabel' in plt_kwargs:
        ax.set_xlabel(plt_kwargs['xlabel'], fontname='Times New Roman')
    if 'ylabel' in plt_kwargs:
        ax.set_ylabel(plt_kwargs['ylabel'], fontname='Times New Roman')
    if 'text' in plt_kwargs:
        textstr=''  #making the text option available for pwploter
        for key, value in plt_kwargs['text'].items():
            text = str(key)+' = '+str(value)+'\n'
            textstr=textstr+text
        textstr=textstr.rstrip("\n")
        props = dict(boxstyle='round', facecolor=pgreen1, alpha=0.6,edgecolor=pgreen1)
        ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=12,verticalalignment='top', bbox=props,fontname='Times New Roman')

    counts,bins2,ignored=ax.hist(x,bins,density=density,edgecolor='white')
    return fig,ax,counts,bins2
