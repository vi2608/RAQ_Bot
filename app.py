import streamlit as st
from src.retrieval_generation import generation
from src.data_ingestion import ingestdata
from dotenv import load_dotenv

load_dotenv()

vstore = ingestdata("None")
chain = generation(vstore)

def generate_response(user_input):
    return chain.invoke(user_input)

st.image("data:image/webp;base64,UklGRh4DAABXRUJQVlA4IBIDAAAwEQCdASo4ADgAPi0Ki0WhkNDNeBgCxLQAaPgMIpvZvxy543jTwBzFNa/4bpNeJt0pfMB+oHrLdIB+zPWQfsB7EHSo/uT6QGrmBdPt/47Luvz1vOfsDfqd/r+BV/YAouinVkQrOEfqThgU3pYXpPMin1WlgMPyWzbyQGXfztyRWOnc2IScwog03EM9En6SAAewwAD+//rkj6yPf85Z2Lc269c+c559v2A94a9n85FCPeY5MkipSz9d+1r5TrEg/+WWdxksodNhvP2QX1jugLoyG/YIdz06/WGqX69iPbB98Xm+sCLWO3cvLE1ZIQMF8IvQT8GodAgkw0rYLf034oJFT5/Uyy8vityU+Pxn9KTPl3ZqEMf+k0KXAFb4L3EiyLJYAiFgjuqhGJx70ya80vfekrHRKG8/wVg20ikYZIgkXOSG2j19OfB/399GcvH2QNp4uJmnfcuDMwEUSHND4AAHhvWzT//9eMo3juRZOP/T5ZRX+r5kua4QJEyuV++RPUxzOEenQaCyrD6vxbMvydh9WKPdc6DykMVb2jCi7odfKCpJtrckCqQBw/1A7++cqvp3MfoxHEZO12INHcHQmHcUYRIfYIxGjE86MR+hUrRx0/Gp/+jVl/vH9MUPbbj5/aMBALoENCfWdV+NJSMAZfc44djnjOsQexlv2P/Ay/9Ryn35mKflPJMwc3JvS57r1Sd3i62Xv3/kgs/l6Px1G61zxS4z9olZxQ6uaVef4rVab7Mf3x1X8DvVVW+/pDWSRr5w4h0MKKuv7otNVzlKGoYzgyYtL5gyB91+lR6Vgm2pNmFau/Ntev8QN4sMA2mC/lZ32n3zF/QNT/0ud0jF2faGrxaSLjXhoMghujPtg2GpfXL/gBn/rTpvkjFf610m+FuiiMBArrzYLYUPP0jF9lYQ3lv7k0TVcQelEX/+VL1q3pMPjscch5cStGIOninL5xt6AR7JsDA9yqaPYZ7i3f+NvNGCfeXcIP+i441BqXDxEPa6vt3r1a+/kaIbP5kbNYZY5EZWmwA6vCk3MXB5CAAAAAA=", width=300)

if 'conversation' not in st.session_state:
    st.session_state.conversation = []


st.title("Privacera QA Chatbot by Vipul Munot")
st.write("Ask me anything about Our Sucess Stories!!")

user_input = st.text_input("Type your message here...", "")

if user_input:
    
    response = generate_response(user_input)
    
    
    st.session_state.conversation.append({"user": user_input, "bot": response})


for message in st.session_state.conversation:
    st.write(f"**You:** {message['user']}")
    st.write(f"**Bot:** {message['bot']}")
