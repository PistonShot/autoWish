import telebot
import mysql.connector

bot = telebot.TeleBot('6161649236:AAG1Yzu57aJsYjb8lJPHwu3EuLxbuExmW4o')

cnx = mysql.connector.connect(
    # host='localhost',
    # user='root',
    # password='nanda123',
    # database='birthday_wisher'

    host='webproject-bwisher.mysql.database.azure.com',
    user='admin1',
    password='nanda123',
    database='birthday_wisher'
)

cursor = cnx.cursor()

# creates view
query = "CREATE OR REPLACE VIEW today_birthdays AS SELECT student.StudentID,student.name,YEAR(CURDATE())-YEAR(student.DOB) AS age , student.phoneNo, student_chatID.chatID FROM student JOIN student_chatID ON student.studentID = student_chatID.studentID WHERE DAY(student.DOB) = DAY(CURDATE()) AND MONTH(student.DOB) = MONTH(CURDATE())"
cursor.execute(query)

query = "SELECT * FROM today_birthdays"
cursor.execute(query)

rows = cursor.fetchall()
for row in rows:
    # TODO : remember to add here the bot sending message
    studentID = row[0]
    name = row[1]
    age = row[2]
    chatID = row[4]
    if chatID != None:

        photo_path = "./web_project/BirthdayPosterWeb.png"
        cake_emo = u'U+1F382'
        caption = f"Hello , {name}! Wishing you a very Happy Birthday \U0001F370!!!\nYou are {age} years old"
        image_url = 'https://cdn.pixabay.com/photo/2017/10/02/11/23/happy-birthday-2808536_1280.jpg'
        bot.send_photo(chat_id=chatID,photo=image_url,caption=caption)

    else :
        print(f"Setup is not complete for student ID = {studentID}")
        continue



        
cursor.close()
cnx.close()
