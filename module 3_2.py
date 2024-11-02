def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if "@" not in recipient or "@" not in sender or not recipient.endswith(
            ('.com', '.ru', '.net')) or not sender.endswith(('.com', '.ru', '.net')):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    if recipient.lower() == sender.lower():
        print("Нельзя отправить письмо самому себе!")
        return

    if sender.lower() == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")


send_email("Hi, how are you?", "my_mail@gmail.com")
send_email("Hi, how are you?", "my_mail@gmail.com", sender = "my_pochta@mail.ru")
send_email("Hi, how are you", "Pochta_mail.ru",  sender = "my_mail@gmail.com")
send_email("Hi, how are you", "my_mail@gmail.com", sender = "my_mail@gmail.com")
