#### iterations ###

import math
def square(x): return x*x
def squareroot(x): return math.sqrt(x)

m_pl = 7200
moe_mtow = 0.576
MTOW = 25185.82
mf_mtow = 0.131735403

M_mto = m_pl/(1-moe_mtow-mf_mtow)

e = 0.54853362
Clfl = 0.45
A_wet_wing = 449
bypass_ratio = 4.9
cl_max_landing= 2.31
AR = 8.21
sweep_lew = 0.563741
stall_speed = 51.85
lfl = Clfl*stall_speed**2

#cd0

W_S = 4257
T_W = 0.203
g = 9.81
taper_ratio = 0.32
sweep_c_4 = 29.4

S = (MTOW*g)/W_S

b = squareroot(AR*S)

C_r = 2*S/((1+taper_ratio)*b)
C_t = taper_ratio*C_r
LE_sweep = sweep_c_4-C_r/(2*b)*(taper_ratio-1)
C_mac = (2/3)*C_r*(1+taper_ratio*taper_ratio**2)//(1+taper_ratio)

# required for tail #
l_fus = 27.47
lnc = 4.67
ltc = 6.23
x_aft = 12.238
htv_coefficient = 0.82
htail_AR = 3.4
htail_taper = 0.4
c_ = 2.64
c4 = 29.4
vtv_coefficient = 0.11
vtail_AR = 0.9
vtail_taper = 0.45

# Horizontal tail #
x_h = 0.9*l_fus
aft_cg_m = 12.238
s_h = htv_coefficient*c_*S/aft_cg_m
span_h = (s_h*htail_AR)**0.5
cr_h = 2*s_h/((1+htail_taper)*span_h)
ct_h = htail_taper*cr_h
MAC_h = (2/3)*cr_h*(1+htail_taper*htail_taper**2)/(1+htail_taper)
sweep_c4_h = (40-c4)/2+c4

# Vertical Tail #
s_v = vtv_coefficient*b*S/aft_cg_m
span_v = (s_v*vtail_AR)**0.5
cr_v = 2*s_v/((1+vtail_taper)*span_v)
ct_v = vtail_taper*cr_v
MAC_v = (2/3)*cr_v*(1+vtail_taper*vtail_taper**2)/(1+vtail_taper)
sweep_c4_v = (50-c4)/2+c4

B_h_new = 3.2808399*span_h*2
B_h = 3.2808399*11.73519996
print("BH new:", B_h_new)
print("BH:", B_h)

print("M_mto:", M_mto)
print("Landing field length:", lfl)
print("Wing area:", S)
print("Wingspan:", b)
print("Root Chord:", C_r)
print("Tip Chord:", C_t)
print("Leading edge sweep:", LE_sweep)
print("MAC:", C_mac)

print("Horizontal tail area:", s_h)
print("Horizontal tail span:", span_h)
print("Root chord horizontal:", cr_h)
print("Tail chord horizontal:", ct_h)
print("MAC chord horizontal:", MAC_h)
print("Sweep c4 horizontal:", sweep_c4_h)

print("Vertical tail area:", s_v)
print("Vertical tail span:", span_v)
print("Vertical tail root chord:", cr_v)
print("Vertical tail tip chord:", ct_v)
print("MAC chord vertical:", MAC_v)
print("Sweep c4 vertical:", sweep_c4_v)
