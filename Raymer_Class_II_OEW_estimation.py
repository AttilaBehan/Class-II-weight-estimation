#from Raymer_variables import *
import math
# Design variables and parameters (fill in actual values for specific design)
A   = 8.39                      #Aspect ratio                                              
A_h = 3.4                       #Horizontal tail aspect ratio                           
A_v = 0.9                       #Vertical tail aspect ratio
B_h = 3.2808399*11.7352         #Horizontal tail span (ft) 
B_w = 3.2808399*22.14           #Wing span (ft)                                                                            
D   = 3.2808399*3.1             #Fuselage structural depth (ft)                            
F_w = 3.2808399*1.5             #Fuselage width at horizontal tail section (ft)  CHANGE VALUE         
Ht_per_Hv = 0.0                 #For conventional tail, 1.0 for T tail               
t_c_wing  = 0.15                #Thickness to chord ratio at wing root
t_c_vt    = 0.1                 #Thickness to chord ratio at vertical stabilizer root
R_kva     = 51                  #System electrcal rating (40-60) (kvA)
lambda_   = 0.32                #Wing taper ratio    
Lambda    = math.pi/180*29.4    #Wing sweep angle at 25% MAC (rad)                   
Lambda_ht = math.pi/180*34.7    #Horizontal tail sweep at 25% MAC (rad)
Lambda_vt = math.pi/180*39.7    #Vertical tail sweep at 25% MAC (rad)             

# Similar notation stuff
L    = 3.2808399*21.77      #Overall length of fuselage (exclude radome and tail cap) (ft)          
L_ec = 3.2808399*11         #Length from engine from to cockpict, total if multi engine (ft)          
L_a  = 100                  #Electrical routing distance (ft)     
L_f  = 3.2808399*27.47      #Total fuselage length (ft)                              
L_t  = 3.2808399*11.043     #Length to horizontal tail (ft)                         
L_m  = 3.2808399*11         #Length from wing quarter-MAC to tail quarter-MAC (ft)  
L_n  = 39.370*2.1           #Nose gear length (in)    CHANGE VALUE

L_in   = 3.2808399*2.9      #Fuselage inner diameter (ft)
L_cab  = 3.2808399*19.44    #Cabin length (ft)
L_no   = 3.2808399*4.67     #Nose length (ft)
L_tail = 3.2808399*4.89     #Tail length (ft)

N_z   = 4.32                #Load factor                                            
N_mw  = 4                   #Number of main wheels                                 
N_nw  = 2                   #Number of nose wheels                                  
N_l   = 3                   #Number of landing gears                                
N_mss = 2                   #Number of main gear shock struts                      
N_en  = 2                   #Number of engines                                      
N_t   = 2                   #Number of fuel tanks                                    
N_f   = 6                   #Number of functions performed by controls (4-7)         
N_m   = 2                   #Number of mechanical functions (0-2)                    
N_c   = 2                   #Number of crew (only pilots)                            
N_gen = N_en                #Number of generators                                  
N_p   = 76                  #Number of personel onboard (crew+passengers)
N_Lt  = 3.2808399*3.85      #Nacelle length (ft)
N_w   = 3.2808399*1.54      #Nacelle width (ft)
S_w   = 10.7639104*58.4             #Wing surface area (ft^2)                               
S_csw = 10.7639104*(9.6+6.1+8.22)   #Control surface area (wing-mounted) (ft^2)           
S_cs  = 10.7639104*(9.6+6.1+8.22+3+3) #Total area of control surface (ft^2)    
S_f   = 10.7639104*217.53           #Fuselage wetted area (ft^2)                                
S_ht  = 10.7639104*10.1261          #Horizontal tail area (ft^2)                           
S_e   = 10.7639104*3                #Elevator area (ft^2)                                               
S_vt  = 10.7639104*11.392           #Vertical tail area (ft^2)
S_n   = N_Lt*N_w*math.pi            #Nacelle wetted area (ft^2)
V_stall = 3.2808399*51.85   #Stall speed (ft/s)                                  
V_t  = 219.969157*4.15      #Total fuel volume (gal) (converting from from m^3)                                 
V_i  = 219.969157*0         #Integral tanks volume (gal)                             
V_p  = 219.969157*6.93      #Self sealing "protected" tanks volume (gal)             
V_pr = (L_in/2)**2*math.pi*(L_cab+L_no/3+L_tail/3) #Volume of pressurized section (ft^3)

K_door = 1.0     #For no cargo door                                   
K_Lg   = 1.0     #1.12  For fuselage-mounted landing gear, 1.0 otherwise         
K_mp   = 1.0     #1.126 For kneeling gear, 1.0 otherwise                        
K_np   = 1.0     #1.15  For kneeling gear, 1.0 otherwise                           
K_ng   = 1.017   #Pylon-mounted nacelle, 1.0 otherwise                    
K_r    = 1.0     #1.133 For reciprocating engine, 1.0 otherwise                      
K_uht  = 1.0     #1.143 For unit (all-moving) horizontal tail, 1.0 otherwise   
K_ws   = 0.75*(1+2*lambda_)/(1+lambda_)*B_w*math.tan(Lambda)/L                                         
K_y    = 0.3*L_t #Aircraft pitching radius of gyration ~0.3*L_t (ft)       
K_z    = L_t     #Aircraft yawing radius of gyration ~L_t (ft)                 
K_tp   = 1.0     #0.793 For turboprop, 1.0 otherwise
K_p    = 1.0     #1.4 for engine with propeller or 1.0 otherwise
K_tr   = 1.18    #1.18 for jet with thrust reverer or 1.0 otherwise

