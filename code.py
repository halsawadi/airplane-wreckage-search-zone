mport numpy as np # you have to import numpy library

def total_movement(theta,v_ascent,ascent_rate,tw,v_descent,descent_rate,alpha,wind_speed_formula):

    # theta: heading angle in degrees
    # v_ascent: airspeed on ascent in m/s
    # ascent_rate: ascent rate in m/s
    # tw: time period from takeoff to engine failure
    # v_descent: airspeed on descent in m/s
    # descent_rate: descent rate
    # alpha: wind angle
    # wind_speed_formula : wind speed function formula in terms of time t. write the formula as it is (using t variable only)
    # between single quotation marks. Example: '-(1/720)*t**2+25'. Remember power in python is written like this t**2 not t^2

    x1,y1 = ascent_movement(v_ascent,tw,theta)
    x2,y2 = descent_movement(v_descent,tw,theta,ascent_rate,descent_rate)
    x3,y3 = wind_movement(wind_speed_formula,tw,alpha,ascent_rate,descent_rate,)

    X = x1 + x2 + x3
    Y = y1 + y2 + y3

    distance = np.sqrt(np.power(X,2)+np.power(Y,2))
    if(np.sign(X) == 1.0 and np.sign(Y) == -1.0):
        direction = np.arctan(X/Y)*(180/np.pi) + 180
    elif(np.sign(X) == -1.0 and np.sign(Y) == -1.0):
        direction = np.arctan(X/Y)*(180/np.pi) - 180
    else:
        direction = np.arctan(X/Y)*(180/np.pi)

    return distance, direction

def ascent_movement(v_ascent,tw,theta):
    x1 = v_ascent*tw*np.sin(theta*(np.pi/180))
    y1 = v_ascent*tw*np.cos(theta*(np.pi/180))
    return x1, y1


def descent_movement(v_descent,tw,theta,ascent_rate,descent_rate):
    x2 = (ascent_rate*tw*v_descent/descent_rate)*np.sin(theta*(np.pi/180))
    y2 = (ascent_rate*tw*v_descent/descent_rate)*np.cos(theta*(np.pi/180))
    return x2,y2

def wind_movement(wind_speed_formula,tw,alpha,ascent_rate,descent_rate):
    tf = (ascent_rate*tw)/descent_rate
    var = {'t':np.linspace(0,tf,10000000)}
    w = eval(wind_speed_formula,var)
    x3 = np.trapz(w, var['t'])*np.sin(2*np.pi - alpha*(np.pi/180))
    y3 = np.trapz(w, var['t'])*np.cos(2*np.pi - alpha*(np.pi/180))
    return x3,y3
