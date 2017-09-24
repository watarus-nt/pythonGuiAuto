import pyautogui
import time


class ImageHandler(object):
    """"
    The helper to handle image related actions
    """

    def __init__(self, _timeOut=10):
        self.timeOut = _timeOut

    def wait_for_image(self, image_path, _timeout= None):
        """
        wait for image to be displayed on the screen
        :param image_path:
        :param _timeout: using default timeout if user doesn't input anything
        :return: img_location with 4 coordinates
        """
        if _timeout is None:
            _timeout = self.timeOut

        print "*INFO* wait_for_image() - Wait for image with path = %s" % image_path
        # image_path = str(image_path)

        _count = 1
        img_location = None
        while True:
            img_location = pyautogui.locateOnScreen(image_path, grayscale=True)
            if img_location is not None:
                print "*INFO* wait_for_image() - Expected image has been displayed on the screen"
                break
            if _count < _timeout:
                print "*INFO* wait_for_image() - Count= %d - Image hasn't been displayed" \
                      " on screen, wait 1s before rechecking " % _count
                _count += 1
                time.sleep(1)
            else:
                print "*FAIL* wait_for_image() - Can't find image after %d seconds" % _timeout
                raise RuntimeError("wait_for_image() - Can't find image after %d seconds") % _timeout
        return img_location

    def get_image_location(self, image_path):
        """
        get image location on screen
        :param image_path: image's path
        :return: x_coordinate and y_coordinate of the image if found
        """
        image_path = str(image_path)
        # wait for image to be displayed before getting it location on screen
        img_location = self.wait_for_image(image_path)

        print "*INFO* get_image_location() - Try to get image with path = %s" % image_path
        if img_location is not None:
            img_location_x, img_location_y = pyautogui.center(img_location)
            print "*INFO* get_image_location() - Found image at X= %s  Y= %s" % (img_location_x, img_location_y)
            return img_location_x, img_location_y
        else:
            print "*INFO* get_image_location() - Can't find image on the screen"
            raise LookupError('Can\'t find image on the screen')

    def get_image_x_coordinate(self, image_path):
        image_path = str(image_path)
        return self.get_image_location(image_path)[0]

    def get_image_y_coordinate(self, image_path):
        image_path = str(image_path)
        return self.get_image_location(image_path)[1]

    def click_image(self, image_path):
        """
        click on image
        :param image_path: image's path
        :return: nothing
        """
        image_path = str(image_path)
        img_location_x, img_location_y = self.get_image_location(image_path)
        print "*INFO* Clicking image at X=%s, Y=%s" % (img_location_x, img_location_y)
        pyautogui.click(img_location_x, img_location_y)
        time.sleep(1)