#I_y       = 1/12*55000*(3*(L_in/2)**2+L**2)*5/4      #Yawing moment of inertia (lb-ft^2)
I_y =27254011.48830488*0.0190280424
print(I_y)

#Some more weights
W_dg   = 2.20462262*25327 #Design gross weight (lb)                              
W_l    = 2.20462262*22541 #Landing design gross weight (lb)                        
W_en   = 2780             #Engine weight (lb)                                     
W_APU_uninstalled = 309   #APU weight independent from installment (lb)  
W_uav  = 2.20462262*1300  #Uninstalled avionics weight (800-1400) (lb)           
W_c    = 2.20462262*2979.4           #Maximum cargo weight (lb) (25327-14816-76*99.1)
W_ec   = 2.331*W_en**0.901*K_p*K_tr  #Weight of engine and contents (lb per nacelle)
m_fuel=0.131*25327

#Raymer Cargo/Transport Weights

# 1. Wing Weight
W_wing = 0.0051*(W_dg*N_z)**0.557*S_w**0.649*A**0.5*t_c_wing**(-0.4)*(1+lambda_)**0.1*math.cos(Lambda)**(-1)*S_csw**0.1 

# 2. Horizontal Tail Weight
W_horizontal_tail = 0.0379*K_uht*(1+F_w/B_h)**(-0.25)*W_dg**0.639*N_z**0.1*S_ht**0.75*(L_t)**(-1.0)*K_y**0.704*math.cos(Lambda_ht)**(-1.0)*A_h**0.166*(1+S_e/S_ht)**0.1

# 3. Vertical Tail Weight
W_vertical_tail = 0.0026*(1 + Ht_per_Hv)**0.225*W_dg**0.556*N_z**0.536*L_t**(-0.5)*S_vt**0.5*K_z**0.875*math.cos(Lambda_vt)**(-1.0)*A_v**0.35*t_c_vt**(-0.5)

# 4. Fuselage Weight
W_fuselage = 0.3280*K_door*K_Lg*(W_dg*N_z)**0.5*L**0.25*S_f**0.302*(1+K_ws)**0.4*(L/D)**0.1

# 5. Main Landing Gear Weight
W_main_landing_gear = 0.0106*K_mp*W_l**0.888*N_l**0.25*L_m**0.4*N_mw**0.321*N_mss**(-0.5)*V_stall**0.1

# 6. Nose Gear Weight
W_nose_landing_gear = 0.032*K_np*W_l**0.646*N_l**0.2*L_n**0.5*N_nw**0.45

# 7. Nacelle Group Weight
W_nacelle_group = 0.6724*K_ng*N_Lt**0.10*N_w**0.294*N_z**0.119*W_ec**0.611*N_en**0.984*S_n**0.224

# 8. Engine Controls Weight (L_ec)
W_engine_controls = 5.0 * N_en + 0.80 * L_ec

# 9. Starter Pneumatic Weight 
W_starter_pneumatic = 49.19*(N_en*W_en/1000)**0.541

# 10. Fuel System Weight
W_fuel_system = 2.405*V_t**0.606*(1+V_i/V_t)**(-1)*(1 + V_p/V_t)*N_t**0.5

# 11. Flight Controls Weight
W_flight_controls = 145.9*N_f**0.554*(1+N_m/N_f)**(-1)*S_cs**0.20*(I_y*10**(-6))**0.07

# 12. APU Installed Weight (W_APU_uninstalled)
W_APU_installed = 2.2*W_APU_uninstalled

# 13. Instruments Weight
W_instruments = 4.509*K_r*K_tp*N_c**0.541*N_en*(L_f+B_w)**0.5

# 14. Hydraulics Weight
W_hydraulics = 0.2673*N_f*(L_f+B_w)**0.937

# 15. Electrical Weight     (L_a)
W_electrical = 7.291*R_kva**0.782*L_a**0.346*N_gen**0.10

# 16. Avionics Weight       
W_avionics = 1.73*W_uav**0.983

# 17. Furnishings Weight
W_furnishings = 0.0577*N_c**0.1*W_c**0.393*S_f**0.75

# 18. Air Conditioning Weight     
W_air_conditioning = 62.36*N_p**0.25*(V_pr/1000)**0.604*W_uav**0.10 

# 19. Anti-Ice System Weight
W_anti_ice = 0.002*W_dg

# 20. Handling Gear Weight
W_handling_gear = 3.0*10**(-4)*W_dg 

print("Wing group")
print(W_wing+W_main_landing_gear)

print("Tail group")
print(W_horizontal_tail+W_vertical_tail)

print("Fuselage group")
print(W_fuselage)

print("Landing Gear Group")
print(W_main_landing_gear+W_nose_landing_gear)

print("Surface controls group")
print(W_flight_controls)

print("Nacelle group")
print(W_nacelle_group)

print("")
print("OEW")   
OEW = W_wing+W_horizontal_tail+W_vertical_tail+W_fuselage+W_main_landing_gear+W_nose_landing_gear+W_nacelle_group+W_engine_controls+W_starter_pneumatic \
+W_fuel_system+W_flight_controls+W_APU_installed+W_instruments+W_hydraulics+W_electrical+W_avionics+W_furnishings+W_air_conditioning+W_anti_ice+W_handling_gear+N_en*W_ec
print(OEW/2.20462262)
