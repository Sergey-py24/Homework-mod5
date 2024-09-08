import time

class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title

    def __contains__(self, item):
        return item in self.title


class WooTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_out(self):
        self.current_user = None

    def log_in(self, nickname: str, password: int):
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = user
                return

    def register(self, nickname: str, password: int, age: int):
        password = hash(password)
        for user in self.users:
            if nickname == user.nickname:
                print(f"Учетная запись {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Учетная запись {nickname} активирована.")

    def add(self, *args):
        for movie in args:
            if movie.title not in [video.title for video in self.videos]:
                self.videos.append(movie)

    def get_videos(self, text: str):
        list_movie = []
        for video in self.videos:
            if text.upper() in video.title.upper():
                list_movie.append(video.title)
        return list_movie

    def watch_video(self, movie: str):
        if self.current_user:
            for video in self.videos:
                if self.current_user and self.current_user.age < 18:
                    print('Контент для лиц старше 18 лет')
                    return
                if movie in video.title:
                    for i in range(1, 4):
                        print(i, end=' ')
                        time.sleep(3)
                        video.time_now += 1
                    video.time_now = 0
                    print('Финал')
        else:
            print('Войдите в учетную запись.')


if __name__ == '__main__':
    woo = WooTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Тили-тили-трали-вали', 10, adult_mode=True)

# Добавление видео
woo.add(v1, v2)

# Проверка поиска
print(woo.get_videos('лучший'))
print(woo.get_videos('ТИЛИ'))

# Проверка на вход пользователя и возрастное ограничение
woo.watch_video('Тили-тили-трали-вали')
woo.register('Иван_Иваныч', 'qwertyuiop', 13)
woo.watch_video('Тили-тили-трали-вали')
woo.register('Петр_Петрович', '1234asdfgHJKL', 25)
woo.watch_video('Тили-тили-трали-вали')

# Проверка входа в другой аккаунт
woo.register('Иван_Иваныч', '4321ZXCV', 55)
print(woo.current_user)

# Попытка воспроизведения несуществующего видео
woo.watch_video('Лучший язык 2024 года!')