# -*- coding: utf-8 -*-

# python imports
from math import degrees

# pyfuzzy imports
from fuzzy.storage.fcl.Reader import Reader


class FuzzyController:

    def __init__(self, fcl_path):
        self.system = Reader().load_from_file(fcl_path)


    def _make_input(self, world):
        return dict(
            cp = world.x,
            cv = world.v,
            pa = degrees(world.theta),
            pv = degrees(world.omega)
        )


    def _make_output(self):
        return dict(
            force = 0.
        )


    def decide(self, world):
        print("new cycle")
        inp_doc = self._make_input(world)
        pv = inp_doc['pv']
        pa = inp_doc['pa']
        cv = inp_doc['cv']
        if pa < 0:
            pa += 360
        if pv > 200:
            pv = 199
        if pv < -200:
            pv = -199

        output = self._make_output()
        self.system.calculate(self._make_input(world), output)
        print("output : ", output)

        return self.calc_center_of_mass(pv, pa, cv)


        # return output['force']


    def cw_fast(self, x):
        if -100 > x >= -200:
            return float(-x - 100) / 100

        else:
            return 0

    def cw_slow(self, x):
        if -100 > x >= -200:
            return float(x + 200)/ 100

        if 0 > x >= -100:
            return float(-x) / 100

        else:
            return 0

    def stop(self, x):
        if 0 > x >= -100:
            return float(x + 100)/ 100

        elif 100 > x >= 0:

            return float(-x + 100) / 100

        else:
            return 0

    def ccw_slow(self, x):

        if 100 > x >= 0:
            return float(x) / 100

        if 200 >= x >= 100:
            return float(-x + 200) / 100

        else:
            return 0

    def ccw_fast(self, x):

        if 200 >= x >= 100:
            return float(x - 100) / 100

        else:
            return 0

    def up_more_right(self, x):

        if 0 < x <= 30 :
            return float(x) / 30

        elif 30 < x <= 60:
            return float(-x + 60) / 30

        else:
            return 0

    def up_right(self, x):

        if 30 < x <= 60 :
            return float(x  - 30) / 30

        elif 60 < x <= 90:
            return float(-x + 90) / 30

        else:
            return 0

    def up(self, x):

        if 60 < x <= 90 :
            return float(x  - 60) / 30

        elif 90 < x <= 120:
            return float(-x + 120) / 30

        else:
            return 0

    def up_left(self, x):

        if 90 < x <= 120 :
            return float(x  - 90)/ 30

        elif 120 < x <= 150:
            return float(-x + 150) / 30

        else:
            return 0

    def up_more_left(self, x):

        if 120 < x <= 150 :
            return float(x - 120)/ 30

        elif 150 < x <= 180:
            return float(-x + 180) / 30

        else:
            return 0

    def down_more_left(self, x):

        if 180 < x <= 210 :
            return float(x - 180)/ 30

        elif 210 < x <= 240:
            return float(-x + 240) / 30

        else:
            return 0


    def down_left(self, x):

        if 210 < x <= 240 :
            return float(x - 210)/ 30

        elif 240 < x <= 270:
            return float(-x + 270) / 30

        else:
            return 0

    def down(self, x):

        if 240 < x <= 270 :
            return float(x - 240)/ 30

        elif 270 < x <= 300:
            return float(-x + 300) / 30

        else:
            return 0

    def down_right(self, x):

        if 270 < x <= 300 :
            return float(x - 270)/ 30

        elif 300 < x <= 330:
            return float(-x + 330) / 30

        else:
            return 0

    def down_more_right(self, x):

        if 300 < x <= 330 :
            return float(x - 300)/ 30

        elif 330 < x <= 360:
            return float(-x + 360) / 30

        else:
            return 0

    def left_far(self, x):
        if -10 <= x < -5:
            return float(-x + 5) / 5
        else:
            return 0
    def left_near(self, x):
        if -10 <= x < -2.5:
            return float(x + 10) / 7.5
        elif -2.5 <= x < 0:
            return float(-x) / 2.5
        else:
            return 0

    def cp_stop(self, x):
        if -2.5 <= x < 0:
            return float(x + 2.5) / 2.5
        elif 0 <= x < 2.5:
            return float(-x + 2.5) / 2.5
        else:
            return 0

    def right_near(self, x):
        if 0 <= x < 2.5:
            return float(x) / 2.5
        elif 2.5 <= x < 10:
            return float(-x + 10) / 7.5
        else:
            return 0

    def right_far(self, x):
        if 5 <= x < 10:
            return float(x - 5) / 5
        else:
            return 0

    def cv_left_fast(self, x):
        if -5 <= x < -2.5:
            return float(-x + 2.5) / 2.5
        else:
            return 0

    def cv_left_slow(self, x):
        if -5 <= x < -1:
            return float(x + 5) / 4
        elif -1 <= x < 0:
            return float(-x) / 1
        else:
            return 0

    def cv_stop(self, x):
        if -1 <= x < 0:
            return float(x + 1) / 1
        elif 0 <= x < 1:
            return float(-x + 1) / 1
        else:
            return 0

    def cv_right_slow(self, x):
        if 0 <= x < 1:
            return float(x) / 1
        elif 1 <= x < 5:
            return float(-x + 5) / 4
        else:
            return 0

    def cv_right_fast(self, x):
        if 2.5 <= x < 5:
            return float(x - 2.5) / 2.5
        else:
            return 0

    def right_fast_calc(self, pv, pa, cv):
        pa_dict = {"up_more_right":False, "up_right":False, "up":False, "up_left":False, "up_more_left":False,
                   "down_more_left":False, "down_left":False, "down":False, "down_right":False, "down_more_right":False}

        pv_dict = {"cw_fast": False, "cw_slow": False, "stop": False, "ccw_slow": False, "ccw_fast": False}

        cv_dict = {"left_fast": False, "left_slow": False, "stop": False, "right_slow": False, "right_fast": False}

        cv_dict["left_fast"] = self.cv_left_fast(cv)
        cv_dict["left_slow"] = self.cv_left_slow(cv)
        cv_dict["stop"] = self.cv_stop(cv)
        cv_dict["right_slow"] = self.cv_right_slow(cv)
        cv_dict["right_fast"] = self.cv_right_fast(cv)

        pa_dict["up_more_right"] = self.up_more_right(pa)
        pa_dict["up_right"] = self.up_right(pa)
        pa_dict["up"] = self.up(pa)
        pa_dict["up_left"] = self.up_left(pa)
        pa_dict["up_more_left"] = self.up_more_left(pa)
        pa_dict["down_more_right"] = self.down_more_right(pa)
        pa_dict["down_right"] = self.down_right(pa)
        pa_dict["down"] = self.down(pa)
        pa_dict["down_more_left"] = self.down_more_left(pa)
        pa_dict["down_left"] = self.down_left(pa)

        pv_dict["ccw_slow"] = self.ccw_slow(pv)
        pv_dict["ccw_fast"] = self.ccw_fast(pv)
        pv_dict["cw_slow"] = self.cw_slow(pv)
        pv_dict["cw_fast"] = self.cw_fast(pv)
        pv_dict["stop"] = self.stop(pv)

        cv_dict["left_fast"] = self.cv_left_fast(cv)
        cv_dict["left_slow"] = self.cv_left_slow(cv)
        cv_dict["stop"] = self.cv_stop(cv)
        cv_dict["right_slow"] = self.cv_right_slow(cv)
        cv_dict["right_fast"] = self.cv_right_fast(cv)

        print("pa dict : ", pa_dict)
        print("pv_dict :", pv_dict)
        print("cv_dict : ", cv_dict)

        rule_1 = max(min(pa_dict["up_more_right"], pv_dict["ccw_slow"]), min(pa_dict["up_more_right"], 1 - cv_dict["right_fast"]))
        rule_2 = max(min(pa_dict["up_more_right"], pv_dict["cw_slow"]), min(pa_dict["up_more_right"], 1 - cv_dict["right_fast"]))
        rule_6 = max(min(pa_dict["up_more_right"], pv_dict["cw_fast"]), min(pa_dict["up_more_right"], 1 - cv_dict["right_fast"]))
        rule_9 = max(min(pa_dict["down_more_right"], pv_dict["ccw_slow"]), min(pa_dict["down_more_right"], 1 - cv_dict["right_fast"]))
        rule_17 = max(min(pa_dict["down_right"], pv_dict["ccw_slow"]), min(pa_dict["down_right"], 1 - cv_dict["right_fast"]))
        rule_18 = max(min(pa_dict["down_right"], pv_dict["cw_slow"]), min(pa_dict["down_right"], 1 - cv_dict["right_fast"]))
        rule_26 = max(min(pa_dict["up_right"], pv_dict["cw_slow"]), min(pa_dict["up_right"], 1 - cv_dict["right_fast"]))
        rule_27 = max(min(pa_dict["up_right"], pv_dict["stop"]) , min(pa_dict["up_right"], 1 - cv_dict["right_fast"]))
        rule_32 = min(pa_dict["up_right"], pv_dict["cw_fast"])
        rule_33 = max(min(pa_dict["up_left"], pv_dict["cw_fast"]), min(pa_dict["up_left"], cv_dict["left_fast"]))
        rule_35 = min(pa_dict["down"], pv_dict["stop"] , min(pa_dict["down"], 1 - cv_dict["right_fast"]))
        rule_41 = max(min(pa_dict["up"], pv_dict["cw_fast"]), min(pa_dict["up"], cv_dict["left_fast"]))

        # rule_43 = max(pa_dict["down_more_right"], pa_dict["down_right"]), max(pv_dict[""], pv_dict[""])

        values = [rule_1, rule_6, rule_2, rule_9, rule_17, rule_26, rule_18, rule_27, rule_32, rule_33, rule_35, rule_41]
        return max(values)

    def right_slow_calc(self, pv, pa, cv):
        pa_dict = {"up_more_right": False, "up_right": False, "up": False, "up_left": False, "up_more_left": False,
                   "down_more_left": False, "down_left": False, "down": False, "down_right": False,
                   "down_more_right": False}

        pv_dict = {"cw_fast": False, "cw_slow": False, "stop": False, "ccw_slow": False, "ccw_fast": False}

        cv_dict = {"left_fast": False, "left_slow": False, "stop": False, "right_slow": False, "right_fast": False}

        cv_dict["left_fast"] = self.cv_left_fast(cv)
        cv_dict["left_slow"] = self.cv_left_slow(cv)
        cv_dict["stop"] = self.cv_stop(cv)
        cv_dict["right_slow"] = self.cv_right_slow(cv)
        cv_dict["right_fast"] = self.cv_right_fast(cv)

        pa_dict["up_more_right"] = self.up_more_right(pa)
        pa_dict["up_right"] = self.up_right(pa)
        pa_dict["up"] = self.up(pa)
        pa_dict["up_left"] = self.up_left(pa)
        pa_dict["up_more_left"] = self.up_more_left(pa)
        pa_dict["down_more_right"] = self.down_more_right(pa)
        pa_dict["down_right"] = self.down_right(pa)
        pa_dict["down"] = self.down(pa)
        pa_dict["down_more_left"] = self.down_more_left(pa)
        pa_dict["down_left"] = self.down_left(pa)

        pv_dict["ccw_slow"] = self.ccw_slow(pv)
        pv_dict["ccw_fast"] = self.ccw_fast(pv)
        pv_dict["cw_slow"] = self.cw_slow(pv)
        pv_dict["cw_fast"] = self.cw_fast(pv)
        pv_dict["stop"] = self.stop(pv)

        rule_5 = max(min(pa_dict["up_more_right"], pv_dict["ccw_fast"]),
                     min(pa_dict["up_more_right"], cv_dict["right_fast"]))
        rule_13 = max(min(pa_dict["down_more_right"], pv_dict["ccw_fast"]), min(pa_dict["down_more_right"], cv_dict["right_fast"]))
        rule_22 = max(min(pa_dict["down_right"], pv_dict["cw_fast"]), min( pa_dict["down_right"], cv_dict["right_fast"]))
        rule_25 = max(min(pa_dict["up_right"], pv_dict["ccw_slow"]), min(pa_dict["up_right"], cv_dict["right_fast"]))
        rule_40 = max(min(pa_dict["up"], pv_dict["cw_slow"]) , min(pa_dict["up"], cv_dict["right_fast"]))

        values = [rule_5, rule_13, rule_22, rule_25, rule_40]
        return max(values)

    def left_fast_calc(self, pv, pa, cv):
        pa_dict = {"up_more_right":False, "up_right":False, "up":False, "up_left":False, "up_more_left":False,
                   "down_more_left":False, "down_left":False, "down":False, "down_right":False, "down_more_right":False}

        pv_dict = {"cw_fast": False, "cw_slow": False, "stop": False, "ccw_slow": False, "ccw_fast": False}

        cv_dict = {"left_fast": False, "left_slow": False, "stop": False, "right_slow": False, "right_fast": False}

        cv_dict["left_fast"] = self.cv_left_fast(cv)
        cv_dict["left_slow"] = self.cv_left_slow(cv)
        cv_dict["stop"] = self.cv_stop(cv)
        cv_dict["right_slow"] = self.cv_right_slow(cv)
        cv_dict["right_fast"] = self.cv_right_fast(cv)

        pa_dict["up_more_right"] = self.up_more_right(pa)
        pa_dict["up_right"] = self.up_right(pa)
        pa_dict["up"] = self.up(pa)
        pa_dict["up_left"] = self.up_left(pa)
        pa_dict["up_more_left"] = self.up_more_left(pa)
        pa_dict["down_more_right"] = self.down_more_right(pa)
        pa_dict["down_right"] = self.down_right(pa)
        pa_dict["down"] = self.down(pa)
        pa_dict["down_more_left"] = self.down_more_left(pa)
        pa_dict["down_left"] = self.down_left(pa)

        pv_dict["ccw_slow"] = self.ccw_slow(pv)
        pv_dict["ccw_fast"] = self.ccw_fast(pv)
        pv_dict["cw_slow"] = self.cw_slow(pv)
        pv_dict["cw_fast"] = self.cw_fast(pv)
        pv_dict["stop"] = self.stop(pv)


        rule_3 = max(min(pa_dict["up_more_left"], pv_dict["cw_slow"]), min(pa_dict["up_more_left"], 1 - cv_dict["left_fast"]))
        rule_4 = max(min(pa_dict["up_more_left"], pv_dict["ccw_slow"]), min(pa_dict["up_more_left"], 1 -  cv_dict["left_fast"]))
        rule_8 = max(min(pa_dict["up_more_left"], pv_dict["ccw_fast"]), min(pa_dict["up_more_left"], 1 -  cv_dict["left_fast"]))
        rule_11 = max(min(pa_dict["down_more_left"], pv_dict["cw_slow"]), min(pa_dict["down_more_left"], 1 -  cv_dict["left_fast"]))
        rule_19 = max(min(pa_dict["down_left"], pv_dict["cw_slow"]), min(pa_dict["down_left"], 1 -  cv_dict["left_fast"]))
        rule_20 = max(min(pa_dict["down_left"], pv_dict["ccw_slow"]), min(pa_dict["down_left"], 1 -  cv_dict["left_fast"]))
        rule_29 = max(min(pa_dict["up_left"], pv_dict["ccw_slow"]), min(pa_dict["up_left"], 1 -  cv_dict["left_fast"]))
        rule_30 = max(min(pa_dict["up_left"], pv_dict["stop"]), min(pa_dict["up_left"], 1 -  cv_dict["left_fast"]))
        rule_31 = min(pa_dict["up_right"], pv_dict["ccw_fast"])
        rule_34 = max(min(pa_dict["up_left"], pv_dict["ccw_fast"]), min(pa_dict["up_left"], cv_dict["right_fast"]))
        rule_39 = max(min(pa_dict["up"], pv_dict["ccw_fast"]), min(pa_dict["up"], cv_dict["right_fast"]))

        values = [rule_3, rule_4, rule_8, rule_11, rule_19, rule_20, rule_29, rule_30, rule_31, rule_34, rule_39]

        return max(values)

    def left_slow_calc(self, pv, pa, cv):
        pa_dict = {"up_more_right":False, "up_right":False, "up":False, "up_left":False, "up_more_left":False,
                   "down_more_left":False, "down_left":False, "down":False, "down_right":False, "down_more_right":False}

        pv_dict = {"cw_fast": False, "cw_slow": False, "stop": False, "ccw_slow": False, "ccw_fast": False}

        cv_dict = {"left_fast": False, "left_slow": False, "stop": False, "right_slow": False, "right_fast": False}

        cv_dict["left_fast"] = self.cv_left_fast(cv)
        cv_dict["left_slow"] = self.cv_left_slow(cv)
        cv_dict["stop"] = self.cv_stop(cv)
        cv_dict["right_slow"] = self.cv_right_slow(cv)
        cv_dict["right_fast"] = self.cv_right_fast(cv)

        pa_dict["up_more_right"] = self.up_more_right(pa)
        pa_dict["up_right"] = self.up_right(pa)
        pa_dict["up"] = self.up(pa)
        pa_dict["up_left"] = self.up_left(pa)
        pa_dict["up_more_left"] = self.up_more_left(pa)
        pa_dict["down_more_right"] = self.down_more_right(pa)
        pa_dict["down_right"] = self.down_right(pa)
        pa_dict["down"] = self.down(pa)
        pa_dict["down_more_left"] = self.down_more_left(pa)
        pa_dict["down_left"] = self.down_left(pa)

        pv_dict["ccw_slow"] = self.ccw_slow(pv)
        pv_dict["ccw_fast"] = self.ccw_fast(pv)
        pv_dict["cw_slow"] = self.cw_slow(pv)
        pv_dict["cw_fast"] = self.cw_fast(pv)
        pv_dict["stop"] = self.stop(pv)

        rule_7 = max(min(pa_dict["up_more_left"], pv_dict["cw_fast"]),
                     min(pa_dict["up_more_left"], cv_dict["left_fast"]))
        rule_15 = max(min(pa_dict["down_more_left"], pv_dict["cw_fast"]),  min(pa_dict["down_more_left"], cv_dict["left_fast"]))
        rule_24 = max(min(pa_dict["down_left"], pv_dict["ccw_fast"]), min(pa_dict["down_left"], cv_dict["left_fast"]))
        rule_28 = max(min(pa_dict["up_left"], pv_dict["cw_slow"]), min(pa_dict["up_left"], cv_dict["left_fast"]))
        rule_38 = max(min(pa_dict["up"], pv_dict["ccw_slow"]), min(pa_dict["up"], cv_dict["left_fast"]))

        values = [rule_7, rule_15,  rule_24, rule_38, rule_28]

        return max(values)

    def f_stop_calc(self, pv, pa, cv):
        pa_dict = {"up_more_right":False, "up_right":False, "up":False, "up_left":False, "up_more_left":False,
                   "down_more_left":False, "down_left":False, "down":False, "down_right":False, "down_more_right":False}

        pv_dict = {"cw_fast": False, "cw_slow": False, "stop": False, "ccw_slow": False, "ccw_fast": False}

        cv_dict = {"left_fast": False, "left_slow": False, "stop": False, "right_slow": False, "right_fast": False}

        cv_dict["left_fast"] = self.cv_left_fast(cv)
        cv_dict["left_slow"] = self.cv_left_slow(cv)
        cv_dict["stop"] = self.cv_stop(cv)
        cv_dict["right_slow"] = self.cv_right_slow(cv)
        cv_dict["right_fast"] = self.cv_right_fast(cv)

        pa_dict["up_more_right"] = self.up_more_right(pa)
        pa_dict["up_right"] = self.up_right(pa)
        pa_dict["up"] = self.up(pa)
        pa_dict["up_left"] = self.up_left(pa)
        pa_dict["up_more_left"] = self.up_more_left(pa)
        pa_dict["down_more_right"] = self.down_more_right(pa)
        pa_dict["down_right"] = self.down_right(pa)
        pa_dict["down"] = self.down(pa)
        pa_dict["down_more_left"] = self.down_more_left(pa)
        pa_dict["down_left"] = self.down_left(pa)

        pv_dict["ccw_slow"] = self.ccw_slow(pv)
        pv_dict["ccw_fast"] = self.ccw_fast(pv)
        pv_dict["cw_slow"] = self.cw_slow(pv)
        pv_dict["cw_fast"] = self.cw_fast(pv)
        pv_dict["stop"] = self.stop(pv)

        rule_0 = max(min(pa_dict["up"], pv_dict["stop"]), min(pa_dict["up_right"], pv_dict["ccw_slow"]),
                     min(pa_dict["up_left"], pv_dict["cw_slow"]))

        rule_10 = min(pa_dict["down_more_right"], pv_dict["cw_slow"], 1 -  cv_dict["right_slow"])
        rule_12 = min(pa_dict["down_more_left"], pv_dict["ccw_slow"], 1 -  cv_dict["left_slow"])
        # rule_13 = min(pa_dict["down_more_right"], pv_dict["ccw_fast"], 1 -  cv_dict["right_fast"])
        rule_14 = min(pa_dict["down_more_right"], pv_dict["cw_fast"], 1 -  cv_dict["left_slow"])
        rule_16 = min(pa_dict["down_more_left"], pv_dict["ccw_fast"], 1 -  cv_dict["left_slow"])
        rule_21 = min(pa_dict["down_right"], pv_dict["ccw_fast"], 1 -  cv_dict["right_slow"])
        rule_23 = min(pa_dict["down_left"], pv_dict["cw_fast"], 1 -  cv_dict["left_slow"])
        rule_36 = min(pa_dict["down"], pv_dict["cw_fast"], 1 -  cv_dict["left_slow"])
        rule_37 = min(pa_dict["down"], pv_dict["ccw_fast"], 1 -  cv_dict["right_fast"])
        rule_42 = min(pa_dict["up"], pv_dict["stop"], 1 -  cv_dict["stop"])

        values = [rule_0, rule_10, rule_12, rule_14, rule_16, rule_21, rule_23, rule_36, rule_37, rule_42]

        return max(values)


    def left_fast(self, x, is_in=True):
        if not is_in:
            return 0
        if -80 > x >= -100:
            return float(x + 100) / 20
        elif -60 > x >= -80:
            return float(-x - 60)/ 20
        else:
            return 0

    def left_slow(self, x, is_in=True):
        if not is_in:
            return 0
        if -60 > x >= -80:
            return float(x + 80) / 20
        elif 0 > x >= -60:
            return float(-x) / 60
        else:
            return 0

    def f_stop(self, x, is_in=True):
        if not is_in:
            return 0
        if -60 > x >= 0:
            return float(x + 60) / 60
        elif 0 < x <= 60:
            return float(-x + 60) / 60
        else:
            return 0

    def right_slow(self, x, is_in=True):
        if not is_in:
            return 0
        if 0 < x <= 60:
            return float(x) / 60
        elif 60 < x <= 80:
            return float(-x + 60) / 20
        else:
            return 0

    def right_fast(self, x, is_in=True):
        if not is_in:
            return 0
        if 60 < x <= 80:
            return float(x - 60) / 2
        elif 80 < x <= 100:
            return float(-x + 100) / 20
        else:
            return 0


    def calc_center_of_mass(self, pv, pa, cv):
        # force_points = [0 for i in range(200 * 1000 + 1)]
        left_fast = self.left_fast_calc(pv=pv, pa=pa, cv=cv)
        left_slow = self.left_slow_calc(pv=pv, pa=pa, cv=cv)
        f_stop = self.f_stop_calc(pv, pa, cv)
        right_fast = self.right_fast_calc(pv, pa, cv)
        right_slow = self.right_slow_calc(pv, pa, cv)
        lfm = bool(left_fast)  # left_fast membership
        lsm = bool(left_slow)
        fsm = bool(f_stop)
        rfm = bool(right_fast)
        rsm = bool(right_slow)

        print("pv :", pv, ", pa:", pa, "cv : ", cv, "left_fast :", left_fast)
        print("left_slow :", left_slow, "stop:", f_stop, "right_slow:", right_slow, "right_fast: ", right_fast)

        sum = 0
        sum_x = 0

        for i in range(0, 2000, 1):
            x = -100 + i * 0.1
            # if x == -80 and int(pa) == 206:
            #     print("x == 80 and lfm = ", lfm, "func = ", self.left_fast(x, lfm), "leffas = ", left_fast)

            sum += max(min(self.left_fast(x, lfm), left_fast), min(self.left_slow(x, lsm), left_slow),
                            min(self.f_stop(x, fsm), f_stop), min(self.right_slow(x, rsm), right_slow),
                            min(self.right_fast(x, rfm), right_fast))
            sum_x = sum_x + max(min(self.left_fast(x, lfm), left_fast), min(self.left_slow(x, lsm), left_slow),
                       min(self.f_stop(x, fsm), f_stop), min(self.right_slow(x, rsm), right_slow),
                       min(self.right_fast(x, rfm), right_fast)) * x
        # if sum == 0 :
        # x = 80.01
        # print(" values", min(self.left_fast(x, lfm), left_fast), min(self.left_slow(x, lsm), left_slow),
        #                     min(self.f_stop(x, fsm), f_stop), min(self.right_slow(x, rsm), right_slow),
        #                     min(self.right_fast(x, rfm), right_fast))
        print("sum : ", sum)
        print("sum x : ", sum_x)
        return sum_x / sum
