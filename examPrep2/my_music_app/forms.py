from django import forms

from examPrep2.my_music_app.models import Profile, Album


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

class ProfileCreateForm(ProfileBaseForm):
    pass

class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._hide_input_fields()



    def _hide_input_fields(self):
        for _,field in self.fields.items():
            field.widget = forms.HiddenInput()


    def save(self, commit=True):
        if commit:
            Album.objects.all().delete()
            self.instance.delete()

        return self.instance



class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"

class AlbumCreateForm(AlbumBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['album_name'].widget.attrs['placeholder'] = 'Album Name'
        self.fields['artist'].widget.attrs['placeholder'] = 'Artist'
        self.fields['description'].widget.attrs['placeholder'] = 'Description'
        self.fields['image_url'].widget.attrs['placeholder'] = 'Image URL'
        self.fields['price'].widget.attrs['placeholder'] = 'Price'


class AlbumEditForm(AlbumBaseForm):
    pass

class AlbumDeleteForm(AlbumBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'