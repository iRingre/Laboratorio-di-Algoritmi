import matplotlib.pyplot as plt


def _radice(albero):
    """Accetta sia un ABR (con .radice) sia direttamente un Nodo."""
    return getattr(albero, "radice", albero)


def _layout(radice):
    """{nodo: (colonna, profondita')} con visita in-order iterativa."""
    pos = {}
    pila = []
    corr = radice
    d=0
    col=0
    while pila or corr is not None:
        while corr is not None:
            pila.append((corr, d))
            corr = corr.sx
            d += 1
        corr, d = pila.pop()
        pos[corr] = (col, d)
        col += 1
        corr = corr.dx
        d += 1
    return pos

def disegna_matplotlib(albero):
    """Disegna l'albero. Con `percorso` salva il file, altrimenti apre una finestra."""
    import matplotlib
    import matplotlib.pyplot as plt

    pos = _layout(_radice(albero))
    if not pos:
        return
    n = len(pos)
    prof = max(d for _, d in pos.values()) + 1

    fig, ax = plt.subplots(figsize=(max(4, n * 0.55), max(3, prof * 0.9)))
    for x, (c, d) in pos.items():
        for f in (x.sx, x.dx):
            if f is not None:
                cf, df = pos[f]
                ax.plot([c, cf], [-d, -df], color="#888", lw=1.2, zorder=1)
    for x, (c, d) in pos.items():
        ax.scatter(c, -d, s=700, color="#d97a2b" if d == 0 else "#3478c8",
                   edgecolors="white", linewidths=1.5, zorder=2)
        ax.text(c, -d, str(x.chiave), ha="center", va="center",
                color="white", fontsize=9, fontweight="bold", zorder=3)
    ax.set_aspect("equal")
    ax.set_xlim(-1, n)
    ax.set_ylim(-prof, 0.8)
    ax.axis("off")
    plt.show()