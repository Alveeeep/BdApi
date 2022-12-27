from . import models


class MainPageBanner():
    main_model = models.MainPageBanner
    id = main_model.id
    title = main_model.title
    description = main_model.description
    image_left = main_model.image_left
    image_right = main_model.image_right
    background_color = main_model.background_color


class Blog():
    main_model = models.Blog
    id = main_model.id
    title = main_model.title
    description = main_model.description
    image = main_model.image
    date = main_model.date
    timezone = main_model.timezone


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
