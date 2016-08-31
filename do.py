import os
import pandas as pd

laptop_lib_path = u'/Users/partond/music_lib/iTunes 1/iTunes Media/Music'
external_hdd_lib_path = u'/Volumes/SamsungStory/music_lib'


def get_artist_albums(lib_path):
    artists = [artist for artist in os.listdir(lib_path) if len(artist) > 0 and artist[0] != '.']

    artist_albums = []

    for artist in artists:
        albums = os.listdir(os.path.join(lib_path, artist))
        for album in albums:
            dirpath = os.path.join(lib_path, artist, album)
            if len(album) > 0 and album[0] != '.':
                artist_albums.append((artist, album, dirpath))

    df = pd.DataFrame(
        index=pd.MultiIndex.from_tuples(artist_albums, names=['artist', 'album', 'dirpath'])
    ).reset_index()

    df['artist_l'] = df['artist'].apply(unicode.lower)
    df['album_l'] = df['album'].apply(unicode.lower)
    df.set_index(['artist_l', 'album_l'], inplace=True)

    return df


# dfl: df laptop
# dfe: df external hdd
dfl = get_artist_albums(laptop_lib_path)
dfe = get_artist_albums(external_hdd_lib_path)

print('=====================')
print('Laptop artist_albums not available on ext HDD')
print('=====================\n')

for i in dfl.index:
    if i not in dfe.index:
        print(i)

# print('=====================')
# print('Ext HDD artist_albums not available on laptop')
# print('=====================\n')

# for i in dfe.index:
#     if i not in dfl.index:
#         print(i)

# Now step through each of the laptop entries not available on ext HDD,
# to provide further info

for i in dfl.index:
    if i not in dfe.index:
        songs = os.listdir(dfl.loc[i].dirpath)
            print('')
        # TODO should prob show laptop albums for that artist, and ext albums for that artist
        # print(u'== {} - {} =='.format(dfl.loc[i].artist, dfl.loc[i].album))
        print('')
        print(u'\n'.join(songs))
        print(u'')
        raw_input('Type anything to continue...')

