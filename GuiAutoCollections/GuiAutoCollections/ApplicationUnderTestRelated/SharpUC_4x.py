from pywinauto import Application
import pyautogui
import time


class SharpUC_4x(object):
    """
    Test library for testing *SharpUC 4.x application*
    """

    def __init__(self, _app_location=None):
        if _app_location is None:
            self.appLocation = "C:\\Program Files\\VW-eBook-AC\\Bookshelf.exe"
        else:
            self.appLocation = _app_location

        self.currentWindow = None
        self.name = None

    def start_vwebooks_app(self):
        """
        Start the Bookshelf app for testing
        """
        print "*INFO* Starting Bookshelf app...."
        # app = Application().Start(cmd_line=u'"C:\\Program Files\\VW-eBook-AC\\Bookshelf.exe" ')
        app = Application().Start(cmd_line=self.appLocation)
        cefclient = app.CEFCLIENT
        cefclient.Wait('ready')

        print "*INFO* Finding ok button image to click..."  # We have to click on Ok butotn to see bookshelf content
        # self.click_image('images/start_ok_button.PNG')
        _x_coordinate, _y_coordinate = self.get_image_location('images/13001.PNG')  # get the location of 13001 text
        pyautogui.click(_x_coordinate - 10, _y_coordinate + 40)  # click the ok button based on above location
        self.currentWindow = cefclient

    def wait_for_app_to_be_ready(self, name, app_type):
        """
        Use this keyword to wait for the app before executing new action
        """
        print "*INFO* wait_for_app_to_be_ready() is called!"
        time.sleep(3)
        name = str(name)
        if app_type == "reflow":
            app = Application().Connect(title=name, class_name='WindowsForms10.Window.8.app.0.74db74_r11_ad1')
        elif app_type == "bigImage":
            app = Application().Connect(title=name, class_name='WindowsForms10.Window.8.app.0.11c3e_r11_ad1')
        else:
            print "Wrong app_type is passed to this method! app_type = %s" % app_type
            print "Correct app_type is reflow or bigImage"
            raise ValueError('Wrong appType value has been given!')

        self.currentWindow = app[name]
        self.currentWindow.Wait('ready')
        self.name = name

    def wait_for_app_to_be_clickable(self):
        self.currentWindow.Wait('ready')

    def click_GUI_Element(self, locator):
        """
        Use this keyword to click on an element on GUI based on its locator
        """
        self.wait_for_app_to_be_clickable()
        locator = str(locator)
        _currentWindow = self.currentWindow[locator]
        _currentWindow.Click()

    def clear_text(self):
        """
        Use this keyword to clear text in a textbox (after clicking to that textbox)
        :return:
        """
        self.wait_for_app_to_be_clickable()
        pyautogui.keyDown('shift')
        pyautogui.press('end')
        pyautogui.keyUp('shift')
        pyautogui.press('backspace')

    def input_text(self, text):
        """
        Use this keyword to input text to at current pointer
        :param text:
        :return:
        """
        self.wait_for_app_to_be_clickable()
        self.clear_text()
        text = str(text)
        pyautogui.typewrite(text)

    def click_to_bookmark_text_field(self):
        """
        This is a specific keyword to click bookmark text field
        :return:
        """
        self.currentWindow.Edit.Click()
        time.sleep(1)
