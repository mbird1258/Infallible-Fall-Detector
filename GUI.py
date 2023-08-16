import PySimpleGUI as sg
# import cv2
import FallDetection as FD

WIDTH, LENGTH = 1000, 500
DARK_GREEN = '#182C1C'
LIGHTER_DARK_GREEN = "#1C3221"
UNDERLINED_FONT = ("Helvetica", 11, "underline")
NAME = "Ascensional"
current_lang = 0  # 0=eng, 1=chi
users = [['user', 'User1234', [12345678], [150, 30]]]

path_to_file_location = r"/Users/ ... /" #edit upon downloading code


# ---------------------used every page-------------------------
settings_layout = [[sg.Button(["Language", "語文"][current_lang], k="lang"), sg.Button(["Menu", "選單"][current_lang], k="menu")]]


# ------------------------login page---------------------------
col1 = [[sg.Text(["Don't have an account?", "沒有帳戶？"][current_lang])],
        [sg.Button(["Sign up", "創建你的帳號"][current_lang], font=UNDERLINED_FONT, k="sign up")]]
col2 = [[sg.Text(["email: ", "帳號名稱"][current_lang])],
        [sg.Input(k="email")],
        [sg.Text(["Password: ", "密碼"][current_lang])],
        [sg.Input(k="pw", password_char="*")],
        [sg.Button(["Login", "登錄"][current_lang], k="login")],
        [sg.Button(["Contact Us", "聯絡我們"][current_lang], font=UNDERLINED_FONT)]]
login_layout = [[sg.Column(layout=col1), sg.Text(["Sign In", "登入"][current_lang], p=(int(WIDTH/4), 0), font=UNDERLINED_FONT)],
                [sg.Column(col2, background_color=DARK_GREEN, justification="center")]]
# sg.Image("icon.png", size=(WIDTH//3, int(WIDTH*291.49/427/3))),

# ------------------------get home page after login--------------------


# ----------------------------Sign up page (1)-------------------------------
col6 = [[sg.Text("Already have an account?")], [sg.Button("Sign in", font=UNDERLINED_FONT, k="sign in")]]
col15 = [[sg.Column(col6), sg.Text("Sign Up", p=(int(WIDTH/4), 0), font=UNDERLINED_FONT)]]
col7 = [[sg.Text("email: ")],
        [sg.Input(k="new email")],
        [sg.Text("Password: ", )],
        [sg.Input(k="new pw", password_char="*")],
        [sg.Text("Re-enter your password:")],
        [sg.Input(k="new pw2", password_char="*")],
        [sg.Button("Continue", k="continue")],
        [sg.Button("Contact Us", font=UNDERLINED_FONT)]]
SignUpPage_layout = [[sg.Column(col7)]]


# -----------------------------Sign up page 2--------------------------------
col8 = [[sg.Text("Confirmation code:")],
        [sg.Input(k="confirmation code")],
        [sg.Button("Resend confirmation code", font=UNDERLINED_FONT)]]
col9 = [[sg.Button("Back", k="back", p=(int(WIDTH/46.857), 0)), sg.Button("Sign Up", k="confirm 2to3", p=(int(WIDTH/46.857), 0))]]
SignUpConfirmEmail_layout = [[sg.Text("We have sent a confirmation code to itsxxxxxxxxx@gmail.com")],
                             [sg.Column(col8)],
                             [sg.Column(col9)]]

# -----------------------------Sign up page 3--------------------------------
col3 = [[sg.Text(["Get Started", "開始"][current_lang], font=UNDERLINED_FONT, p=(int(WIDTH * 0.4), 0))]]
col4 = [[sg.Text(["Activate Your Product", "啟動你的產品"][current_lang])],
        [sg.Text(["Product code: ", "產品編碼："][current_lang]), sg.Input(k="product_code")]]
col5 = [[sg.Button(["Back", "返回"][current_lang], k="back2", p=(int(WIDTH/46.857), 0)),
         sg.Button(["Skip", "跳過"][current_lang], k="skip/next", p=(int(WIDTH/46.857), 0))]]
SignUpSetProductCode_layout = [[sg.Column(col4, background_color=LIGHTER_DARK_GREEN, justification="center")],
                               [sg.Column(col5, background_color=LIGHTER_DARK_GREEN, justification="center")]]


