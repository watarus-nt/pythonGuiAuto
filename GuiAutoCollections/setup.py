try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'GuiAutoCollections',
    'author': 'Hung Tran',
    'url': 'https://github.com/watarus-nt/pythonGuiAuto',
    'dowload_url': 'https://github.com/watarus-nt/pythonGuiAuto.git',
    'author_email': 'watarus.nt@gmail.com',
    'version': '0.1',
    'install_requires': ['pyautogui', 'pywinauto'],
    'scripts': [],
    'name': 'projectName'
}

setup (**config)
