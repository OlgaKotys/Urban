import hashlib
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.age = age

    def __str__(self):
        return f"{self.nickname}, {self.age}"

    def __repr__(self):
        return f"User('{self.nickname}', '{self.age}')"

    def __eq__(self, other):
        return self.nickname == other.nickname and self.password == other.password

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return f"{self.title}, {self.duration}, {self.adult_mode}"

    def __repr__(self):
        return f"Video('{self.title}', {self.duration}, {self.adult_mode})"

    def reset_time(self):
        self.time_now = 0

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        for user in self.users:
            if user.nickname == nickname and user.password == password_hash:
                self.current_user = user
                return True
        return False

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, search_word):
        search_word = search_word.lower()
        return [video.title for video in self.videos if search_word in video.title.lower()]

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                print(f"Просмотр видео: {title}")
                for second in range(1, video.duration + 1):
                    time.sleep(1)
                    print(second, end=' ')
                    video.time_now = second
                print("Конец видео")
                video.reset_time()
                return
        print(f"Видео {title} не найдено")

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 10)
v2 = Video('Для чего парням девушка-программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего парням девушка-программист?')
ur.register('Игорёк', 'lolkekcheburek', 14)
ur.watch_video('Для чего парням девушка-программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего парням девушка-программист?')

ur.register('Игорёк', 'F8098FM8fjm9jmi', 43)
print(ur.current_user)

ur.watch_video('Лучший язык программирования 2024 года!')
