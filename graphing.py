import matplotlib.pyplot as plt

def plotWinRate(winrates):
    fig, ax = plt.subplots(figsize=(5, 3), layout='constrained')

    ax.plot(winrates, label ='winrates')

    fig.show()