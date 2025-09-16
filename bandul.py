import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Simulasi Bandul Sederhana")

# Input parameter
L = st.slider("Panjang tali (m)", 0.1, 2.0, 1.0, 0.1)
g = 9.8
theta0 = st.slider("Sudut awal (derajat)", 1, 90, 30)
t_max = st.slider("Waktu simulasi (detik)", 1, 20, 10)

# Konversi sudut ke radian
theta0_rad = np.radians(theta0)

# Rumus periode bandul sederhana
T = 2 * np.pi * np.sqrt(L / g)
st.write(f"Periode Bandul: {T:.2f} detik")

# Waktu
t = np.linspace(0, t_max, 500)

# Sudut sebagai fungsi waktu (aproksimasi bandul kecil)
theta = theta0_rad * np.cos(np.sqrt(g / L) * t)

# Posisi x, y bandul
x = L * np.sin(theta)
y = -L * np.cos(theta)

# Plot lintasan
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_aspect("equal", "box")
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_title("Lintasan Bandul")

st.pyplot(fig)
