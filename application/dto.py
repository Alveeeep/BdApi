from . import models


class MainPageBanner():
    id = models.MainPageBanner.id
    title = models.MainPageBanner.title
    description = models.MainPageBanner.description
    image_left = models.MainPageBanner.image_left
    image_right = models.MainPageBanner.image_right
    background_color = models.MainPageBanner.background_color


class Blog():
    id = models.Blog.id
    title = models.Blog.title
    description = models.Blog.description
    image = models.Blog.image
    date = models.Blog.date
    timezone = models.Blog.timezone


class Vacancies():
    id = models.Vacancies.id
    title = models.Vacancies.title
    phone_one = models.Vacancies.phone_one
    phone_two = models.Vacancies.phone_two
    email = models.Vacancies.email


class Phones():
    id = models.Phones.id
    phone = models.Phones.phone


class Objects():
    id = models.Objects.id
    icon = models.Objects.icon
    link = models.Objects.link


class Addresses():
    id = models.Addresses.id
    address = models.Addresses.address
