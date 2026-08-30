from music_node import MusicNode

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        self.size = 0

    def add_music(self, music):
        new_music = MusicNode(music)

        if self.head is None:
            self.head = new_music
            self.tail = new_music
            self.current = new_music

            new_music.next = new_music
            new_music.prev = new_music
            print("First Music Added to playlist")

        else:
            new_music.prev = self.tail
            new_music.next = self.head

            self.tail.next = new_music
            self.head.prev = new_music

            self.tail = new_music
            print("Music Added to playlist")

        self.size += 1

    def remove_music(self, music):
        #Empty LinkedList
        if self.head is None:
            return False
        #Only single node in the LL
        if self.head == self.tail:
            if self.head == music:
                self.head = None
                self.tail = None
                self.current = None
                self.size -= 1
                print("Music Deleted from Playlist")
                return True
            print("Music Not Found.")
            return False
        #When the head node is to be removed
        if self.head == music:
            if self.current == music:
                self.current = music.next
            self.head = self.head.next
            self.tail.next = self.head
            self.head.prev = self.tail
            self.size -= 1
            print("Music Deleted from Playlist")
            return True
        #Search for music
        current = self.head
        while current.next != self.head:
            if current.next == music:
                break
            current = current.next
        #Music not found in the LL
        if current.next != music:
            print("Music Not Found.")
            return False
        #Remove Node
        if self.current == music:
            self.current = music.next
        current.next = music.next
        music.next.prev = current
        #If music is in Tail node, then assign the second last Node as Tail for future
        if music == self.tail:
            self.tail = current
        self.size -= 1
        print("Music Deleted from Playlist")
        return True
                        

    def display_playlist(self):
        if self.head is None:
            print("Playlist is Empty")
            return
        current = self.head
        position = 1
        while True:
            print(
                f"{position}. "
                f"{current.music.Title} - "
                f"{current.music.Artist} - "
                f"{current.music.Genre} - "
                f"{current.music.Duration} "               
            )
            position += 1
            current = current.next
            if current == self.head:
                break

    def search(self, search):
        if self.head is None:
            print("Playlist is Empty")
            return
        current = self.head
        position = 1
        found = False
        while True:
            if search.lower() in current.music.Title.lower() or \
                search.lower() in current.music.Artist.lower():
                print(
                    f"{position}. "
                    f"{current.music.Title} - "
                    f"{current.music.Artist} - "
                    f"{current.music.Genre} - "
                    f"{current.music.Duration} "               
                )
                position += 1
                found = True
            current = current.next
            if current == self.head:
                break
        #found == False
        if not found:
            print("Search Item not found")

    def count(self):
        return self.size




        