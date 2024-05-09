import matplotlib.pyplot as plt


# Definición de las ecuaciones del modelo
def dTt_dt(T, P, N, DBO, DQO, V, It, R, T_ext, F_nut, r_p, K_p, r_f, K_f, a, b, c, d, e, T_opt, alpha, beta_nut, gamma, delta, e_DBO, beta_DBO, e_DQO, beta_DQO, k_ilum, k_temp, tau):
    dTtdt = r_p * T * (1 - T / K_p) - a * N * P * ((T - T_opt) / T_opt) ** alpha - gamma * (DBO + DQO) * (V / V_0) - delta * It
    return dTtdt


def dP_dt(T, P, N, DBO, DQO, V, It, R, T_ext, F_nut, r_p, K_p, r_f, K_f, a, b, c, d, e, T_opt, alpha, beta_nut, gamma, delta, e_DBO, beta_DBO, e_DQO, beta_DQO, k_ilum, k_temp, tau):
    dPdt = r_f * P * (1 - P / K_f) - b * P * T / (P + T) * ((T - T_opt) / T_opt) ** alpha - gamma * (DBO + DQO) * (V / V_0)
    return dPdt


def dN_dt(T, P, N, DBO, DQO, V, It, R, T_ext, F_nut, r_p, K_p, r_f, K_f, a, b, c, d, e, T_opt, alpha, beta_nut, gamma, delta, e_DBO, beta_DBO, e_DQO, beta_DQO, k_ilum, k_temp, tau):
    dNdt = c * R - e * N - a * N * P * ((T - T_opt) / T_opt) ** alpha + beta_nut * F_nut * (V / V_0)
    return dNdt


def dR_dt(T, P, N, DBO, DQO, V, It, R, T_ext, F_nut, r_p, K_p, r_f, K_f, a, b, c, d, e, T_opt, alpha, beta_nut, gamma, delta, e_DBO, beta_DBO, e_DQO, beta_DQO, k_ilum, k_temp, tau):
    dRdt = -c * R + d
    return dRdt


def dT_dt(T, P, N, DBO, DQO, V, It, R, T_ext, F_nut, r_p, K_p, r_f, K_f, a, b, c, d, e, T_opt, alpha, beta_nut, gamma, delta, e_DBO, beta_DBO, e_DQO, beta_DQO, k_ilum, k_temp, tau):
    dTdt = k_temp * It - (T - T_ext) / tau
    return dTdt


def dDBO_dt(T, P, N, DBO, DQO, V, It, R, T_ext, F_nut, r_p, K_p, r_f, K_f, a, b, c, d, e, T_opt, alpha, beta_nut, gamma, delta, e_DBO, beta_DBO, e_DQO, beta_DQO, k_ilum, k_temp, tau):
    dDBOdt = e_DBO * (R - DBO) - beta_DBO * P * T
    return dDBOdt


def dDQO_dt(T, P, N, DBO, DQO, V, It, R, T_ext, F_nut, r_p, K_p, r_f, K_f, a, b, c, d, e, T_opt, alpha, beta_nut, gamma, delta, e_DBO, beta_DBO, e_DQO, beta_DQO, k_ilum, k_temp, tau):
    dDQOdt = e_DQO * (R - DQO) - beta_DQO * P * T
    return dDQOdt


def dV_dt(T, P, N, DBO, DQO, V, It, R, T_ext, F_nut, r_p, K_p, r_f, K_f, a, b, c, d, e, T_opt, alpha, beta_nut, gamma, delta, e_DBO, beta_DBO, e_DQO, beta_DQO, k_ilum, k_temp, tau):
    dVdt = V * (c * R - d - e * N)
    return dVdt


def dI_dt(T, P, N, DBO, DQO, V, It, R, T_ext, F_nut, r_p, K_p, r_f, K_f, a, b, c, d, e, T_opt, alpha, beta_nut, gamma, delta, e_DBO, beta_DBO, e_DQO, beta_DQO, k_ilum, k_temp, tau):
    dIdt = - k_ilum * It - alpha_sol * T * It + I_sol
    return dIdt


