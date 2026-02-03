import marimo

__generated_with = "0.16.0"
app = marimo.App(width="medium", app_title="Mohr's Circle Demo")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    return mo, np, plt


@app.cell
def _(mo):
    mo.md(
        r"""
    # Crystallography Visualizations

    ## Point Coordinates
    In crystallography, we will want to describe a point inside a unit cell. Recall that a unit cell is characterized by its lattice parameters $a$, $b$, and $c$ to describe the unit length in each dimenision. For describing the location of a point within a unit cell, the **point coordinates** $q$, $r$, and $s$ are used, and correspond to the fraction of the lengths $a$, $b$, and $c$ respectively. This creates the requirement that $0 \leq q,r,s \leq 1$.

    Below is an interactive GUI to explore point coordinates within a cubic unit cell.
    """
    )
    return


@app.cell
def _(mo):
    mn = 0.0
    mx = 1
    # define sliders
    q_button = mo.ui.slider(
        value=0.0, start=mn, stop=mx, step=0.01, label=r"$q$", show_value=True
    )
    r_button = mo.ui.slider(
        value=0, start=mn, stop=mx, step=0.01, label=r"$r$", show_value=True
    )
    s_button = mo.ui.slider(
        value=0, start=mn, stop=mx, step=0.01, label=r"$s$", show_value=True
    )
    # prepend r before the string to tell marimo that it is latex
    # prepend f before the string to tell marimo to access variables. and write in markdown
    mo.vstack([mo.md("Point Coordinates:"), q_button, r_button, s_button])
    return q_button, r_button, s_button


@app.function
def plotCubeBorders(ax):
    # x axes
    ax.plot([0, 1], [0, 0], [0, 0], "k-")
    ax.plot([0, 1], [1, 1], [0, 0], "k-")
    ax.plot([0, 1], [0, 0], [1, 1], "k-")
    ax.plot([0, 1], [1, 1], [1, 1], "k-")
    # y axes
    ax.plot([0, 0], [0, 1], [1, 1], "k-")
    ax.plot([1, 1], [0, 1], [1, 1], "k-")
    ax.plot([0, 0], [0, 1], [0, 0], "k-")
    ax.plot([1, 1], [0, 1], [0, 0], "k-")
    # z axes
    ax.plot([0, 0], [0, 0], [0, 1], "k-")
    ax.plot([1, 1], [0, 0], [0, 1], "k-")
    ax.plot([0, 0], [1, 1], [0, 1], "k-")
    ax.plot([1, 1], [1, 1], [0, 1], "k-")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_zlim(0, 1)
    ax.grid(True)
    ax.dist = 100
    _fs = 30  # font size pt
    _lp = 5  # padding to labels from axes
    ax.set_xlabel("x", fontsize=_fs, labelpad=_lp)
    ax.set_ylabel("y", fontsize=_fs, labelpad=_lp)
    ax.set_zlabel("z", fontsize=_fs, labelpad=_lp)


@app.cell
def _(
    azim_button,
    elev_button,
    plt,
    q_button,
    r_button,
    roll_button,
    s_button,
):
    # get point location
    q = q_button.value
    r = r_button.value
    s = s_button.value
    # get camera angles
    elev = elev_button.value
    azim = azim_button.value
    roll = roll_button.value
    # make 3d scatter plot
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(projection="3d")
    ax.view_init(elev, azim, roll)
    # ax.scatter(q, r, s, marker="o", s=100, c="red")  # point coordinate
    # now add lines at edges of cube
    plotCubeBorders(ax)
    ax.set_aspect("auto")
    ax.scatter(q, r, s, marker="o", s=100, c="red")  # point coordinate
    return


@app.cell
def _(mo):
    # change orientation of plot
    _mn = 0
    _mx = 360
    # define sliders
    elev_button = mo.ui.slider(
        value=30, start=_mn, stop=_mx, label="elevation angle", show_value=True
    )
    azim_button = mo.ui.slider(
        value=70, start=_mn, stop=_mx, label="azimuthal angle", show_value=True
    )
    roll_button = mo.ui.slider(
        value=0, start=_mn, stop=_mx, label="roll angle", show_value=True
    )
    # prepend r before the string to tell marimo that it is latex
    # prepend f before the string to tell marimo to access variables. and write in markdown
    # mo.hstack([elev_button, azim_button, roll_button])
    mo.vstack([mo.md("Camera Controls:"), elev_button, azim_button])
    return azim_button, elev_button, roll_button


