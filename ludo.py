

import turtle as t

t.speed(0)
# === Scale Factor ===
S = 1.5   # change this to make board bigger/smaller

# === Sizes ===
outer = int(200 * S)
inner = int(40 * S)
pawn_r = int(20 * S)
cell = int((outer - inner) / 6)   # track cell size

# === Outer boundary ===
t.penup()
t.goto(-outer, outer)
t.pendown()
for i in range(4):
    t.forward(outer*2)
    t.right(90)

# === Red Home (Top-Left) ===
t.penup()
t.goto(-outer, outer)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.goto(-inner, outer)
t.goto(-inner, inner)
t.goto(-outer, inner)
t.goto(-outer, outer)
t.end_fill()

# === Green Home (Top-Right) ===
t.penup()
t.goto(inner, outer)
t.pendown()
t.fillcolor("green")
t.begin_fill()
t.goto(outer, outer)
t.goto(outer, inner)
t.goto(inner, inner)
t.goto(inner, outer)
t.end_fill()

# === Blue Home (Bottom-Left) ===
t.penup()
t.goto(-outer, -inner)
t.pendown()
t.fillcolor("blue")
t.begin_fill()
t.goto(-inner, -inner)
t.goto(-inner, -outer)
t.goto(-outer, -outer)
t.goto(-outer, -inner)
t.end_fill()

# === Yellow Home (Bottom-Right) ===
t.penup()
t.goto(inner, -inner)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.goto(outer, -inner)
t.goto(outer, -outer)
t.goto(inner, -outer)
t.goto(inner, -inner)
t.end_fill()
t.penup()

# === Pawn Circles ===
def draw_pawns(positions):
    for pos in positions:
        t.goto(pos)
        t.pendown()
        t.fillcolor("white")
        t.begin_fill()
        t.circle(pawn_r)
        t.end_fill()
        t.penup()

# Red pawns
draw_pawns([(-outer+50*S, outer-50*S), (-outer+110*S, outer-50*S),
            (-outer+50*S, outer-110*S), (-outer+110*S, outer-110*S)])

# Green pawns
draw_pawns([(outer-110*S, outer-50*S), (outer-50*S, outer-50*S),
            (outer-110*S, outer-110*S), (outer-50*S, outer-110*S)])

# Blue pawns
draw_pawns([(-outer+50*S, -outer+110*S), (-outer+110*S, -outer+110*S),
            (-outer+50*S, -outer+50*S), (-outer+110*S, -outer+50*S)])

# Yellow pawns
draw_pawns([(outer-110*S, -outer+110*S), (outer-50*S, -outer+110*S),
            (outer-110*S, -outer+50*S), (outer-50*S, -outer+50*S)])


# === Center Diamond (4 Triangles) ===
center = (0,0)

# Red Triangle (Top)
t.penup()
t.goto(center)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.goto(-inner, inner)
t.goto(inner, inner)
t.goto(center)
t.end_fill()

# Green Triangle (Right)
t.fillcolor("green")
t.begin_fill()
t.goto(center)
t.goto(inner, inner)
t.goto(inner, -inner)
t.goto(center)
t.end_fill()

# Yellow Triangle (Bottom)
t.fillcolor("yellow")
t.begin_fill()
t.goto(center)
t.goto(inner, -inner)
t.goto(-inner, -inner)
t.goto(center)
t.end_fill()

# Blue Triangle (Left)
t.fillcolor("blue")
t.begin_fill()
t.goto(center)
t.goto(-inner, -inner)
t.goto(-inner, inner)
t.goto(center)
t.end_fill()


# === 3×6 Path Boxes ===
def draw_track(x1, y1, w, h, rows, cols, color=None, fill_cols=None, fill_rows=None, fill_cells=None, skip_cells=None):
    """
    Draw a grid of rows x cols starting from (x1,y1) downward/right.
    fill_cols: list of column indices to fill entirely
    fill_rows: list of row indices to fill entirely
    fill_cells: list of (r,c) tuples to fill individual boxes
    skip_cells: list of (r,c) tuples to skip filling
    """
    fill_cols = fill_cols or []
    fill_rows = fill_rows or []
    fill_cells = fill_cells or []
    skip_cells = skip_cells or []

    box_w = w // cols
    box_h = h // rows

    for r in range(rows):
        for c in range(cols):
            t.penup()
            t.goto(x1 + c*box_w, y1 - r*box_h)
            t.pendown()

            fill = False
            if color:
                if c in fill_cols or r in fill_rows or (r,c) in fill_cells:
                    fill = True
                if (r,c) in skip_cells:
                    fill = False
                if fill:
                    t.fillcolor(color)
                    t.begin_fill()

            for _ in range(4):
                t.forward(box_w if _ % 2 == 0 else box_h)
                t.right(90)

            if fill:
                t.end_fill()


# Top region (Red & Green)
draw_track(-inner, outer, 2*inner, outer-inner, 6, 3, color="red",
           fill_cols=[1], skip_cells=[(0,1)], fill_cells=[(1,0)])

# Bottom region (Blue & Yellow)
draw_track(-inner, -inner, 2*inner, outer-inner, 6, 3, color="yellow",
           fill_cols=[1], skip_cells=[(5,1)], fill_cells=[(4,2)])

# Left region (Red & Blue)
draw_track(-outer, inner, outer-inner, 2*inner, 3, 6, color="blue",
           fill_rows=[1], skip_cells=[(1,0)], fill_cells=[(2,1)])

# Right region (Green & Yellow)
draw_track(inner, inner, outer-inner, 2*inner, 3, 6, color="green",
           fill_rows=[1], skip_cells=[(1,5)], fill_cells=[(0,4)])

t.hideturtle()
t.done()
