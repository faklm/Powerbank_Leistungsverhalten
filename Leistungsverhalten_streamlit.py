import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Parameter der Quelle
U0 = 4.95 # Leerlaufspannung [V]
Ri = 0.496 # Innenwiderstand [Ohm]

st.title("Ausgangskennlinie einer realen Spannungsquelle")

# Sidebar für Lastwiderstand
RL_slider = st.sidebar.slider("R$_L$ [Ω]", 0.001, 10.0, 2.5, step=0.001, format="%.3f")
RL_input = st.sidebar.number_input("R$_L$ eingeben [Ω]", min_value=0.001, max_value=10.0, value=2.5, step=0.001, format="%.3f")

# Button zur Bestätigung der Eingabe
if st.sidebar.button("R$_L$ setzen"):
    RL = RL_input
else:
    RL = RL_slider

# Maximaler Strom
Imax = U0 / Ri * 1.1
I = np.linspace(0, Imax, 400)

# Kennlinien berechnen
U_quelle = U0 - I * Ri
U_last = I * RL

# Arbeitspunkt
IA = U0 / (Ri + RL)
UA = IA * RL
Ui = IA * Ri
P = UA * IA
IK = U0 / Ri  # Kurzschlussstrom

# Plot erstellen
fig, ax = plt.subplots(figsize=(8,6))
ax.plot(I, U_quelle, label="Kennlinie Quelle", color="blue")
ax.plot(I, U_last, label=f"Kennlinie Last (R$_L$={RL:.3f} Ω)", color="green")
ax.plot([IA], [UA], 'ro', label="Arbeitspunkt")
ax.fill_between([0, IA], 0, UA, color='red', alpha=0.2)

# Pfeile für Spannungen
ax.annotate("", xy=(0, UA), xytext=(0, 0), arrowprops=dict(arrowstyle='<->', color='green', lw=2))
ax.annotate("", xy=(0, U0), xytext=(0, UA), arrowprops=dict(arrowstyle='<->', color='orange', lw=2))
ax.text(-0.2, UA/2, f"U$_A$ = {UA:.2f} V", va='center', ha='right', color='green')
ax.text(-0.2, UA + Ui/2, f"U$_i$ = {Ui:.2f} V", va='center', ha='right', color='orange')

# Textfelder für U0 und IK
ax.text(-0.1, U0, f"U$_0$ = {U0:.2f} V", color='blue', va='bottom', ha='right')
ax.text(IK, -0.5, f"I$_K$ = {IK:.2f} A", color='blue', va='top', ha='center')

# Achsen und Layout
ax.set_xlim(0, Imax)
ax.set_ylim(0, U0*1.1)
ax.set_xlabel("Strom I$_A$ [A]")
ax.set_ylabel("Spannung [V]")
ax.legend()
ax.grid(True)

# Leistung anzeigen
st.write(f"**Leistung P:** {P:.2f} W")

# Plot anzeigen
st.pyplot(fig)
