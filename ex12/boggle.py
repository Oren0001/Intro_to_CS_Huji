import tkinter as tki
from boggle_board_randomizer import randomize_board
import tkinter.messagebox


def read_boggle_dic(filename):
    with open(filename) as file:
        for line in file:
            yield line.strip()
    yield "end of words"


class MyBoggle:
    BOARD_SIZE = 4
    REMAINING_TIME = "03:00"

    def __init__(self, root):
        root.geometry("590x535")
        root.configure(bg="lavender")
        self._root = root
        self._game_info = GameInfo(root)

        self._ltr_buttons = list()
        self._chosen_ltrs = str()
        self.create_board()

        game_btns_frame = tki.Frame(root)
        game_btns_frame.place(x=0, y=0)
        self.clickable = list()
        self._timer_updater = None
        self.create_play_btn(game_btns_frame)
        self.create_search_dict_btn(game_btns_frame)
        self.create_refresh_btn(game_btns_frame)
        self.create_new_game_btn(game_btns_frame)

        self.exit_img = tki.PhotoImage(file="exit button.png")
        exit_btn = tki.Button(root, image=self.exit_img, command=lambda: root.destroy())
        exit_btn.place(x=410, y=440)

    def create_board(self):
        board_frame = tki.Frame(self._root)
        board_frame.place(x=0, y=105)
        for ind in range(MyBoggle.BOARD_SIZE**2):
            row, column = ind // MyBoggle.BOARD_SIZE, ind % MyBoggle.BOARD_SIZE
            button = tki.Button(board_frame, text="?", height=3, width=6, bg="snow",
                                fg="MediumOrchid4", font=("Times", 16))
            self._ltr_buttons.append(button)
            button.grid(row=row, column=column)

    def create_play_btn(self, frame):
        self.play_button_img = tki.PhotoImage(file="play button.png")
        play_button = tki.Button(frame, image=self.play_button_img)
        play_button.bind("<Button-1>", self.play_btn_callback)
        play_button.grid(row=0, column=0)

    def play_btn_callback(self, play_btn_event):
        if self._game_info.get_timer().get() == MyBoggle.REMAINING_TIME:
            board = randomize_board()
            for button in self._ltr_buttons:
                button.configure(text=board[button.grid_info()["row"]][button.grid_info()["column"]])
                button.bind("<Button-1>", lambda event, btn=button: self.board_callback(event, btn))
            self.update_timer()

    def board_callback(self, event, btn):
        if btn["bg"] == "green2" and btn["text"].upper() == self._chosen_ltrs[-len(btn["text"]):]:
                btn.configure(bg="snow")
                self._chosen_ltrs = self._chosen_ltrs[:-len(btn["text"])]
                self.clickable.pop(-1)
        elif btn["bg"] == "snow":
            row, column = btn.grid_info()["row"], btn.grid_info()["column"]
            if self.clickable == list() or (row, column) in self.clickable[-1]:
                self._chosen_ltrs += btn["text"].upper()
                btn.configure(bg="green2")
                coordinates = list()
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        coordinates.append((row + i, column + j))
                self.clickable.append(coordinates)
        self._game_info.get_chosen_ltrs_label().configure(text=self._chosen_ltrs)

    def update_timer(self):
        m, s = map(int, self._game_info.get_timer().get().split(":"))
        if s == 0 and m > 0:
            m -= 1
            s = 59
        elif s > 0:
            s -= 1
        self._game_info.get_timer().set(f"0{m}:{s}" if s > 9 else f"0{m}:0{s}")
        if s == 0 and m == 0:
            self.game_over_msg()
            return
        self._timer_updater = self._root.after(1000, self.update_timer)

    def game_over_msg(self):
        end_msg = tki.messagebox.askyesno(title="Game Over",
                                          message="Time is up. Would you like to play again?")
        if end_msg == tki.YES:
            self.reset_game()
        else:
            self._root.destroy()

    def create_search_dict_btn(self, frame):
        self.search_dict_img = tki.PhotoImage(file="search dict button.png")
        search_dict_btn = tki.Button(frame, image=self.search_dict_img)
        search_dict_btn.bind("<Button-1>", self.search_dict_btn_callback)
        search_dict_btn.grid(row=0, column=1)

    def search_dict_btn_callback(self, event):
        if not self._timer_updater:
            return
        elif self._chosen_ltrs in self._game_info.get_list_box().get(0, tki.END):
            self.thumbs_img = tki.PhotoImage(file="double check img.png")
            self.display_answer(self.thumbs_img)
        else:
            for word in read_boggle_dic("boggle_dict.txt"):
                if word == self._chosen_ltrs:
                    score = int(self._game_info.get_score()["text"]) + len(self._chosen_ltrs) ** 2
                    self._game_info.get_score().configure(text=str(score))
                    self.correct_img = tki.PhotoImage(file="correct img.png")
                    self.display_answer(self.correct_img)
                    self._game_info.get_list_box().insert(tki.END, word)
                    break
                elif word == "end of words":
                    self.wrong_img = tki.PhotoImage(file="wrong img.png")
                    self.display_answer(self.wrong_img)
        self._chosen_ltrs = str()
        self._game_info.get_chosen_ltrs_label()["text"] = self._chosen_ltrs

    def display_answer(self, img):
        img_label = tki.Label(self._root, image=img)
        img_label.place(x=220, y=220)
        img_label.after(1000, img_label.place_forget)
        for ltr_btn in self._ltr_buttons:
            ltr_btn.configure(bg="snow")
        self._chosen_ltrs = str()
        self.clickable = list()

    def create_refresh_btn(self, frame):
        self.refresh_img = tki.PhotoImage(file="refresh button.png")
        refresh_btn = tki.Button(frame, image=self.refresh_img)
        refresh_btn.bind("<Button-1>", self.refresh_game)
        refresh_btn.grid(row=0, column=3)

    def refresh_game(self, event):
        board = randomize_board()
        for button in self._ltr_buttons:
            button.configure(text=board[button.grid_info()["row"]][button.grid_info()["column"]], bg="snow")
        self.clickable = list()
        self._chosen_ltrs = str()
        self._game_info.get_chosen_ltrs_label()["text"] = self._chosen_ltrs

    def create_new_game_btn(self, frame):
        self.new_img = tki.PhotoImage(file="new game button.png")
        new_btn = tki.Button(frame, image=self.new_img)
        new_btn.bind("<Button-1>", self.reset_game)
        new_btn.grid(row=0, column=4)

    def reset_game(self, event=None):
        if self._timer_updater:
            self._root.after_cancel(self._timer_updater)
            self._game_info.get_timer().set(MyBoggle.REMAINING_TIME)
            self._game_info.get_score().configure(text="0")
            self._chosen_ltrs = str()
            self._game_info.get_chosen_ltrs_label()["text"] = self._chosen_ltrs
            for ltr in self._ltr_buttons:
                ltr.configure(text="?", bg="snow")
            self.clickable = list()
            self._game_info.get_list_box().delete(0, tki.END)


