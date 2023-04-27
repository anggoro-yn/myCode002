#Import Streamlit library
import streamlit as st

#Displaying Markdown
st.markdown("# Hi,\n# ***People*** \t!!!!!!!!!")
st.markdown('## Welcome to')
st.markdown("""### Streamlit's World""")

#Displaying Latex
st.latex(r'''cos2\theta = 1 - 2sin^2\theta''')
st.latex("""(a+b)^2 = a^2 + b^2 + 2ab""")
st.latex(r'''\frac{\partial u}{\partial t}
= h^2 \left( \frac{\partial^2 u}{\partial x^2}
+ \frac{\partial^2 u}{\partial y^2}
+ \frac{\partial^2 u}{\partial z^2} \right)''')

# Displaying Python Code
st.subheader("""Python Code""")
code = '''def hello():
print("Hello, Streamlit!")'''
st.code(code, language='python')
# Displaying Java Code
st.subheader("""Java Code""")
st.code("""public class GFG {
public static void main(String args[])
{
System.out.println("Hello World");
}
}""", language='javascript')
st.subheader("""JavaScript Code""")
st.code(""" <p id="demo"></p>
<script>
try {
adddlert("Welcome guest!");
}
catch(err) {
document.getElementById("demo").innerHTML = err.message;
}
</script> """)

# Import Necessary libraries
import pandas as pd
import numpy as np
# defining random values in a dataframe using pandas and numpy
df = pd.DataFrame(
np.random.randn(20, 5),
columns=('col_no %d' % i for i in range(5)))
st.dataframe(df)

# defining random values in a dataframe using pandas and numpy
df = pd.DataFrame(
np.random.randn(20, 5),
columns=('col_no %d' % i for i in range(5)))
# Highlighting minimum value objects
st.dataframe(df.style.highlight_min(axis=0))
