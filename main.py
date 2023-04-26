#Import Streamlit library
import streamlit as st
#Displaying Latex
st.latex(r'''cos2\theta = 1 - 2sin^2\theta''')
st.latex("""(a+b)^2 = a^2 + b^2 + 2ab""")
st.latex(r'''\frac{\partial u}{\partial t}
= h^2 \left( \frac{\partial^2 u}{\partial x^2}
+ \frac{\partial^2 u}{\partial y^2}
Chapter 2 Ttext and table elements
26
+ \frac{\partial^2 u}{\partial z^2} \right)''')
