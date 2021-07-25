from tkinter import *
from tkinter import filedialog
import pygame
import time
from mutagen.mp3 import MP3


class mp3player:
    paused = False

    # Tkinter setup
    root = Tk()
    root.iconbitmap('icons/world.ico')
    root.title("*** Mp3 Player ***")
    root.geometry("500x300")

    # Initialize Pygame Mixer
    pygame.mixer.init()

    # Create Playlist Box
    songs_box = Listbox(root, bg="black", fg="orange", width=60, selectbackground="orange",
                        selectforeground="white")
    songs_box.pack(pady=20)

    # Create Control Frame
    controls_frame = Frame(root)
    controls_frame.pack()

    # Create Menu
    mp3menu = Menu(root)
    root.config(menu=mp3menu)

    # Create Status Bar
    # Status Bar
    status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=W)
    status_bar.pack(fill=X, side=BOTTOM, ipady=2)

    # Grab Song Length Time Info
    def play_time(self):
        cur_time = pygame.mixer.music.get_pos() // 1000
        conv_curr_time = time.strftime('%M:%S', time.gmtime(cur_time))

        # Get currently playing song
        cur_song = self.songs_box.curselection()
        song = self.songs_box.get(cur_song)
        song = f'audio/{song}.mp3'

        song_mut = MP3(song)
        song_length = song_mut.info.length
        conv_length = time.strftime('%M:%S', time.gmtime(song_length))

        self.status_bar.config(text=f'{conv_curr_time} of {conv_length}')
        self.status_bar.after(1000, self.play_time)

        if conv_curr_time == conv_length:
            self.next_song()

    def prev_song(self):
        prev_s = self.songs_box.curselection()
        prev_s = prev_s[0] - 1
        song = f'audio/{self.songs_box.get(prev_s)}.mp3'

        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

        self.songs_box.selection_clear(0, END)
        self.songs_box.activate(prev_s)
        self.songs_box.selection_set(prev_s, last=None)

    def next_song(self):
        next_s = self.songs_box.curselection()
        next_s = next_s[0] + 1
        song = f'audio/{self.songs_box.get(next_s)}.mp3'

        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

        self.songs_box.selection_clear(0, END)
        self.songs_box.activate(next_s)
        self.songs_box.selection_set(next_s, last=None)

    def play(self):
        if self.paused:
            self.paused = False
            pygame.mixer.music.unpause()
        else:
            song = self.songs_box.get(ACTIVE)
            song = f'audio/{song}.mp3'

            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops=0)

            self.play_time()

    def stop(self):
        pygame.mixer.music.stop()
        self.songs_box.selection_clear(ACTIVE)

    def pause(self):
        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
        else:
            pygame.mixer.music.pause()
            self.paused = True

    def add_song(self):
        song = filedialog.askopenfilename(initialdir='audio/', title="Choose a Song",
                                          filetypes=(("mp3 Files", "*.mp3"),))
        song = song.replace("PUT FILENAME HERE", "")
        song = song.replace('.mp3', "")

        self.songs_box.insert(END, song)

    def add_songs(self):
        songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose a Song",
                                            filetypes=(("mp3 Files", "*.mp3"),))

        for song in songs:
            song = song.replace("PUT FILENAME HERE", "")
            song = song.replace('.mp3', "")

            self.songs_box.insert(END, song)

    def del_song(self):
        self.songs_box.delete(ANCHOR)
        pygame.mixer.music.stop()

    def del_songs(self):
        self.songs_box.delete(0, END)
        pygame.mixer.music.stop()

    def __init__(self):

        # Define Images
        rewind_img = PhotoImage(file='icons/rewind.png')
        forward_img = PhotoImage(file='icons/fast-forward.png')
        play_img = PhotoImage(file='icons/play.png')
        pause_img = PhotoImage(file='icons/pause.png')
        stop_img = PhotoImage(file='icons/stop.png')

        # Make Buttons
        rewind_btn = Button(self.controls_frame, image=rewind_img, border=0, command=self.prev_song)
        forward_btn = Button(self.controls_frame, image=forward_img, border=0, command=self.next_song)
        play_btn = Button(self.controls_frame, image=play_img, border=0, command=self.play)
        stop_btn = Button(self.controls_frame, image=stop_img, border=0, command=self.stop)
        pause_btn = Button(self.controls_frame, image=pause_img, border=0, command=self.pause)

        rewind_btn.grid(row=0, column=0)
        forward_btn.grid(row=0, column=4)
        play_btn.grid(row=0, column=1)
        stop_btn.grid(row=0, column=3)
        pause_btn.grid(row=0, column=2)

        # Add Song Menu
        add_song_menu = Menu(self.mp3menu)
        self.mp3menu.add_cascade(label='Add Songs', menu=add_song_menu)
        add_song_menu.add_command(label='Add One Song to Playlist', command=self.add_song)
        add_song_menu.add_command(label='Add Songs to Playlist', command=self.add_songs)

        # Delete Song Menu
        del_song_menu = Menu(self.mp3menu)
        self.mp3menu.add_cascade(label='Delete Songs', menu=del_song_menu)
        del_song_menu.add_command(label='Delete a Song from Playlist', command=self.del_song)
        del_song_menu.add_command(label='Delete Songs from Playlist', command=self.del_songs)

        # Mainloop
        self.root.mainloop()


mp3player()
