from pywinauto import Application
import pyautogui
import time
from pywinauto import keyboard


class pywinAutoKeywords(object):
    """Test library for testing *Calculator* business logic.

    Interacts with the calculator directly using its ``push`` method.
    """

    def __init__(self):

        self._result = ''
        self.currentWindow= ''
        self.currentWorking = None
        self.name = ''

    def start_vwEbooks_app(self):
        print "*INFO* Starting Bookshelf app...."
        app = Application().Start(cmd_line=u'"C:\\Program Files\\VW-eBook-AC\\Bookshelf.exe" ')
        cefclient = app.CEFCLIENT
        cefclient.Wait('ready')

        print "*INFO* Finding ok button image to click..."
        # self.click_image('images/start_ok_button.PNG')
        _x_cordinate, _y_cordinate = self.get_image_location('images/13001.PNG')  #get the location of 13001 text
        pyautogui.click(_x_cordinate - 10, _y_cordinate + 40) # click the ok button based on above location

        # time.sleep(2)
        # keyboard.SendKeys("{ENTER}")
        # self.currentWindow = cefclient



    def wait_for_app_to_be_ready(self, name, app_type):
        time.sleep(3)
        name = str(name)
        try:
            if app_type == "reflow":
                app = Application().Connect(title= name, class_name='WindowsForms10.Window.8.app.0.74db74_r11_ad1')
            elif app_type == "bigImage":
                app = Application().Connect(title= name, class_name='WindowsForms10.Window.8.app.0.11c3e_r11_ad1')
        except:
            print "Wrong app_type is passed to this method! app_type = %s" % app_type
            print "Correct app_type is reflow or bigImage"
            return None

        windowsformswindowappdbrad = app[name]
        self.currentWorking = windowsformswindowappdbrad
        windowsformswindowappdbrad.Wait('ready')
        self.currentWindow = windowsformswindowappdbrad
        self.name = name

    def wait_for_app_to_be_clickable(self):
        self.currentWorking.Wait('ready')

    def wait_for_image(self, image_path):
        print "*INFO* wait_for_image() - Wait for image with path = %s" % image_path
        time.sleep(2)
        # image_path = str(image_path)
        _found_image = False
        _count=1
        img_location = None
        while not _found_image:
            img_location = pyautogui.locateOnScreen(image_path, grayscale=True)
            if img_location is not None:
                _found_image = True
                print "*INFO* wait_for_image() - Expected image has been displayed on the screen"
                break
            if _count < 6:
                print "*INFO* wait_for_image() - Count= %d - Image hasn't been displayed" \
                      " on screen, wait 1s before rechecking " % _count
                _count += 1
                time.sleep(1)
            else:
                print "*FAIL* wait_for_image() - Can't find image after 5 seconds"
                raise RuntimeError("wait_for_image() - Can't find image after 5 seconds")
        return img_location

    def get_image_location(self, image_path):
        image_path = str(image_path)
        img_location = self.wait_for_image(image_path)
        img_location_x, img_location_y = None, None
        print "*INFO* get_image_location() - Try to get image with path = %s" % image_path
        if img_location is not None:
            img_location_x, img_location_y =  pyautogui.center(img_location)
            print "*INFO* get_image_location() - Found image at X= %s  Y= %s" % (img_location_x, img_location_y)
        else:
            print "*INFO* get_image_location() - Can't find image on the screen"
            raise LookupError('Can\'t find image on the screen')

        return img_location_x, img_location_y
    
    def get_image_x_coordinate(self, image_path):
        image_path = str(image_path)
        return self.get_image_location(image_path)[0]
    
    def get_image_y_coordinate(self, image_path):
        image_path = str(image_path)
        return self.get_image_location(image_path)[1]
    
    def click_image(self, image_path):
        # print "image_path type = ",
        # print type(image_path)
        # print "image_path = %s" % image_path
        image_path = str(image_path)
        img_location_x, img_location_y = self.get_image_location(image_path)
        print "*INFO* Clicking image at X=%s, Y=%s" %(img_location_x, img_location_y)
        pyautogui.click(img_location_x, img_location_y)
        time.sleep(2)
     
    def click_GUI_Element(self, locator):
        self.wait_for_app_to_be_clickable()
        # self.wait_for_app_to_be_ready(self.name)
        locator = str(locator)
        _currentWindow = self.currentWindow[locator]
        _currentWindow.Click()

    def move_mouse(self, location_x, location_y):
        time.sleep(1)
        pyautogui.click(location_x, location_y)  # click to put drawing program in focus
        distance = 100
        pyautogui.dragRel(-distance, 0, duration=0.5)  # move left
        pyautogui.dragRel(0, distance, duration=0.5)  # move down
        pyautogui.dragRel(distance, 0, duration=0.5)  # move right
        pyautogui.dragRel(0, -distance, duration=0.5)  # move up

    def clear_text(self):
        self.wait_for_app_to_be_clickable()
        pyautogui.keyDown('shift')
        pyautogui.press('end')
        pyautogui.keyUp('shift')
        pyautogui.press('backspace')
        
    def input_text(self, text):
        self.wait_for_app_to_be_clickable()
        self.clear_text()
        text = str(text)
        pyautogui.typewrite(text)
        
    def click_to_bookmark_text_field(self):
        self.currentWindow.Edit.Click()
        time.sleep(1)
    # def close_windows_by_keyboards(self):
    #     keyboard.SendKeys('%{F4}')
        
        
time.sleep(3)
app = pywinAutoKeywords()
app.start_vwEbooks_app()