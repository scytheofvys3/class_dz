from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __repr__(self):
        return f'{self.nickname}. {self.password}, {self.age}'


class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title =  title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __repr__(self):
        return f'{self.title}'


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def __repr__(self):
        return f'{self.users}, {self.videos}, {self.current_user}'

    def log_in(self, nickname, password):
        pas = hash(password)
        for i in self.users:
            if nickname == i.nickname and pas == i.password:
                self.current_user = nickname
                print(f'Пользователь {nickname} вошел в аккаунт')

    def register(self, nickname, password, age):
        if any(p.nickname == nickname for p in self.users):
            print(f'Юзер {nickname} уже существует')
        else:
            obj = User(nickname, password, age)
            self.users.append(obj)
            self.current_user = nickname
            print(f'Пользователь {nickname} вошел в аккаунт')
            return self.users


    def log_out(self):
        self.current_user = None

    def add(self, *other):
        self.videos = [*other]

    def get_videos(self, other):
        value = other.lower()
        get_videos1 = []
        for x in self.videos:
            if value in x.title.lower():
                get_videos1.append(x.title)
        return get_videos1

    def watch_video(self, film):
        if not self.current_user:
            print('Войдите в аккаунт')
            return
        for i in self.videos:
            if film in i.title:
                for k in self.users:
                    if k.nickname == self.current_user and i.adult_mode:
                        if k.age < 18:
                            print(f'Вам нет 18 лет для просмотра видео "{i.title}"')
                            return
                print(f'Воспроизводится видео: {i.title}')
                for l in range(i.time_now, i.duration): #
                    sleep(1)
                    i.time_now += 1
                    print(f"Время: {i.time_now} сек")
                print(f'Конец видео')
                i.time_now = 0
                return
        print(f'Видео не найдено, повторите поиск')


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
ur.register('test_mou_test', 'dlgkokLKDFJo2354F', 14)
ur.watch_video('Для чего девушкам парень программист?')
# ur.watch_video('Лучший язык программирования 2024 года') # воспроизводится
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
print(ur.current_user)
# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')