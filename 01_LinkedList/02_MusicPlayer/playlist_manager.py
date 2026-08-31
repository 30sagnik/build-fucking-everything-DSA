import json
from library import Library
from playlist import Playlist

class PlaylistManager:
    def __init__(self, library: Library, playlist_file = "playlists.json"):
        self.library = library
        self.playlist_file = playlist_file
        self.playlists = {}
        self.load_playlists()

    #CREATE PLAYLIST
    def create_playlist(self, name):
        if name in self.playlists:
            print(f"Playlist {name} already exists")
            return None
        new_playlist = Playlist(name)
        self.playlists[name] = new_playlist
        self.save_playlists()
        print(f"Playlist {name} created successfully")
        return new_playlist

    #RENAME PLAYLIST
    def rename_playlist(self, old_name, new_name):
        if old_name not in self.playlists:
            print(f"Playlist {old_name} not found")
            return False
        if new_name in self.playlists:
            print(f"A playlist already exits with this name {new_name}")
            return False
        pl = self.playlists.pop(old_name) #This removes the old_name and attaches the values assigned to it to pl
        pl.playlistname = new_name #This updates the internal name attribute of Playlist object to new_name
        self.playlists[new_name] = pl #This creates a new entry in self.playlists using new_name as the key
        self.save_playlists()
        print(f"Playlist renamed from {old_name} to {new_name}")
        return True

    #DELETE PLAYLIST
    def delete_playlist(self, name):
        if name not in self.playlists:
            print(f"Playlist {name} not found")
            return False
        del self.playlists[name]
        self.save_playlists()
        print(f"Playlist {name} deleted successfully")
        return True

    #GET PLAYLIST
    def get_playlist(self, name):
        playlist = self.playlists.get(name)
        if not playlist:
            print(f"Playlist {name} does not exist")
        return playlist

    #LIST OF PLAYLISTS
    def list_playlists(self):
        if not self.playlists:
            print("No Playlists available")
            return
        print("\n====== Available Playlists ======")
        print(
            f"{'Playlist Name':<20}"
            f"{'Tracks':<5}"
        )
        for name, playlist in self.playlists.items():
            print(
                f"{name:<20}"
                f"{playlist.count():<5}"
            )

    #-----Bridged Actions(Executes Playlist Actions)------

    #Add Track
    def add_track_to_playlist(self, playlist_name, track_id):
        playlist = self.get_playlist(playlist_name)
        if not playlist:
            return False
        music = self.library.get_track(track_id)
        if not music:
            print(f"Track ID {track_id} not found in the music library")
            return False
        playlist.add_music(music)
        self.save_playlists()
        return True

    #Remove Track
    def remove_track_from_playist(self, playlist_name, track_id):
        playlist = self.get_playlist(playlist_name)
        if not playlist:
            return False
        if playlist.remove_music(track_id):
            self.save_playlists()
            return True

    #Change position
    def change_track_postion(self, playlist_name, track_id, after_track_id):
        playlist = self.get_playlist(playlist_name)
        if not playlist:
            return False
        if playlist.change_position(track_id, after_track_id):
            self.save_playlists()
            return True
        return False

    #Clear playlist
    def clear_playlist(self, playlist_name):
        playlist = self.get_playlist(playlist_name)
        if not playlist:
            return False
        if playlist.clear():
            self.save_playlists()
            return True
        return False

    #------JSON Persistence------

    def save_playlists(self):
        data = {}
        for name, pl in self.playlists.items():
            data[name] = pl.get_track_ids()

        with open(self.playlist_file, "w") as file:
            json.dump(data, file, indent = 4)

    def load_playlists(self):
        try:
            with open(self.playlist_file, "r") as file:
                data = json.load(file)

            for name, track_ids in data.items(): #To loop through all Playlists
                pl = Playlist(name)
                for tid in track_ids: #To loop through all track_ids in the saved playlist
                    music = self.library.get_track(int(tid))
                    if music:
                        pl.add_music(music)
                self.playlists[name] = pl
        except FileNotFoundError:
            print("No existing 'playlists.json' found, Initializing Empty playlist manager")
        
