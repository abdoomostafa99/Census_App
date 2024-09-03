import streamlit as st

st.set_page_config(page_title="Contact Us", page_icon=":email:", layout="centered")

st.title("Contact Us")

st.write("We are here to help you! You can reach out to us through the following methods:")

st.subheader("Get in Touch")
st.write("For any inquiries, feel free to contact us using the information below:")

st.write("📧 **Email**: [abdoomostafa333@gmail.com](https://mail.google.com/mail/?view=cm&fs=1&to=abdoomostafa333@gmail.com)")
st.write("📞 **Phone**: [(+20) 111 204 5083](tel:+201112045083)")

st.write("---")
st.subheader("Connect with Us")
st.write("Stay updated by following us on social media:")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        '<a href="https://www.linkedin.com/in/abdoo-mostafa99/"><img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" style="width: 50px; height: 50px;" alt="LinkedIn"></a>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        '<a href="https://www.facebook.com/abdoorooney"><img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" style="width: 50px; height: 50px;" alt="Facebook"></a>',
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        '<a href="https://github.com/abdoomostafa99"><img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" style="width: 50px; height: 50px;" alt="GitHub"></a>',
        unsafe_allow_html=True
    )


st.write("---")
st.write("We look forward to hearing from you! For any urgent matters, please use the contact details above.")
