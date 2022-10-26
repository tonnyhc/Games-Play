from django.shortcuts import render, redirect

from examPrep2.my_music_app.forms import ProfileCreateForm, AlbumCreateForm, AlbumEditForm, AlbumDeleteForm, \
    ProfileDeleteForm
from examPrep2.my_music_app.models import Profile, Album


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    profile = get_profile()
    if profile is None:
        return add_profile(request)
    context = {
        'profile': profile,
        'albums': Album.objects.all()
    }
    return render(request, 'common/home-with-profile.html', context=context)


def add_album(request):
    if request.method == "POST":
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home page")
    form = AlbumCreateForm()
    context = {'form': form}
    return render(request, 'album/add-album.html', context=context)


def details_album(request, pk):
    album = Album.objects.filter(pk=pk) \
        .get()
    context = {
        'album': album,
    }
    return render(request, 'album/album-details.html', context=context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == "POST":
        form = AlbumEditForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')
    form = AlbumEditForm(instance=album)
    context = {
        'form': form,
        'album': album
    }
    return render(request, 'album/edit-album.html', context=context)


def delete_album(request, pk):
    album = Album.objects \
        .filter(pk=pk) \
        .get()

    if request.method == 'GET':
        form = AlbumDeleteForm(instance=album)
    else:
        # Album.objects.filter(pk=pk).delete() # Don't do this!
        # Do it in the `form`
        form = AlbumDeleteForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'album': album,
    }

    return render(
        request,
        'album/delete-album.html',
        context,
    )


def add_profile(request):
    if get_profile() is not None:
        return redirect('index')

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'hide_nav_links': True,
    }

    return render(
        request,
        'common/home-no-profile.html',
        context,
    )


def details_profile(request):
    profile = Profile.objects.get()
    albums = Album.objects.all()
    context = {
        'profile': profile,
        'albums_count': len(albums),

    }
    return render(request, 'profile/profile-details.html', context=context)


def delete_profile(request):
    profile = get_profile()
    if request.method == "POST":
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')

    form = ProfileDeleteForm(instance=profile)
    context = {
        'form': form,
    }
    return render(
        request,
        'profile/profile-delete.html',
        context
    )