# Parámetros del modelo
r_p = 0.5                       # Tasa de crecimiento de las plantas.
K_p = 100                       # Capacidad de carga para el crecimiento de las plantas.
r_f = 0.3                       # Tasa de crecimiento de los peces.
K_f = 200                       # Capacidad de carga para el crecimiento de los peces.
a = 0.1                         # Factor de interacción entre plantas y peces.
b = 0.05                        # Factor de interacción entre plantas y peces.
c = 0.2                         # Tasa de reposición de nutrientes en el ambiente.
d = 0.1                         # Tasa de decaimiento de recursos en el ambiente.
e = 0.05                        # Tasa de degradación de nutrientes en el sistema.
T_opt = 25                      # Temperatura óptima para el crecimiento de plantas y peces.
alpha = 0.1                     # Sensibilidad de las tasas de crecimiento al cambio de temperatura.
beta_nut = 0.02                 # Sensibilidad de la entrada/salida de nutrientes al flujo de nutrientes.
gamma = 0.05                    # Sensibilidad de las tasas de crecimiento al contenido de oxígeno disuelto.
delta = 0.03                    # Sensibilidad de las tasas de crecimiento a la iluminación.
e_DBO = 0.03                    # Tasa de degradación de la DBO.
beta_DBO = 0.5                  # Eficiencia de producción/consumo de DBO.
e_DQO = 0.02                    # Tasa de degradación de la DQO.
beta_DQO = 0.6                  # Eficiencia de producción/consumo de DQO.
k_ilum = 0.1                    # Coeficiente de atenuación del agua para la iluminación.
k_temp = 0.05                   # Coeficiente de eficiencia de calentamiento por la luz solar.
tau = 120                       # Escala de tiempo característica (en días).
F_nut = 100                     # Flujo de nutrientes.
alpha_sol = 0.5                 # Sensibilidad de las tasas de crecimiento a la iluminación solar.
I_sol = 1000                    # Intensidad de la luz solar en Cartagena de Indias en un día soleado al mediodía (en W/m^2).


