import streamlit as st
from PIL import Image
new_title = '<p style="font-family:century gothic; color:Blue; font-size: 42px;">We will tell you your spirit animal based on your favorite foods</p>'
st.markdown(new_title, unsafe_allow_html=True)


#Pick the breakfast

option=bf=st.selectbox(
    'Pick your breakfast',
    ('None','Waffles', 'Pancakes','Cereal','Bagel',))
if bf=='Waffles':
    image=Image.open('pictures/waffles.jpg')
    st.image(image, caption='Waffles')
elif bf=='Pancakes':
    image=Image.open('pictures/pancakes.jpg')
    st.image(image, caption='Pancakes')
elif bf=='Cereal':
    image=Image.open('pictures/cereal.jpg')
    st.image(image, caption='Cereal')
elif bf=='Bagel':
    image=Image.open('pictures/bagel.jpg')
    st.image(image, caption='Bagel')
elif bf=='None':
    st.write('Please select a food')
st.write('----------------------------------------------------------------------------------')

#Pick the Lunch

option=lunch=st.selectbox(
    'Pick your lunch' ,
    ('None', 'Pasta', 'Pizza', 'Sushi','Burger'))
if lunch=='Pasta':
    image=Image.open('pictures/pasta.jpg')
    st.image(image, caption='Pasta')
elif lunch=='Pizza':
    image=Image.open('pictures/pizza.jpg')
    st.image(image, caption='Pizza')
elif lunch=='Sushi':
    image=Image.open('pictures/sushi.jpg')
    st.image(image, caption='Sushi')
elif lunch=='Burger':
    image=Image.open('pictures/burger.jpg')
    st.image(image, caption='Burger')
elif lunch=='None':
    st.write("Please select a food")
st.write('----------------------------------------------------------------------------------')


#Pick the dinner

option=din=st.selectbox(
    'Pick your dinner',
    ('None','Steak', 'Fried Rice', 'Fried Chicken','Soup'))
if din=='Steak':
    image=Image.open('pictures/steak.jpg')
    st.image(image, caption='Steak')
elif din=='Fried Rice':
    image=Image.open('pictures/rice.jpg')
    st.image(image, caption='Fried Rice')
elif din=='Fried Chicken':
    image=Image.open('pictures/chicken.jpg')
    st.image(image, caption='Fried Chicken')
elif din=='Soup':
    image=Image.open('pictures/soup.jpg')
    st.image(image, caption='Soup')
elif din=='None':
    st.write("Please select a food")
st.write('----------------------------------------------------------------------------------')

#pick the desert

option=des=st.selectbox(
    'Pick your desert',
    ('None','Chocolate Cake', 'Ice cream', 'Cookies','Chocolate'))
if des=='Chocolate Cake':
    image=Image.open('pictures/cake.jpg')
    st.image(image, caption='Chocolate Cake')
elif des=='Ice cream':
    image=Image.open('pictures/ice cream.jpg')
    st.image(image, caption='Ice cream')
elif des=='Cookies':
    image=Image.open('pictures/cookie.jpg')
    st.image(image, caption='Cookies')
elif des=='Chocolate':
    image=Image.open('pictures/choco.jpg')
    st.image(image, caption='Chocolate')
elif des=='None':
    st.write("Please select a food")
st.write('----------------------------------------------------------------------------------')

#pick the drink

option=drink=st.selectbox(
    'Pick your drink',
    ('None','Water', 'Soda', 'Juice','Milk'))
if drink=='Water':
    image=Image.open('pictures/water.jpg')
    st.image(image, caption='Water')
elif drink=='Soda':
    image=Image.open('pictures/soda.jpg')
    st.image(image, caption='Soda')
elif drink=='Juice':
    image=Image.open('pictures/juice.jpg')
    st.image(image, caption='Juice')
elif drink=='Milk':
    image=Image.open('pictures/milk.jpg')
    st.image(image, caption='Milk')
elif drink=='None':
    st.write("Please select a drink")
st.write('----------------------------------------------------------------------------------')

#what is the spirit animal

if bf=='Waffles' and lunch=='Pasta' and din=='Steak' and des=='Chocolate Cake' and drink=='Water':
    st.write('Your spirit animal is:')
    st.write('A horse' , 'You are very strong, but sometimes you can be shy and quiet')
    image=Image.open('pictures/horse.jpg')
    st.image(image, caption='Horse')

elif bf=='Pancakes' and lunch=='Pizza' and din=='Fried Rice' and des=='Ice cream' and drink=='Soda':
    st.write('Your spirit animal is:')
    st.write('A cat.' , 'You are very quiet and kind.')
    image=Image.open('pictures/cat.jpg')
    st.image(image, caption='Cat')

elif bf=='Cereal' and lunch=='Sushi' and din=='Fried Chicken' and des=='Cookies' and drink=='Juice':
    st.write('Your spirit animal is:')
    st.write('A monkey.' , 'You are very active, crazy, and happy.')
    image=Image.open('pictures/monkey.jpg')
    st.image(image, caption='Monkey')

elif bf=='Bagel' and lunch=='Burger' and din=='Soup' and des=='Chocolate' and drink=='Milk':
    st.write('Your spirit animal is:')
    st.write('A frog.' , 'You are very bright and cheerful.')
    image=Image.open('pictures/frog.jpg')
    st.image(image, caption='Frog')

elif bf=='Bagel' and lunch=='Pizza' and din=='Fried Rice' and des=='Ice cream' and drink=='Water':
    st.write('Your spirit animal is:')
    st.write('A tiger.' , 'You are very powerful and strong.')
    image=Image.open('pictures/tiger.jpg')
    st.image(image, caption='Tiger')

elif bf=='Pancakes' and lunch=='Sushi' and din=='Soup' and des=='Chocolate Cake' and drink=='Water':
    st.write('Your spirit animal is:')
    st.write('A fox.' , 'You are very sly and intelligent.')
    image=Image.open('pictures/fox.jpg')
    st.image(image, caption='Fox')

elif bf=='Waffles' and lunch=='Pasta' and din=='Fried Rice' and des=='Chocolate Cake' and drink=='Water':
    st.write('Your spirit animal is:')
    st.write('A deer.' , 'You are very quiet and gentil.')
    image=Image.open('pictures/deer.jpg')
    st.image(image, caption='Deer')

elif bf=='None' and lunch=='None' and din=='None' and des=='None' and drink=='None':
    st.write('Please input your answers')

else:
    st.write('Your spirit animal is:')
    st.write('A lion.', 'You are very strong and intelligent')
    image=Image.open('pictures/lion.jpg')
    st.image(image, caption='Lion')
