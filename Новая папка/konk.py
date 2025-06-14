from sketchpy import canvas

pen = canvas.sketch(x_offset=500, y_offset=350)
pen.draw_fn("reds", co=(210,0,0), mode=0)
pen.draw_fn("shadows1", co=(153,0,0), mode=0)
pen.draw_fn("shadows2", co=(153,0,0), mode=0)
pen.draw_fn("shadows3", co=(153,0,0), mode=0)
pen.draw_fn("shadows4", co=(153,0,0), mode=0)
pen.draw_fn("reds", co=(0,0,0), mode=1, thickness=3)
pen.draw_fn("face1", co=(255,255,100), mode=0)
pen.draw_fn("face1", co=(0,0,0), mode=1, thickness=2)
pen.draw_fn("eyes", co=(0,255,255), mode=0)
pen.draw_fn("eyes", co=(0,0,0), mode=1, thickness=2)
pen.draw_fn("mouse1", co=(0,0,0), mode=1, thickness=1)
pen.draw_fn("l_yel1", co=(255,178,102), mode=0)
pen.draw_fn("l_yel1", co=(0,0,0), mode=1, thickness=3)
pen.draw_fn("r_yel1", co=(255,178,102), mode=0)
pen.draw_fn("r_yel1", co=(0,0,0), mode=1, thickness=3)
pen.draw_fn("blast2", co=(153,153,255), mode=0)
pen.draw_fn("blacks", co=(0,0,0), mode=1, thickness=3)
pen.draw_fn("blacks2", co=(0,0,0), mode=1, thickness=4)
pen.draw_fn("blacks3", co=(0,0,0), mode=1, thickness=3)
pen.draw_fn("blast1", co=(0,255,255), mode=0)
pen.draw_fn("blast1", co=(0,0,0), mode=1, thickness=2)
pen.draw_fn("blast2", co=(0,0,0), mode=1, thickness=3, retain=True)