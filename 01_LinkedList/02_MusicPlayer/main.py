from library import Library
from playlist_manager import PlaylistManager

def manage_playlist_menu(playlist, pm: PlaylistManager):
    """Sub-menu that runs operations inside the selected playlist"""
    while True:
        print("\n==========================================")
        print(f"SELECTED PLAYLIST: {playlist.playlistname}")
        print("="*42)
        print("1. Display Playlist")
        print("2. Add Music to Playlist")
        print("3. Remove Music from Playlist")
        print("4. Change Track Position")
        print("5. Search Music in Playlist")
        print("6. Clear Playlist")
        print("7. Back to Main Menu")

        choice = input("\nEnter choice (1-7): ").strip()

        if choice == "1":
            playlist.display_playlist_tracks()

        elif choice == "2":
            try:
                track_id = int(input("Enter Track ID from library to add: "))

                pm.add_track_to_playlist(playlist.playlistname, track_id)
            except ValueError:
                print("Invalid Input. Track ID must be an integer")

        elif choice == "3":
            try:
                track_id = int(input("Enter Track ID from playlist to remove: "))

                pm.remove_track_from_playist(playlist.playlistname, track_id)
            except ValueError:
                print("Invalid Input. Track ID must be an integer")

        elif choice == "4":
            try:
                track_id = int(input("Enter Track ID to move: "))
                after_id = int(input("Enter target Track ID to place it after: "))

                pm.change_track_postion(playlist.playlistname, track_id, after_id)
            except ValueError:
                print("Invalid Input. Track IDs must be an integer")

        elif choice == "5":
            query = input("Search (Title or Artist): ")
            results = playlist.search_inside_playlist(query)
            if not results:
                print(f"No tracks found matching {query}")
            else:
                print(f"\n-----Search Results for {query}-----")
                print(
                    f"{'Title':<20}"
                    f"{'Artist':<20}"
                    f"{'Genre':<15}"
                    f"{'ID':<7}"
                )
                for node in results:
                    t = node.music
                    print(
                        f"{t.Title:<20}"
                        f"{t.Artist:<20}"
                        f"{t.Genre:<15}"
                        f"{t.Id:<7}"
                    )

        elif choice == "6":
            confirm = input(f"Are you sure you want to clear '{playlist.playlistname}'? (y/n): ")
            if confirm.lower() == "y":
                pm.clear_playlist(playlist.playlistname)

        elif choice == "7":
            print(f"Exiting playlist '{playlist.playlistname}' ")
            break
        else:
            print("Invalid choice. Please try again. ")

def main():
    library = Library()
    pm = PlaylistManager(library)

    while True:
        print("\n==========================================")
        print("         MUSIC PLAYLIST MANAGER           ")
        print("="*42)
        print("1. Create Playlist")
        print("2. Select/Open Playlist")
        print("3. Rename Playlist")
        print("4. Delete Playlist")
        print("5. List All Playlists")
        print("6. Exit")

        choice = input("\nEnter choice (1-6): ").strip()

        if choice == "1":
            name = input("Enter new Playlist name: ")
            pm.create_playlist(name)

        elif choice == "2":
            pm.list_playlists()
            name = input("\nEnter playlist name to open: ")
            #Get the playlist using get function of playlistmanager
            selected_playlist = pm.get_playlist(name)
            if selected_playlist:
                manage_playlist_menu(selected_playlist, pm)

        elif choice == "3":
            old_name = input("Enter Playlist name to rename: ")
            new_name = input("Enter new Playlist name: ")
            pm.rename_playlist(old_name, new_name)

        elif choice == "4":
            name = input("Enter Playlist name to delete: ")
            pm.delete_playlist(name)

        elif choice == "5":
            pm.list_playlists()

        elif choice == "6":
            print("GoodBye!")
            break

        else:
            print("Invalid Input. Please Enter 1-6")


if __name__ == "__main__":
    main()