# Implementación del método de Euler
def euler_method(Tt_0, P_0, N_0, DBO_0, DQO_0, V_0, I_0, R_0, T_0, F_nut, dt, num_steps):
    # Listas para almacenar los valores de las variables en cada paso de tiempo
    Tt_values = [Tt_0]
    P_values = [P_0]
    N_values = [N_0]
    DBO_values = [DBO_0]
    DQO_values = [DQO_0]
    V_values = [V_0]
    I_values = [I_0]
    R_values = [R_0]
    T_values = [T_0]

    # Iteración sobre los pasos de tiempo
    for i in range(num_steps):
        # Calcular las derivadas en el tiempo actual
        dTt = dTt_dt(T_values[-1], P_values[-1], N_values[-1], DBO_values[-1], DQO_values[-1], V_values[-1], I_values[-1], R_values[-1], T_ext_values[-1], F_nut, r_p, K_p, r_f, K_f, a, b, c, d, e, T_opt, alpha, beta_nut, gamma, delta, e_DBO, beta_DBO, e_DQO, beta_DQO, k_ilum, k_temp, tau)

        dP = dP_dt(T_values[-1], P_values[-1], N_values[-1], DBO_values[-1], DQO_values[-1], V_values[-1], I_values[-1], R_values[-1], T_ext_values[-1], F_nut, r_p, K_p, r_f, K_f, a, b, c, d, e, T_opt, alpha, beta_nut, gamma, delta, e_DBO, beta_DBO, e_DQO, beta_DQO, k_ilum, k_temp, tau)

        dN = dN_dt(T_values[-1], P_values[-1], N_values[-1], DBO_values[-1], DQO_values[-1], V_values[-1], I_values[-1], R_values[-1], T_ext_values[-1], F_nut, r_p, K_p, r_f, K_f, a, b, c, d, e, T_opt, alpha, beta_nut, gamma, delta, e_DBO, beta_DBO, e_DQO, beta_DQO, k_ilum, k_temp, tau)

        dR = dR_dt(T_values[-1], P_values[-1], N_values[-1], DBO_values[-1], DQO_values[-1], V_values[-1], I_values[-1], R_values[-1], T_ext_values[-1], F_nut, r_p, K_p, r_f, K_f, a, b, c, d, e, T_opt, alpha, beta_nut, gamma, delta, e_DBO, beta_DBO, e_DQO, beta_DQO, k_ilum, k_temp, tau)

        dT = dT_dt(T_values[-1], P_values[-1], N_values[-1], DBO_values[-1], DQO_values[-1], V_values[-1], I_values[-1], R_values[-1], T_ext_values[-1], F_nut, r_p, K_p, r_f, K_f, a, b, c, d, e, T_opt, alpha, beta_nut, gamma, delta, e_DBO, beta_DBO, e_DQO, beta_DQO, k_ilum, k_temp, tau)

        dDBO = dDBO_dt(T_values[-1], P_values[-1], N_values[-1], DBO_values[-1], DQO_values[-1], V_values[-1], I_values[-1], R_values[-1], T_ext_values[-1], F_nut, r_p, K_p, r_f, K_f, a, b, c, d, e, T_opt, alpha, beta_nut, gamma, delta, e_DBO, beta_DBO, e_DQO, beta_DQO, k_ilum, k_temp, tau)

        dDQO = dDQO_dt(T_values[-1], P_values[-1], N_values[-1], DBO_values[-1], DQO_values[-1], V_values[-1], I_values[-1], R_values[-1], T_ext_values[-1], F_nut, r_p, K_p, r_f, K_f, a, b, c, d, e, T_opt, alpha, beta_nut, gamma, delta, e_DBO, beta_DBO, e_DQO, beta_DQO, k_ilum, k_temp, tau)

        dV = dV_dt(T_values[-1], P_values[-1], N_values[-1], DBO_values[-1], DQO_values[-1], V_values[-1], I_values[-1], R_values[-1], T_ext_values[-1], F_nut, r_p, K_p, r_f, K_f, a, b, c, d, e, T_opt, alpha, beta_nut, gamma, delta, e_DBO, beta_DBO, e_DQO, beta_DQO, k_ilum, k_temp, tau)

        dI = dI_dt(T_values[-1], P_values[-1], N_values[-1], DBO_values[-1], DQO_values[-1], V_values[-1], I_values[-1], R_values[-1], T_ext_values[-1], F_nut, r_p, K_p, r_f, K_f, a, b, c, d, e, T_opt, alpha, beta_nut, gamma, delta, e_DBO, beta_DBO, e_DQO, beta_DQO, k_ilum, k_temp, tau)

        # Calcular los nuevos valores de las variables utilizando el método de Euler.
        Tt_new = Tt_values[-1] + dt * dTt
        P_new = P_values[-1] + dt * dP
        N_new = N_values[-1] + dt * dN
        DBO_new = DBO_values[-1] + dt * dDBO
        DQO_new = DQO_values[-1] + dt * dDQO
        V_new = V_values[-1] + dt * dV
        I_new = I_values[-1] + dt * dI
        R_new = R_values[-1] + dt * dR
        T_new = T_values[-1] + dt * dT

        # Almacenar los nuevos valores en las listas.
        Tt_values.append(Tt_new)
        P_values.append(P_new)
        N_values.append(N_new)
        DBO_values.append(DBO_new)
        DQO_values.append(DQO_new)
        V_values.append(V_new)
        I_values.append(I_new)
        R_values.append(R_new)
        T_values.append(T_new)

    return Tt_values, P_values, N_values, DBO_values, DQO_values, V_values, I_values, R_values, T_values


