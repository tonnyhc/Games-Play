from enum import Enum

from django.core import validators, exceptions
from django.db import models


def username_is_allnum_validator(value):
    for ch in value:
        if not ch.isalnum() and ch != "_":
            raise exceptions.ValidationError('Ensure this value contains only letters, numbers, and underscore.')


class Profile(models.Model):
    MAX_USERNAME_LEN = 15
    MIN_USERNAME_LEN = 2

    username = models.CharField(
        max_length=MAX_USERNAME_LEN,
        null=False,
        blank=False,
        validators=[
            validators.MinLengthValidator(MIN_USERNAME_LEN),
            username_is_allnum_validator,
        ],
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True
    )

class ChoicesEnum(Enum):

    @classmethod
    def choices(cls):
        return ([x.name, x.value] for x in cls)


class AlbumGenres(ChoicesEnum):
    POP ="Pop Music"
    JAZZ ="Jazz Music"
    RNB = "R&B Music"
    ROCK = "Rock Music"
    COUNTRY = "Country Music"
    DANCE = "Dance Music"
    HIP_HOP = "Hip Hop Music"
    OTHER = "Other"


class Album(models.Model):
    MAX_LEN_NAME = 30
    MAX_LEN_ARTIST = 30
    MAX_LEN_GENRE = 30
    MIN_PRICE_VALUE = 0.0

    album_name = models.CharField(
        max_length=MAX_LEN_NAME,
        unique=True,
        null=False,
        blank=False,
        verbose_name="Album Name"
    )

    artist = models.CharField(
        max_length=MAX_LEN_ARTIST,
        null=False,
        blank=False
    )

    genre = models.CharField(
        max_length=MAX_LEN_GENRE,
        choices=AlbumGenres.choices()
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL'
    )

    price = models.FloatField(
        validators=(
            validators.MinValueValidator(MIN_PRICE_VALUE),
        ),
    null = False,
    blank = False,
    )
