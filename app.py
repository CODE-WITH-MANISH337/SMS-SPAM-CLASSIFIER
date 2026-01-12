import streamlit as st
import nltk as nk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import string 
import pickle
nk.download('punkt')
nk.download('stopwords')

tfidf=pickle.load(open('vectorizer.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))


st.title('Sms Spam Clssifier')
input_sms=st.text_input('Enter message')


# preprocessing
def transform(text):
    text=text.lower()
    text=nk.word_tokenize(text)
    y=[]
    for i in text:
        if i.isalnum():
            y.append(i)
    text=y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text=y[:]
    y.clear()
    for i in text:
        y.append(PorterStemmer().stem(i))
    return ' '.join(y)

if st.button('Predict'):
    result=model.predict(tfidf.transform([transform(input_sms)]))[0]


   


    if result==1:
        st.success('SPAM')

    else:
        st.success('HAm') 
st.markdown("Check out the app's [GitHub repository](https://github.com/CODE-WITH-MANISH337/SMS-SPAM-HAM-CLASSIFIER)")           