# -----------------------------Sign up page 4---------------------------------
SignUpCamAccess_layout = [[sg.Text(["We now need access to your camera. ", "首先，我們需要相機的權限"][current_lang])],
                          [sg.Text(["We need it for detection and recording. ", "我們需要它來檢測和記錄"][current_lang])],
                          #[sg.Image("cam.png")],
                          [sg.Button(["Allow", "允許"][current_lang], s=(WIDTH//5, 0), p=(int(WIDTH*0.3), 0))],
                          [sg.Button(["Back", "返回"][current_lang], k="back3")]]

# -----------------------------Sign up page 5--------------------------------
contact_input_list = ["0", "0"]
col11 = [[sg.Text(["Emergency Number 1", "緊急聯絡人電話 1"][current_lang], k="Emergency Number 1")],
         [sg.Input(k="emergency number 1")],
         [sg.Text(["Emergency Number 2", "緊急聯絡人電話 2"][current_lang], k="Emergency Number 2")],
         [sg.Input(k="emergency number 2")],
         [sg.Text(["Emergency Number 3", "緊急聯絡人電話 3"][current_lang], k="Emergency Number 3", visible=False)],
         [sg.Input(k="emergency number 3", visible=False)],
         [sg.Text(["Emergency Number 4", "緊急聯絡人電話 4"][current_lang], k="Emergency Number 4", visible=False)],
         [sg.Input(k="emergency number 4", visible=False)],
         [sg.Text(["Emergency Number 5", "緊急聯絡人電話 5"][current_lang], k="Emergency Number 5", visible=False)],
         [sg.Input(k="emergency number 5", visible=False)]]
col12 = [[sg.Button(["Back", "返回"][current_lang], k="back4", p=(int(WIDTH/46.857), 0)), sg.Button("Next", k="next", p=(int(WIDTH/46.857), 0))]]
col10 = [[sg.Text(["We need somebody to alert in case of danger", "當有危險時，我們需要通知那些聯絡人？"][current_lang])],
         [sg.Text(["Please insert the phone number of the individuals.", "請填寫他們的電話號碼"][current_lang])],
         [sg.Column(col11, background_color=LIGHTER_DARK_GREEN, justification="center")],
         [sg.Column(col12, background_color=LIGHTER_DARK_GREEN, justification="center")]]
SignUpEmergencyContacts_layout = [[sg.Text(["Then, we need to know who to call.", "設立你的聯絡人"][current_lang])],
                                  [sg.Column(col10, background_color=LIGHTER_DARK_GREEN, justification="center")]]


# -----------------------------Sign up page 6--------------------------------
col13 = [[sg.Text(["We need this information to more accurately detect falls", "為了更準確的偵測，我們需要更多的資訊"][current_lang])],
         [sg.Text(["Height of the person (cm):", "身高（厘米）"][current_lang]), sg.Input(k="height")],
         [sg.Text(["Shoulder width of the person (cm):", "肩寛（厘米）"][current_lang]), sg.Input(k="shoulder_width")]]
col14 = [[sg.Button(["Back", "返回"][current_lang], k="back5", p=(int(WIDTH/46.857), 0)),
          sg.Button(["Finish", "完成"][current_lang], k="finish_signup", p=(int(WIDTH/46.857), 0))]]
SignUpBodyInfo_layout = [[sg.Text(["Next, we need the person's height and shoulder width", "然後，我們需要他的身高和肩寛"][current_lang])],
                         [sg.Column(col13, background_color=LIGHTER_DARK_GREEN, justification="center")],
                         [sg.Column(col14, background_color=LIGHTER_DARK_GREEN, justification="center")]]


# -----------------------------Home page (7)---------------------------------
Home_layout = [[sg.Button("View the camera", k="view_cam")],
               [sg.Button(f"Test for sound: {FD.test_sound}", k="sound_test")],
               [sg.Button("Falling history", k="history")]]


# -----------------------------History (9)---------------------------------
History_layout = [[sg.Text("", k="fall_history_display")],
                [sg.Button("Clear History", k="clear_history"), sg.Button("Back", k="back")]]


# ---------------------------------------------------------------------------
v_layout = [[sg.Column(settings_layout)],
            [sg.Column(col3, k="col3", justification="left", visible=False),
            sg.Column(col15, k="col15", justification="left", visible=False)],
            [sg.Column(login_layout, k="login_layout", justification="center"),
             sg.Column(SignUpPage_layout, k="signup_layout1", visible=False, justification="center"),
             sg.Column(SignUpConfirmEmail_layout, k="signup_layout2", visible=False, justification="center"),
             sg.Column(SignUpSetProductCode_layout, k="signup_layout3", visible=False, justification="center"),
             sg.Column(SignUpCamAccess_layout, k="signup_layout4", visible=False, justification="center"),
             sg.Column(SignUpEmergencyContacts_layout, k="signup_layout5", visible=False, justification="center"),
             sg.Column(SignUpBodyInfo_layout, k="signup_layout6", visible=False, justification="center"),
             sg.Column(Home_layout, k="home_layout", visible=False, justification="center"),
             sg.Column(History_layout, k="history_layout",  visible=False, justification="center")],
            [sg.Column([[sg.Text("", k="txtshow_signup_step")]], k="colshow_signup_step", visible=False, justification="right")],
            [sg.Column([[sg.Image(filename=path_to_file_location + r"icon.png")]], justification="right", vertical_alignment='bottom', background_color=DARK_GREEN), [sg.Column([[]], expand_y=True, background_color=DARK_GREEN)]]]
window = sg.Window(NAME, v_layout, background_color=DARK_GREEN, size=(WIDTH, LENGTH))
signup_step = 0



def goto_signup_page():
    global signup_step
    print("going to sign up page...")
    window["col15"].update(visible=True)
    window["login_layout"].update(visible=False)
    window["signup_layout1"].update(visible=True)
    signup_step = 1
    print("you can sign up now")


def goto_login_page():
    global signup_step
    print("going to sign in(login) page...")
    window["signup_layout1"].update(visible=False)
    window["login_layout"].update(visible=True)
    window["col15"].update(visible=False)
    signup_step = 0
    print("you can sign in(login) now")


def signup_1to2(email, pw, pw2):
    global signup_step
    if len(email) == 0:
        print("please enter your email")
    elif pw == pw2:
        print("passwords are identical, going to confirmation page...")
        window["signup_layout1"].update(visible=False)
        window["signup_layout2"].update(visible=True)
        window["col15"].update(visible=False)
        window["col3"].update(visible=True)
        window["colshow_signup_step"].update(visible=True)
        window["txtshow_signup_step"].update("Step 1/5")
        signup_step = 2
        print("let's confirm if the email is yours")
    else:
        print("passwords are different")


def confirm_2to3(code):
    global signup_step
    print("confirming(not made yet) and going to product activation page...")
    window["signup_layout2"].update(visible=False)
    window["signup_layout3"].update(visible=True)
    window["txtshow_signup_step"].update("Step 2/5")
    signup_step = 3
    print("you can start activating your product")


def go_back():
    global signup_step, window
    if signup_step == 0 or signup_step == 1:
        print("Error, check def go_back func")
    elif signup_step == 2:
        print("going back to sign up page...")
        window["signup_layout2"].update(visible=False)
        window["signup_layout1"].update(visible=True)
        window["col15"].update(visible=True)
        window["col3"].update(visible=False)
        window["colshow_signup_step"].update(visible=False)
        signup_step = 1
        print("you are back in sign up page")
    elif signup_step == 3:
        print("Going back to sign up page...")
        window["signup_layout3"].update(visible=False)
        window["signup_layout1"].update(visible=True)
        window["col15"].update(visible=True)
        window["col3"].update(visible=False)
        window["colshow_signup_step"].update(visible=False)
        signup_step = 1
        print("You are back in sign up page")
    elif signup_step == 4:
        print("Going back to home(login) page...")
        window["signup_layout4"].update(visible=False)
        window["login_layout"].update(visible=True)
        window["col3"].update(visible=False)
        window["colshow_signup_step"].update(visible=False)
        signup_step = 0
        print("You are back in home(login) page")
    elif signup_step == 5:
        print("Going back to home(login) page...")
        window["signup_layout5"].update(visible=False)
        window["login_layout"].update(visible=True)
        window["col3"].update(visible=False)
        window["colshow_signup_step"].update(visible=False)
        signup_step = 0
        print("You are back in home(login) page")
    elif signup_step == 6:
        print("Going back to home(login) page...")
        window["signup_layout6"].update(visible=False)
        window["login_layout"].update(visible=True)
        window["col3"].update(visible=False)
        window["colshow_signup_step"].update(visible=False);
        signup_step = 0
        print("You are back in home(login) page")
    elif signup_step == 9:
        window["home_layout"].update(visible=True)
        window["history_layout"].update(visible=False)
        signup_step = 8



def check_product_code():
    return True


def nextbtn():
    global signup_step
    if signup_step == 4:
        print("allowing and going to emergency contact page...")
        window["signup_layout4"].update(visible=False)
        window["signup_layout5"].update(visible=True)
        window["txtshow_signup_step"].update("Step 4/5")
        signup_step = 5
        print("you are in the emergency contact page")
    elif signup_step == 5:
        print("going to body info page...")
        window["signup_layout5"].update(visible=False)
        window["signup_layout6"].update(visible=True)
        window["txtshow_signup_step"].update("Step 5/5")
        signup_step = 6
        print("you are in the body info page")


def execute_FD(h=users[0][3][0], w=users[0][3][1]):
    print("you have signed up/in, press 'q' to exit")
    FD.height, FD.width, FD.path_to_sound_file, FD.leeway = int(h), int(w), path_to_file_location + r'Danger_Alarm_Sound_Effect.wav', 1
    FD.main()
    print("you have exited")


def login(username, pw):
    global signup_step
    #if [username, pw] in users:
    if True:
        print("logging in...")
        window["colshow_signup_step"].update(visible=False)
        window["login_layout"].update(visible=False)
        window["home_layout"].update(visible=True)
        signup_step = 8
        print("logged in")
        #execute_FD(users[0][3][0], users[0][3][1])
    else:
        print("wrong")


def finish_signup(h="", w=""):
    global signup_step
    if len(str(h) + str(w)) > 1:
        if h.isnumeric() and w.isnumeric():
            window["colshow_signup_step"].update(visible=False)
            window["signup_layout6"].update(visible=False)
            window["home_layout"].update(visible=True)
            signup_step = 7
        else:
            print("please enter integers")
    else:
        print("both values are very important for the AI's calculations, please provide them")


def history_show():
    global signup_step
    global window
    window["home_layout"].update(visible=False)
    window["history_layout"].update(visible=True)
    signup_step = 9
    raw_dates = FD.get_fall_hist(path_to_file_location)
    formatted_dates = [f"year:{raw_date[0]}, month:{raw_date[1]}, day:{raw_date[2]}, hour:{raw_date[3]}, minute:{raw_date[4]}, second:{raw_date[5]}" for raw_date in raw_dates]
    window["fall_history_display"].update("\n".join(formatted_dates))


def clear_hist():
    FD.clear_fall_hist(path_to_file_location)
    window["fall_history_display"].update("")


def checkInput2(event):
    global signup_step, window
    if len(window["product_code"].get()) > 0:
        window["skip/next"].update("Next")
        if event == "skip/next":
            if check_product_code():
                print("going to the page for cam allowance...")
                window["signup_layout3"].update(visible=False)
                window["signup_layout4"].update(visible=True)
                window["txtshow_signup_step"].update("Step 3/5")
                signup_step = 4
                print("gone to the page for cam allowance")
    else:
        window["skip/next"].update("Skip")
        if event == "skip/next":
            print("going to the page for emergency contacts...")
            window["signup_layout3"].update(visible=False)
            window["signup_layout5"].update(visible=True)
            window["txtshow_signup_step"].update("Step 4/5")
            signup_step = 5
            print("gone to the page for emergency contacts")


def checkInput5(values):
    global signup_step, contact_input_list, window
    if len(values[f"emergency number {str(len(contact_input_list))}"]) > 0 and len(contact_input_list) < 5:  # the last line has text
        contact_input_list += ["0"]
        window[f"Emergency Number {str(len(contact_input_list))}"].update(visible=True)
        window[f"emergency number {str(len(contact_input_list))}"].update(visible=True)

    elif len(values[f"emergency number {str(len(contact_input_list)-1)}"]) == 0 and len(contact_input_list) > 2:  # the last and second last lines are empty
        contact_input_list.pop()
        window[f"Emergency Number {str(len(contact_input_list)+1)}"].update(visible=False)
        window[f"emergency number {str(len(contact_input_list)+1)}"].update(visible=False)


def change_lang():
    global window, current_lang
    current_lang = abs(current_lang - 1)
    for i in range(len(window.element_list())):
        if str(window.element_list()[i])[25] == "T":
            window.element_list()[i].update(window.element_list()[i].get())
        elif str(window.element_list()[i])[25] == "B":
            window.element_list()[i].update(window.element_list()[i].get_text())



run = True
while run:
    event, values = window.read(timeout=100)
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    elif event == "lang":
        change_lang()  # not done, it failed (no change), suggest making .update() for every element :(
    elif event == "login":
        login(values["email"], values["pw"])
    elif event == "sign up":
        goto_signup_page()
    elif event == "sign in":
        goto_login_page()
    elif event == "continue":
        signup_1to2(values["new email"], values["new pw"], values["new pw2"])
    elif event == "confirm 2to3":
        confirm_2to3(values["confirmation code"])
    elif event == "Allow":
        nextbtn()
    elif event[:4] == "back":
        go_back()
    elif event == "next":
        nextbtn()
    elif event == "finish_signup":
        finish_signup(values["height"], values["shoulder_width"])
    elif event == "view_cam":
        if signup_step == 7:
            execute_FD(values["height"], values["shoulder_width"])
        elif signup_step == 8:
            execute_FD()
    elif event == "history":
        history_show()
    elif event == "clear_history":
        clear_hist()
    elif event == "sound_test":
        FD.test_sound = not FD.test_sound
        window["sound_test"].update(f"Test for sound: {FD.test_sound}")
    elif signup_step == 3:
        checkInput2(event)
    elif signup_step == 5:
        checkInput5(values)
print("thank you for using the infallible fall detector")
window.close()
