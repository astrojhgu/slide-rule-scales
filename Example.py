from SlideRuleScale import SlideRuleScale
import os

os.chdir("./Example/")

Example = SlideRuleScale("./specs/scale/")
Example.set_scale_type("ca", positioning_factor=0.01)
Example.draw_straight("./straight.svg", "./specs/draw_straight.csv")
