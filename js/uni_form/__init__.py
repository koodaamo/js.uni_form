import os

from fanstatic import Library, Group, Resource

library = Library('uni_form', 'resources')

pth = library.path

fnames = lambda subp, ext: [fn for fn in os.listdir(library.path + os.sep + subp) if fn.endswith(ext)]

css_resources = [Resource(library, 'css' + os.sep + fn) for fn in fnames('css', 'css')]
js_resources = [Resource(library, 'js' + os.sep + fn) for fn in fnames('js', 'js')]
i18n_resources = [Resource(library, 'localization' + os.sep + fn) for fn in fnames('localization', 'js')]

css = Group(css_resources)
js = Group(js_resources)
i18n = Group(i18n_resources)

uni_form = Group([css, js, i18n])
