let body = document.querySelector('body')
let image_list = [
    'https://fs.kinomania.ru/image/file/film_wallpaper/e/5f/e5fbd281f43f85152ac3839cc292e22c.1366.768.jpeg',
    'https://wpapers.ru/wallpapers/films/16496/1366x768_%D0%9D%D0%B5%D1%83%D0%B4%D0%B5%D1%80%D0%B6%D0%B8%D0%BC%D1%8B%D0%B5-2.jpg'
]

body.style.background = `url(${image_list[Math.floor(Math.random() * image_list.length)]}) no-repeat`