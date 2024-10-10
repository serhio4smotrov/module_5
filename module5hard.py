from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for i in self.users:
            if i.nickname == nickname and i.password == hash(password):
                self.current_user = i
                return print('Авторизация пользователя прошла успешно')
        return print('Такого пользователя не существует')

    def register(self, nickname, password, age):
        for i in self.users:
            if i.nickname == nickname:
                return print(f'Пользователь {nickname} уже существует')
        self.users.append(User(nickname, password, age))
        self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            if i in self.videos:
                continue
            else:
                self.videos.append(i)

    def get_videos(self, name_search):
        name_list = []
        for i in self.videos:
            if name_search.lower() in i.title.lower():
                name_list.append(i.title)
        return name_list

    def watch_video(self, title):
        if self.current_user is None:
            return print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for i in self.videos:
                if i.title == title:
                    if i.adult_mode and self.current_user.age < 18:
                        return print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        for j in range(i.time_now, i.duration + 1):
                            print(j, end='  ')
                            sleep(1)
                        print('Конец видео')

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')