class GameInfo:
    def __init__(self, root):
        self._root = root

        self._timer = tki.StringVar()
        self._timer_entry = None
        self._score = None
        self.create_info()

        right_frame = tki.Frame(root, bg="lavender")
        right_frame.place(x=350, y=105)
        self._chosen_ltrs_label = tki.Label(right_frame, bg="snow", font=("Times", 20),
                                            fg="MediumOrchid4", width=15)
        self.display_chosen_ltrs(right_frame)
        self.list_box = tki.Listbox(right_frame, height=7, width=22, font=("Times", 15), fg="MediumOrchid4")
        self.display_correct_words(right_frame)

    def get_timer(self):
        return self._timer

    def get_timer_entry(self):
        return self._timer_entry

    def get_score(self):
        return self._score

    def get_chosen_ltrs_label(self):
        return self._chosen_ltrs_label

    def get_list_box(self):
        return self.list_box

    def create_info(self):
        info_frame = tki.Frame(self._root, bg="lavender")
        info_frame.place(x=0, y=475)
        timer_title = tki.Label(info_frame, text="Timer", font=("Times", 20), fg="navy", bg="lavender")
        timer_title.grid(row=0, column=0)
        self._timer.set(MyBoggle.REMAINING_TIME)
        self._timer_entry = tki.Entry(info_frame, textvariable=self._timer, width=5,
                                      fg="MediumOrchid4", font=("Times", 25))
        self._timer_entry.grid(row=0, column=1)
        separator = tki.Label(info_frame, width=2, bg="lavender")
        separator.grid(row=0, column=2)
        score_title = tki.Label(info_frame, text="Score", font=("Times", 20), fg="navy", bg="lavender")
        score_title.grid(row=0, column=3)
        self._score = tki.Label(info_frame, width=4, bg="snow", text="0",
                                font=("Times", 25), fg="MediumOrchid4")
        self._score.grid(row=0, column=4)

    def display_chosen_ltrs(self, frame):
        chosen_ltrs_title = tki.Label(frame, text="Chosen letters", font=("Times", 20),
                                      fg="navy", bg="lavender")
        chosen_ltrs_title.pack()
        self._chosen_ltrs_label.pack()
        separator = tki.Label(frame, height=1, bg="lavender")
        separator.pack()

    def display_correct_words(self, frame):
        correct_words_title = tki.Label(frame, text="Correct words", font=("Times", 20),
                                        fg="navy", bg="lavender")
        correct_words_title.pack()
        scroll = tki.Scrollbar(self.list_box, command=self.list_box.yview)
        scroll.pack(side=tki.RIGHT, fill="y")
        self.list_box.configure(yscrollcommand=scroll.set)
        self.list_box.pack(side=tki.LEFT)
        self.list_box.pack_propagate(tki.FALSE)


if __name__ == "__main__":
    root = tki.Tk()
    MyBoggle(root)
    root.mainloop()
