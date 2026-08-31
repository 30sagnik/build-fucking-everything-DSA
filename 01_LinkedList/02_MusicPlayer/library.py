from music import Music

class Library:
    def __init__(self):
        self.tracks = {}
        self.next_ID = 1000

    #Add Music track to library
    def add_track(self):
        Title = input("Enter Music Title: ")
        Artist = input("Enter Artist name: ")
        Genre = input("Enter Genre: ")
        Duration = int(input("Duration(in seconds): "))
        FilePath = input("Add FilePath: ")

        #Check duplicate Title + Artist
        for track in self.tracks.values():
            if (track.Title.lower() == Title.lower()
                and track.Artist.lower() == Artist.lower()):
                print("\nThis Music track already exists in the library")
                print("Track Not Added")
                return False

        #Automatically generate ID
        track_id = self.next_ID
        music = Music(
            track_id,
            Title,
            Artist,
            Genre,
            Duration,
            FilePath
        )

        self.tracks[track_id] = music
        self.next_ID += 1

        print("\nSong added successfully")
        print("ID: ", music.Id)
        print("Title: ", music.Title)
        print("Artist: ", music.Artist)

        return True

    #To get the track_id
    def get_track(self, track_id):
        return self.tracks.get(track_id)
    
    #To check whether the track_id exists or not in the library
    def contains_track(self, track_id):
        return track_id in self.tracks

    #Search track & artist in the library
    def search(self, query):
        results = []
        query = query.lower()
        for track in self.tracks.values():
            if (query in track.Title.lower() or
                query in track.Artist.lower()):
                results.append(track)
        return results

    #Remove music track from library
    def remove_track(self):
        track_id = int(input("Enter track ID to delete: "))
        if not self.contains_track(track_id):
            print("Music Track not found")
            return False
        track = self.get_track(track_id)

        del self.tracks[track_id]
        print(f"Removed: {track.Title} - {track.Artist}")
        return True

    #Display the Library
    def display_library(self):
        print(
            f"{'Title':<20}"
            f"{'Artist':<20}"
            f"{'Genre':<15}"
            f"{'Id':<7}"
            )
        print("-"*62)
        for track in self.tracks.values():
            print(
                f"{track.Title:<20}"
                f"{track.Artist:<20}"
                f"{track.Genre:<15}"
                f"{track.Id:<7}"
                )

if __name__ == "__main__":
    library = Library()

    library.add_track()
    library.add_track()
    library.add_track()

    library.display_library()

    results = library.search("Ar")
    if not results:
        print("No tracks found")
    else:
        print("\nSearch Results")
        for track in results:
            print(
                f"{track.Title:<20}"
                f"{track.Artist:<20}"
                f"{track.Genre:<15}"
                f"{track.Id:<7}"
                )

    get = library.get_track(1001)
    print(get.Title)

    library.display_library()

    library.remove_track()

    library.display_library()

    




