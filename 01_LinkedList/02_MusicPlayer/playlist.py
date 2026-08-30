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
            print("First Music Added to playlist")

        else:
            new_music.prev = self.tail
            self.tail.next = new_music

            self.tail = new_music
            print("Music Added to playlist")

        self.size += 1

    def remove_music(self, music):
        #Empty LinkedList
        if self.head is None:
            print("Playlist is Empty")
            return False

        current = self.head
        while current is not None:
            if current.music == music:
                break
            current = current.next
        #When the item is not found
        if current is None:
            print("Item Not Found")
            return False
        #To shift the current playing music node if the music is to be removed
        if self.current == current:
            if current.next is not None:
                self.current = current.next
            else:
                self.current = current.prev
        #Remove from the beginning
        if current.prev is None:
            self.head = current.next
        else: 
            current.prev.next = current.next
        #Remove from the end
        if current.next is None:
            self.tail = current.prev
        else:
            current.next.prev = current.prev
        #Disconnect Node
        current.next = None
        current.prev = None

        self.size -= 1
        print("Music Deleted from Playlist")
        return True

    def display_playlist(self):
        if self.head is None:
            print("Playlist is Empty")
            return
        current = self.head
        position = 1
        while current is not None:
            print(
                f"{position}. "
                f"{current.music.Title} - "
                f"{current.music.Artist} - "
                f"{current.music.Genre} - "
                f"{current.music.Duration} "               
            )
            position += 1
            current = current.next

    def search(self, search):
        if self.head is None:
            return []
        current = self.head
        search_result = []
        while current is not None:
            if search.lower() in current.music.Title.lower() or \
                search.lower() in current.music.Artist.lower():
                search_result.append(current)
            current = current.next
        return search_result

    def change_position(self, music, after):
        if self.head is None:
            print("Playlist is Empty")
            return False
        music_node = self.head
        while music_node is not None:
            if music_node.music == music:
                break
            music_node = music_node.next
        if music_node is None:
            print("Music Not Found")
            return False
        after_node = self.head
        while after_node is not None:
            if after_node.music == after:
                break
            after_node = after_node.next
        if after_node is None:
            print("Taget music not found")
            return False
        if after_node == music_node:
            print("Music is alreaddy at target position")
            return False
        #Disconnect Head
        if music_node.prev is None:
            self.head = music_node.next
        else:
            music_node.prev.next = music_node.next
        #Disconnect Tail
        if music_node.next is None:
            self.tail = music_node.prev
        else:
            music_node.next.prev = music_node.prev
        #Connecting the Linked List
        music_node.prev = after_node
        music_node.next = after_node.next
        #after_node.next.prev = music_node //But condition given to point out the tail
        if after_node.next is not None:
            after_node.next.prev = music_node
        else:
            self.tail = music_node
        after_node.next = music_node
        print("Music position changed")
        return True

    def count(self):
        return self.size

    def clear(self):
        if self.head is None:
            print("Playlist is Empty")
            return False
        self.head = None
        self.tail = None
        self.current = None
        self.size = 0
        print("Playlist Cleared")
        return True    