# Parámetros y condiciones iniciales.
T_0 = 50    # Biomasa inicial de plantas.
P_0 = 100   # Población inicial de peces.
N_0 = 50    # Concentración inicial de nutrientes.
DBO_0 = 10  # Valor inicial de DBO.
DQO_0 = 15  # Valor inicial de DQO.
V_0 = 1000  # Volumen inicial de agua.
I_0 = 1000  # Intensidad de luz inicial.
R_0 = 50    # Recursos iniciales en el ambiente.
T_ext_0 = 20  # Temperatura inicial del ambiente.

T_values = [T_0]
P_values = [P_0]
N_values = [N_0]
DBO_values = [DBO_0]
DQO_values = [DQO_0]
V_values = [V_0]
I_values = [I_0]
R_values = [R_0]
T_ext_values = [T_ext_0]

dt = 0.1  # Tamaño del paso de tiempo.
num_steps = 20  # Número total de pasos de tiempo.

# Llamada al método de Euler para resolver el sistema de ecuaciones.
T_values, P_values, N_values, DBO_values, DQO_values, V_values, I_values, R_values, T_ext_values = euler_method(T_0, P_0, N_0, DBO_0, DQO_0, V_0, I_0, R_0, T_ext_0, F_nut, dt, num_steps)

# Imprimir los resultados o realizar cualquier otro análisis deseado.
print("Biomasa de plantas:", T_values)
print("Población de peces:", P_values)
print("Concentración de nutrientes:", N_values)
print("Valor de DBO:", DBO_values)
print("Valor de DQO:", DQO_values)
print("Volumen de agua:", V_values)
print("Intensidad de luz:", I_values)
print("Recursos en el ambiente:", R_values)
print("Temperatura del ambiente:", T_ext_values)

plt.figure(figsize=(15, 15))

plt.subplot(3, 3, 1)
plt.plot(T_values)
plt.title('Biomasa de plantas (T)')
plt.xlabel('Tiempo')
plt.ylabel('Biomasa')
plt.grid(True)

plt.subplot(3, 3, 2)
plt.plot(P_values, color='orange')
plt.title('Población de peces (P)')
plt.xlabel('Tiempo')
plt.ylabel('Población')
plt.grid(True)

# Gráfico de Concentración de nutrientes (N) y Valor de DBO.
plt.subplot(3, 3, 3)
plt.plot(N_values, color='green')
plt.title('Concentración de nutrientes (N)')
plt.xlabel('Tiempo')
plt.ylabel('Concentración')
plt.grid(True)

plt.subplot(3, 3, 4)
plt.plot(DBO_values, color='red')
plt.title('Valor de DBO')
plt.xlabel('Tiempo')
plt.ylabel('DBO')
plt.grid(True)

# Gráfico de Valor de DQO y Volumen de agua (V).
plt.subplot(3, 3, 5)
plt.plot(DQO_values, color='purple')
plt.title('Valor de DQO')
plt.xlabel('Tiempo')
plt.ylabel('DQO')
plt.grid(True)

plt.subplot(3, 3, 6)
plt.plot(V_values, color='brown')
plt.title('Volumen de agua (V)')
plt.xlabel('Tiempo')
plt.ylabel('Volumen')
plt.grid(True)

# Gráfico de Intensidad de luz (I) y Recursos en el ambiente (R).
plt.subplot(3, 3, 7)
plt.plot(I_values, color='pink')
plt.title('Intensidad de luz (I)')
plt.xlabel('Tiempo')
plt.ylabel('Intensidad')
plt.grid(True)

plt.subplot(3, 3, 8)
plt.plot(R_values, color='olive')
plt.title('Recursos en el ambiente (R)')
plt.xlabel('Tiempo')
plt.ylabel('Recursos')
plt.grid(True)

# Gráfico de Temperatura del ambiente (T_ext).
plt.subplot(3, 3, 9)
plt.plot(T_ext_values, color='cyan')
plt.title('Temperatura del ambiente (T_ext)')
plt.xlabel('Tiempo')
plt.ylabel('Temperatura')
plt.grid(True)

plt.show()