@app.cell
def _():
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ---
    ## Crystallographic Direction Vectors
    The **crystallographic direction** is characterized by using a vector [$u$ $v$ $w$]. Note the notation which uses square brackets and no separating punctuation.   
    The indices $u$, $v$, and $w$ correspond with the directions of the lattice parameters $a$, $b$, and $c$.   
    The values of $u$, $v$, and $w$ are not fractions (like in the point coordinates), but rather are integers and also least common multiples.   
    Negative values are denoted by an overbar For example: $\bar{1}$ instead of $-1$.
    """
    )
    return


@app.cell
def _(mo):
    # mn = 0.0
    # mx = 1
    vmx = 5
    # define sliders
    u_button = mo.ui.slider(
        value=0, start=-vmx, stop=vmx, step=1, label=r"$u$", show_value=True
    )
    v_button = mo.ui.slider(
        value=0, start=-vmx, stop=vmx, step=1, label=r"$v$", show_value=True
    )
    w_button = mo.ui.slider(
        value=1, start=-vmx, stop=vmx, step=1, label=r"$w$", show_value=True
    )
    # prepend r before the string to tell marimo that it is latex
    # prepend f before the string to tell marimo to access variables. and write in markdown
    return u_button, v_button, w_button


@app.cell
def _(mo, u_button, v_button, w_button):
    def add_overline(text):
        """Adds an overline to the input text using Unicode combining characters."""
        return "".join([char + "\u0305" for char in text])


    def crystalVectorNotation(u):
        ustr = str(u)
        if u < 0:
            ustr = str(abs(u))
            return add_overline(ustr)
        else:
            ustr = str(u)
            return ustr


    _ustr = crystalVectorNotation(u_button.value)
    _vstr = crystalVectorNotation(v_button.value)
    _wstr = crystalVectorNotation(w_button.value)
    mo.vstack(
        [
            mo.md("Direction Vector Components:"),
            mo.hstack(
                [u_button, mo.md(f"$u$-component notation: {_ustr}")],
                justify="start",
            ),
            mo.hstack(
                [v_button, mo.md(f"$v$-component notation: {_vstr}")],
                justify="start",
            ),
            mo.hstack(
                [w_button, mo.md(f"$w$-component notation: {_wstr}")],
                justify="start",
            ),
            mo.md(
                f"Full vector is: [ {_ustr} {_vstr} {_wstr} ] $^*$Note: this expression may not be properly simplified according to convention."
            ),
        ]
    )
    return


@app.cell
def _(
    azim2_button,
    elev2_button,
    np,
    plt,
    roll2_button,
    u_button,
    v_button,
    w_button,
):
    # get point location
    u = u_button.value  # this is the unnormalized value
    v = v_button.value  # unnormalized value
    w = w_button.value  # unnormalized value
    # normalize the u, v, w values
    _mxu = max(np.abs([u, v, w]))
    _up = u / _mxu
    _vp = v / _mxu
    _wp = w / _mxu
    # get camera angles
    elev2 = elev2_button.value
    azim2 = azim2_button.value
    roll2 = roll2_button.value
    # make 3d scatter plot
    fig2 = plt.figure(figsize=(8, 8))
    ax2 = fig2.add_subplot(projection="3d")
    ax2.view_init(elev2, azim2, roll2)
    # ax.scatter(q, r, s, marker="o", s=100, c="red")  # point coordinate
    # now add lines at edges of cube
    plotCubeBorders(ax2)
    x0 = 0
    y0 = 0
    z0 = 0
    # shift location if the vector is pointing in the negative direction
    if any(n < 0 for n in [u, v, w]):
        x0 = 1.0 if _up < 0 else 0.0
        y0 = 1.0 if _vp < 0 else 0.0
        z0 = 1.0 if _wp < 0 else 0.0
    ax2.quiver(
        x0,
        y0,
        z0,
        _up,
        _vp,
        _wp,
        arrow_length_ratio=0.1,
        color="maroon",
        linewidth=5,
    )
    return


@app.cell
def _(mo):
    # change orientation of plot
    _mn = 0
    _mx = 360
    # define sliders
    elev2_button = mo.ui.slider(
        value=30, start=_mn, stop=_mx, label="elevation angle", show_value=True
    )
    azim2_button = mo.ui.slider(
        value=70, start=_mn, stop=_mx, label="azimuthal angle", show_value=True
    )
    roll2_button = mo.ui.slider(
        value=0, start=_mn, stop=_mx, label="roll angle", show_value=True
    )
    # prepend r before the string to tell marimo that it is latex
    # prepend f before the string to tell marimo to access variables. and write in markdown
    # mo.hstack([elev_button, azim_button, roll_button])
    mo.vstack([mo.md("Camera Controls:"), elev2_button, azim2_button])
    return azim2_button, elev2_button, roll2_button


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
