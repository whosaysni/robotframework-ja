from codecs import open
from io import StringIO

from robot.libdoc import ConsoleViewer
from robot.libdocpkg.robotbuilder import LibraryDocBuilder


class BufferEmitter(ConsoleViewer):

    def __init__(self, libdoc):
        ConsoleViewer.__init__(self, libdoc)
        self.doc = StringIO()
        
    def _console(self, msg):
        self.doc.write(unicode(msg)+'\n')


library_names = (
    "BuiltIn",
    "Collections",
    "DateTime",
    "Dialogs",
    "OperatingSystem",
    "Process",
    "Screenshot",
    "String",
    "Telnet",
    "XML"
    )


for library_name in library_names:
    mod_name = 'robot.libraries.' + library_name
    libdoc = LibraryDocBuilder().build(mod_name)
    con = BufferEmitter(libdoc); con.view('show')
    rst = con.doc.getvalue()
    with open('%s.rst' % (library_name), 'wb', encoding='utf-8') as output:
        output.write(rst)
        output.close()
